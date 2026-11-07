"""第二步：旋转与缩放同一张图片。
运行：python 02_transform.py
左侧原图，右侧处理结果。每次只改一个参数，观察变化。
"""
from pathlib import Path
import sys
import pygame

# 【老师提供】固定的窗口支架。
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("02 图片变换 | 左侧原图，右侧结果")
clock = pygame.time.Clock()
ASSETS = Path(__file__).resolve().parent / "assets"
original = pygame.image.load(str(ASSETS / "ship.png"))

# 【学生重点1】修改尺寸。原图20×100，60×300按比例放大3倍。
# 先保持angle为0，只改width/height；再试试100×100，观察形状。
width = 60
height = 300
# 【学生重点2】修改角度：正数逆时针，负数顺时针，单位是度。
# 依次试0、90、180、45、-90，先预测再运行。
angle = 0

# 【学生重点3】组合两种操作：先缩放，再旋转；结果各保存为一个变量。
# 始终从original开始处理，避免反复缩小、放大导致清晰度下降。
scaled = pygame.transform.scale(original, (width, height))
picture = pygame.transform.rotate(scaled, angle)

# 【老师提供】中心对齐，方便比较；旋转后图片宽高可能改变。
# 这里原图与结果放在不同位置；正负角度方向不受摆放位置影响。
original_rect = original.get_rect(center=(200, 300))
picture_rect = picture.get_rect(center=(600, 300))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((15, 60, 85))
    screen.blit(original, original_rect)
    screen.blit(picture, picture_rect)

    pygame.display.flip()
    clock.tick(60)
    if "--smoke" in sys.argv:
        running = False

pygame.quit()
