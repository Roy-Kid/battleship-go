"""第一步：画出完整场景。
运行：python 01_scene.py
学生重点：变量、位置、图片加载与绘制顺序。
"""
from pathlib import Path
import sys
import pygame

# 【老师提供】窗口、时钟和素材路径，不单独拆成课程。
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("01 场景 | 修改位置与绘制顺序")
clock = pygame.time.Clock()
ASSETS = Path(__file__).resolve().parent / "assets"

# 【学生重点1】读取图片是拿到素材，blit才是把素材画出来。
sea = pygame.image.load(str(ASSETS / "sea.png"))
sea = pygame.transform.scale(sea, (800, 600))  # 海面铺满窗口，下一步再解释缩放。
ship = pygame.image.load(str(ASSETS / "ship.png"))

# 【学生重点2】变量保存位置；x向右增加，y向下增加。
# = 是赋值；(x,y)会指定图片左上角，而不是中心。
x = 200
y = 180
background = (15, 60, 85)  # RGB底色：红、绿、蓝，每个分量为0—255。

running = True
while running:
    # 【老师提供】每圈处理操作；关闭窗口时结束循环。
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 【学生重点3】先画海面，再画舰船；后画的会盖住先画的。
    screen.fill(background)
    screen.blit(sea, (0, 0))
    screen.blit(ship, (x, y))
    # 挑战：交换上面两行，船为什么消失？
    # 海面盖住底色时，修改background看不到效果；暂时注释画海语句再试。

    # 【老师提供】刷新、限速。下面--smoke只供老师自动检查。
    pygame.display.flip()
    clock.tick(60)
    if "--smoke" in sys.argv:
        running = False

pygame.quit()
