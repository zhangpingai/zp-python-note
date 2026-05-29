Python 使用 WebSocket 的学习路径可以从**基础概念**、**标准库实现**、**常用框架集成**到**生产环境部署与扩展**。

以下是从入门到精通的完整指南。

### 第一阶段：基础入门 (原理与原生库)

首先了解 WebSocket 是什么：它是一种在单个 TCP 连接上进行**全双工**通信的协议。与 HTTP 不同，服务器可以主动向客户端推送消息。

#### 1\. 环境准备

Python 处理 WebSocket 最常用的库是 websockets（基于 asyncio）。

```bash
pip install websockets
```

#### 2\. 写一个最简单的 Echo Server (服务端)

这个服务接收客户端消息，然后原样发回去。

```python
# server.py
import asyncio
import websockets

async def echo(websocket):
    # websocket 参数代表一个具体的连接
    async for message in websocket:
        print(f"收到消息: {message}")
        await websocket.send(f"服务器回复: {message}")

async def main():
    # 启动服务，监听 localhost 的 8765 端口
    async with websockets.serve(echo, "localhost", 8765):
        print("WebSocket 服务已启动...")
        await asyncio.Future()  # 运行直到被手动停止

if __name__ == "__main__":
    asyncio.run(main())
```

#### 3\. 写一个客户端 (Client)

```python
# client.py
import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("请输入你的名字: ")

        await websocket.send(name)
        print(f"> 发送: {name}")

        greeting = await websocket.recv()
        print(f"< 接收: {greeting}")

if __name__ == "__main__":
    asyncio.run(hello())
```

### 第二阶段：进阶应用 (广播与逻辑处理)

在真实应用中，你通常需要管理多个连接（例如聊天室），需要处理用户断开连接的情况。

#### 1\. 实现一个简单的聊天室 (广播)

我们需要一个容器来存储所有活跃的连接。

```python
# chat_server.py
import asyncio
import websockets

# 存放所有连接的集合
CONNECTED_CLIENTS = set()

async def handler(websocket):
    # 1. 注册连接
    CONNECTED_CLIENTS.add(websocket)
    try:
        async for message in websocket:
            # 2. 广播消息给所有其他用户
            websockets.broadcast(CONNECTED_CLIENTS, f"有人说: {message}")
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        # 3. 注销连接 (无论正常断开还是异常，都要移除)
        CONNECTED_CLIENTS.remove(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
```

### 第三阶段：框架集成 (现代 Web 开发)

在实际工作中，你很少单独运行一个 WebSocket 服务，而是将其集成在 Web 框架中。

#### 1\. FastAPI (最推荐的现代方案)

FastAPI 原生支持 WebSocket，非常简单且性能极高。

```bash
pip install fastapi uvicorn
```
```python
# main.py
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"用户 {client_id} 说: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"用户 {client_id} 离开了")

# 启动命令: uvicorn main:app --reload
```

#### 2\. Django Channels (适合 Django 生态)

如果你的项目是 Django，你需要使用 **Django Channels**。它将 Django 从同步转为异步，支持 WebSocket。

-   配置较复杂（需要 ASGI 配置，Redis 作为 Channel Layer）。
-   优势是可以使用 Django 的 ORM 和认证系统。

#### 3\. Socket.IO (Python-SocketIO)

**注意**：WebSocket 是协议，Socket.IO 是一个库（即使不支持 WS 也能通过长轮询回退）。如果你的前端用的是 socket.io-client，后端必须用 python-socketio，不能用原生 Websocket。

-   **特点**：自动重连、心跳机制、Room（房间）概念完善。

### 第四阶段：精通与生产环境 (架构与扩展)

当你面对高并发或分布式部署时，仅仅会写代码是不够的。

#### 1\. 横向扩展 (Scaling)

**问题**：如果在生产环境启动了 10 个 Python 进程（Worker），用户 A 连在 进程1，用户 B 连在 进程2。进程1 没法直接把消息推给 进程2 的用户。

**解决方案**：使用 **Redis Pub/Sub (发布/订阅)**。

-   所有 WebSocket 进程都订阅 Redis 的某个 Channel。
-   当需要广播时，将消息发布到 Redis。
-   所有进程收到 Redis 消息后，再转发给自己持有的 WebSocket 连接。

#### 2\. 鉴权 (Authentication)

WebSocket 建立连接是基于 HTTP 握手的。

-   **方法 A (URL 参数)**: ws://api.com/ws?token=xyz。在连接建立(connect)时验证 token。
-   **方法 B (Header)**: 浏览器原生的 WebSocket 对象通常不支持自定义 Header，但有些库支持。通常推荐用 URL 参数或在连接建立后的第一条消息发送 Token 进行认证。

#### 3\. 心跳检测 (Heartbeat / Ping-Pong)

网络设备（防火墙、负载均衡）通常会切断长时间没有数据传输的 TCP 连接。

-   **做法**：服务端定期发送 ping，客户端回复 pong。
-   websockets 库和 FastAPI 通常默认开启了 Ping/Pong，但在配置 Nginx 时需要注意设置 proxy\_read\_timeout。

#### 4\. Nginx 反向代理配置

生产环境通常用 Nginx 做入口，必须配置 Upgrade 头才能支持 WebSocket。

```nginx
location /ws/ {
  proxy_pass http://127.0.0.1:8000;
  proxy_http_version 1.1;
  proxy_set_header Upgrade $http_upgrade; # 关键
  proxy_set_header Connection "upgrade";  # 关键
  proxy_set_header Host $host;
  proxy_read_timeout 600s; # 防止 Nginx 切断长连接
}
```

### 总结：学习路线图
-   **Level 1 (小白)**: 玩转 websockets 库，理解 async/await，跑通 Hello World。
-   **Level 2 (开发者)**: 使用 **FastAPI** 构建带业务逻辑的 WS 接口，处理 JSON 数据，处理断连。
-   **Level 3 (工程师)**: 处理 **鉴权**，使用 **Docker** 部署，配置 **Nginx** 反向代理。
-   **Level 4 (架构师)**: 使用 **Redis** 实现多进程/多服务器的消息同步（广播），处理百万级并发连接的资源优化。

**推荐练习项目**：
-   实时聊天室（支持群聊、私聊）。
-   股票/加密货币价格实时推送面板。
-   简单的多人在线小游戏（如贪吃蛇）。