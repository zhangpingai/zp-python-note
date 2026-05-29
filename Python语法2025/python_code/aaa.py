import pygame
import random
import sys

# 初始化 Pygame
pygame.init()

# 设置窗口大小
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("贪吃蛇游戏")

# 颜色定义
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# 蛇和食物的初始位置
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
food_spawn = True

# 初始移动方向
direction = "RIGHT"
change_to = direction

# 游戏速度
clock = pygame.time.Clock()
snake_speed = 15

# 分数
score = 0

# 游戏结束函数
def game_over():
    pygame.quit()
    sys.exit()

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                if direction != "DOWN":
                    change_to = "UP"
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                if direction != "UP":
                    change_to = "DOWN"
            elif event.key == pygame.K_LEFT or event.key == ord('a'):
                if direction != "RIGHT":
                    change_to = "LEFT"
            elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                if direction != "LEFT":
                    change_to = "RIGHT"

    # 更新方向
    direction = change_to

    # 移动蛇头
    if direction == "UP":
        snake_pos[1] -= 10
    elif direction == "DOWN":
        snake_pos[1] += 10
    elif direction == "LEFT":
        snake_pos[0] -= 10
    elif direction == "RIGHT":
        snake_pos[0] += 10

    # 蛇吃到食物
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # 重新生成食物
    if not food_spawn:
        food_pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
    food_spawn = True

    # 游戏结束条件
    if snake_pos[0] < 0 or snake_pos[0] >= SCREEN_WIDTH or snake_pos[1] < 0 or snake_pos[1] >= SCREEN_HEIGHT:
        game_over()
    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    # 绘制游戏界面
    screen.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # 显示分数
    font = pygame.font.SysFont("Arial", 20)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (0, 0))

    # 更新显示
    pygame.display.update()

    # 控制游戏速度
    clock.tick(snake_speed)
