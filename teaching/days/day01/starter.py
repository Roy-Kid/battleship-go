"""第一课：让舰船出现在海上。
运行：python starter.py
修改后先保存，再关闭旧窗口并重新运行。
--smoke 是老师检查启动用的参数，学生暂时跳过。
"""
# 一、导入工具。import 让程序可以使用对应模块里的功能。
from pathlib import Path  # Python 自带：处理文件路径。
import sys                # Python 自带：这里仅用于老师的启动检查。
import pygame             # 另行安装的游戏库：窗口、图像、键盘和鼠标等。

# 二、准备窗口和素材。这一部分由老师提供，今天先认识它的作用。
# __file__ 是当前代码文件的路径；parent 是它所在的文件夹。
# 路径中的 / 表示拼接文件路径，不是在做数字除法。
ASSETS = Path(__file__).resolve().parent / "assets"

pygame.init()  # 初始化 Pygame；先准备，再使用它的功能。

# (800, 600) 是一个元组：依次表示窗口的宽、高，单位是像素。
# screen 保存返回的窗口绘图表面，后面向它绘制图像。
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Battleship Lab")  # 引号里是字符串，控制窗口标题。
clock = pygame.time.Clock()  # 创建时钟，用来限制循环速度。

# load 读取图片，返回图像对象；此时图片还没有显示在窗口里。
# str 把路径对象转换成 Pygame 可以读取的字符串。
sea = pygame.image.load(str(ASSETS / "sea.png"))
sea = pygame.transform.scale(sea, (800, 600))  # 缩放成窗口大小。
ship = pygame.image.load(str(ASSETS / "ship.png"))
ship = pygame.transform.scale(ship, (48, 144))  # 舰船宽 48、高 144 像素。

# 三、用变量保存位置和颜色。这是今天重点修改的部分。
# = 是赋值：把右边的值保存到左边的名字中。
# x、y 使用整数，不要写成 "200" 这样的字符串。
# 原点在窗口左上角：x 越大越靠右，y 越大越靠下。
x = 100
y = 100

# RGB 颜色也是一个元组：依次是红、绿、蓝，各分量取 0—255。
# 海面铺满窗口时会盖住底色；做颜色实验时先注释掉画海面的那一行。
background = (15, 60, 85)

# 四、游戏循环：处理操作 → 绘制画面 → 刷新 → 控制速度。
# True / False 是布尔值，表示真 / 假；首字母必须大写。
running = True
while running:  # 只要 running 为 True，就重复执行下面缩进的代码。
    # 取出等待处理的事件；for 会逐个处理本次取到的事件。
    # 没有事件时，这个 for 不执行，但后面的绘制仍会继续。
    for event in pygame.event.get():
        # if 表示条件判断；== 比较是否相等，与赋值用的 = 不同。
        # pygame.QUIT 是点击窗口关闭按钮产生的事件类型。
        if event.type == pygame.QUIT:
            running = False  # 当前这一圈会继续做完，下一圈不再开始。

    # 这里与 for 对齐：每一圈都要绘制，不仅仅在有事件时绘制。
    screen.fill(background)  # 先用底色清空绘图表面，避免留下上一帧的痕迹。
    screen.blit(sea, (0, 0))  # 再把海面画在窗口左上角。
    # 学生任务：用 screen.blit 把 ship 画在 (x, y)。
    # 提示：参考上一行画海面的写法；与上一行保持相同缩进。
    # 在这里补上绘制舰船的语句，先不要查看 main.py。

    # 将本轮绘制的结果显示出来；先画完，再刷新。
    pygame.display.flip()
    clock.tick(60)  # 限制循环速度：最多每秒约 60 圈，并非保证达到 60 圈。

    # 教师检查用：收到 --smoke 参数时只运行一圈，平时不影响游戏。
    if "--smoke" in sys.argv:
        running = False

# 五、这一行没有缩进，退出 while 循环之后才执行。
pygame.quit()  # 释放 Pygame 的窗口等资源。
