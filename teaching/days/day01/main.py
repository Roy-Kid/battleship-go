"""03 合并与键盘控制 | 方向键移动 R旋转 +/-缩放 空格复位
运行：python main.py
只修改“本次重点”里的数值，再保存、关闭旧窗口、重新运行。
"""
from pathlib import Path
import sys
import pygame

# 【老师提供的固定支架】每个实验都保留相同的窗口与退出处理。
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("03 合并与键盘控制 | 方向键移动 R旋转 +/-缩放 空格复位")
clock = pygame.time.Clock()
ASSETS = Path(__file__).resolve().parent / "assets"

original = pygame.image.load(str(ASSETS / "ship.png"))
sea = pygame.image.load(str(ASSETS / "sea.png"))
sea = pygame.transform.scale(sea, (800, 600))
# 【合并A】把位置、旋转角度和缩放倍数分别保存为变量。
x, y = 400, 300
angle = 0
scale = 2.0
# 本文件采用图片中心定位：旋转和缩放时中心保持不动。
# 01_scene.py使用左上角定位；此处明确改为中心定位。

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 【合并B】离散操作：按一次键，执行一次。
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                angle = (angle + 90) % 360
            if event.key in (pygame.K_EQUALS, pygame.K_PLUS, pygame.K_KP_PLUS):
                scale = min(4.0, scale + 0.25)
            if event.key in (pygame.K_MINUS, pygame.K_KP_MINUS):
                scale = max(0.5, scale - 0.25)
            if event.key == pygame.K_SPACE:
                x, y, angle, scale = 400, 300, 0, 2.0

    # 【合并C，选做】连续操作：每圈检查方向键是否仍被按住。
    # 先合并旋转和缩放；再加入这里的移动代码，作为第二天的引子。
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 4
    if keys[pygame.K_RIGHT]:
        x += 4
    if keys[pygame.K_UP]:
        y -= 4
    if keys[pygame.K_DOWN]:
        y += 4
    # 这一版允许移动到画面外，按空格可以复位。

    # 【合并D】每圈都根据当前变量，从原图生成需要显示的图片。
    width = max(1, int(original.get_width() * scale))
    height = max(1, int(original.get_height() * scale))
    scaled = pygame.transform.scale(original, (width, height))
    picture = pygame.transform.rotate(scaled, angle)
    rect = picture.get_rect(center=(x, y))
    # 【合并E】先海面、再舰船；最后由固定支架刷新。
    screen.blit(sea, (0, 0))
    screen.blit(picture, rect)

    # 【固定支架】刷新画面，限制速度；--smoke 只供老师自动检查。
    pygame.display.flip()
    clock.tick(60)
    if "--smoke" in sys.argv:
        running = False

pygame.quit()
