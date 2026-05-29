#!/usr/bin/env python3
import argparse
import base64
import json
import os
import shutil
import sys
import time
from pathlib import Path
from urllib import error, request


GATEWAY_ENV_PATH = Path.home() / ".gateway.env"
DEFAULT_BASE_URL = "https://api.apimart.ai/v1"
STYLE_FILE = Path(__file__).resolve().parent.parent / "data" / "style_profiles.json"


def read_gateway_env(path: Path) -> dict:
    data = {}
    if not path.exists():
        raise FileNotFoundError(f"未找到网关环境文件: {path}")
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, val = line.split("=", 1)
        data[key.strip()] = val.strip()
    return data


def http_json(method: str, url: str, token: str, payload=None):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    body = None
    if payload is not None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = request.Request(url=url, method=method, headers=headers, data=body)
    try:
        with request.urlopen(req, timeout=60) as resp:
            charset = resp.headers.get_content_charset() or "utf-8"
            text = resp.read().decode(charset, errors="replace")
            if not text.strip():
                return {}
            return json.loads(text)
    except error.HTTPError as e:
        text = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {e.code} {url}\n{text}") from e


def ensure_style_profile(series: str) -> dict:
    STYLE_FILE.parent.mkdir(parents=True, exist_ok=True)
    if STYLE_FILE.exists():
        all_profiles = json.loads(STYLE_FILE.read_text(encoding="utf-8") or "{}")
    else:
        all_profiles = {}

    if series in all_profiles:
        return all_profiles[series]

    # 首篇自动固化系列风格
    base_styles = [
        "现代教育插画风",
        "清晰信息图风",
        "科技感轻扁平风",
        "专业讲师课件封面风",
    ]
    color_sets = [
        "蓝青渐变主色，白色点缀",
        "深蓝灰主色，橙色强调",
        "青绿主色，深灰文字对比",
        "蓝紫渐变背景，冷白高光",
    ]
    idx = abs(hash(series)) % len(base_styles)
    profile = {
        "style_name": base_styles[idx],
        "palette": color_sets[idx],
        "composition": "中心主视觉 + 简洁背景图形 + 教学主题元素",
        "constraints": "无logo、无水印、画面干净、信息聚焦",
    }
    all_profiles[series] = profile
    STYLE_FILE.write_text(json.dumps(all_profiles, ensure_ascii=False, indent=2), encoding="utf-8")
    return profile


def extract_title(md_path: Path) -> str:
    for line in md_path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.strip().startswith("# "):
            return line.strip()[2:].strip()
    return md_path.stem


def build_prompt(topic: str, series: str, style_profile: dict, cover_text: str | None, style_hint: str | None) -> str:
    parts = [
        f"为IT课程讲义生成16:9封面图，主题是：{topic}",
        f"课程系列：{series}",
        f"风格统一要求：{style_profile['style_name']}，配色：{style_profile['palette']}",
        f"构图要求：{style_profile['composition']}",
        "主视觉元素：电脑/代码/数据图形/学习场景，体现技术与教学结合",
        "画面质量高，层次清晰，可用于课程讲义封面",
        "允许中文标题文字",
        style_profile["constraints"],
    ]
    if cover_text:
        parts.append(f"封面文字：{cover_text}")
    if style_hint:
        parts.append(f"附加风格提示：{style_hint}")
    return "；".join(parts)


def submit_generation(base_url: str, token: str, prompt: str, resolution: str) -> dict:
    payload = {
        "model": "gpt-image-2",
        "prompt": prompt,
        "n": 1,
        "size": "16:9",
        "resolution": resolution,
    }
    return http_json("POST", f"{base_url}/images/generations", token, payload)


def find_task_id(data: dict) -> str | None:
    for key in ("task_id", "id", "taskId"):
        if isinstance(data.get(key), str):
            return data[key]
    nested = data.get("data")
    if isinstance(nested, dict):
        for key in ("task_id", "id", "taskId"):
            if isinstance(nested.get(key), str):
                return nested[key]
    return None


def poll_task(base_url: str, token: str, task_id: str, poll_interval: int, timeout: int) -> dict:
    # 按异步任务接口轮询
    url = f"{base_url}/tasks/{task_id}"
    start = time.time()
    while True:
        result = http_json("GET", url, token, None)
        state = (
            result.get("status")
            or (result.get("data", {}) if isinstance(result.get("data"), dict) else {}).get("status")
            or ""
        )
        state_l = str(state).lower()
        if state_l in {"succeeded", "success", "completed", "done"}:
            return result
        if state_l in {"failed", "error", "cancelled"}:
            raise RuntimeError(f"任务失败: {json.dumps(result, ensure_ascii=False)}")
        if time.time() - start > timeout:
            raise TimeoutError(f"任务轮询超时({timeout}s), task_id={task_id}")
        time.sleep(poll_interval)


def extract_image_bytes(result: dict) -> bytes:
    # 兼容 url 或 base64 两种结构
    candidates = []
    if isinstance(result.get("data"), dict):
        candidates.append(result["data"])
    candidates.append(result)

    for c in candidates:
        # 常见 images 数组
        images = c.get("images")
        if isinstance(images, list) and images:
            first = images[0]
            if isinstance(first, dict):
                if "b64_json" in first and isinstance(first["b64_json"], str):
                    return base64.b64decode(first["b64_json"])
                if "url" in first and isinstance(first["url"], str):
                    return download(first["url"])
            if isinstance(first, str) and first.startswith("http"):
                return download(first)
        # 单对象字段
        if isinstance(c.get("url"), str):
            return download(c["url"])
        if isinstance(c.get("b64_json"), str):
            return base64.b64decode(c["b64_json"])
    raise RuntimeError(f"未找到可下载图像字段: {json.dumps(result, ensure_ascii=False)}")


def download(url: str) -> bytes:
    req = request.Request(url=url, method="GET")
    with request.urlopen(req, timeout=120) as resp:
        return resp.read()


def target_paths(markdown_file: Path) -> tuple[Path, Path]:
    out_dir = markdown_file.parent / "assets" / markdown_file.stem
    out_dir.mkdir(parents=True, exist_ok=True)
    cover = out_dir / "cover.png"
    backup = out_dir / "cover.bak.png"
    return cover, backup


def backup_then_write(cover: Path, backup: Path, image_bytes: bytes):
    if cover.exists():
        shutil.copy2(cover, backup)
    cover.write_bytes(image_bytes)


def run_once(args, resolution: str) -> Path:
    env = read_gateway_env(GATEWAY_ENV_PATH)
    token = env.get("APIMART_API_KEY")
    if not token:
        raise RuntimeError("未在 .gateway.env 中读取到 APIMART_API_KEY")
    base_url = env.get("APIMART_BASE_URL", DEFAULT_BASE_URL).rstrip("/")

    md = Path(args.markdown).resolve()
    if not md.exists():
        raise FileNotFoundError(f"Markdown 文件不存在: {md}")

    series = args.series.strip()
    style_profile = ensure_style_profile(series)
    topic = extract_title(md)
    prompt = build_prompt(topic, series, style_profile, args.cover_text, args.style_hint)

    submit = submit_generation(base_url, token, prompt, resolution)
    task_id = find_task_id(submit)
    if not task_id:
        raise RuntimeError(f"提交成功但未返回 task_id: {json.dumps(submit, ensure_ascii=False)}")

    result = poll_task(base_url, token, task_id, args.poll_interval, args.timeout)
    image_bytes = extract_image_bytes(result)
    cover, backup = target_paths(md)
    backup_then_write(cover, backup, image_bytes)
    return cover


def main():
    parser = argparse.ArgumentParser(description="Generate lecture cover via APIMart GPT-Image-2")
    parser.add_argument("--markdown", required=True, help="目标讲义 markdown 文件路径")
    parser.add_argument("--series", required=True, help="课程系列名，用于风格统一")
    parser.add_argument("--cover-text", default="", help="封面文字（可空）")
    parser.add_argument("--style-hint", default="", help="附加风格提示（可空）")
    parser.add_argument("--poll-interval", type=int, default=4, help="任务轮询间隔秒")
    parser.add_argument("--timeout", type=int, default=240, help="任务轮询超时秒")
    args = parser.parse_args()

    # 默认 2k，失败自动降级；失败后自动重试 2 次（总 3 次）
    resolutions = ["2k", "1k"]
    attempts = 3
    last_err = None
    for attempt in range(1, attempts + 1):
        for res in resolutions:
            try:
                output = run_once(args, res)
                print(str(output))
                return
            except Exception as e:
                last_err = e
                # 继续尝试下一个分辨率或下一次重试
                continue
        time.sleep(1)

    raise SystemExit(f"生成失败: {last_err}")


if __name__ == "__main__":
    main()
