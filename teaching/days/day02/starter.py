"""直接运行：python main.py。--smoke 仅供老师检查启动。"""
from pathlib import Path
import sys
import pygame

# 素材路径由老师准备；从任何目录启动都能找到素材。
ASSETS = Path(__file__).resolve().parent / "assets"
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Battleship Lab")
clock = pygame.time.Clock()
sea = pygame.image.load(str(ASSETS / "sea.png"))
sea = pygame.transform.scale(sea, (800, 600))
ship = pygame.image.load(str(ASSETS / "ship.png"))
ship = pygame.transform.scale(ship, (48, 144))

# 今天重点修改的变量：位置和颜色。
x = 200
y = 180
background = (15, 60, 85)

running = True
while running:
    # 接收操作：先只处理关闭窗口。
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 绘制顺序：背景 → 海面 → 舰船 → 刷新。
    screen.fill(background)
    screen.blit(sea, (0, 0))
    screen.blit(ship, (x, y))
    pygame.display.flip()
    clock.tick(60)
    if "--smoke" in sys.argv:  # 老师的自动检查，可以跳过。
        running = False

pygame.quit()
