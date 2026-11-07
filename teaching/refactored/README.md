# 教学重构完成版

Python 3.13 + pygame 2.6.1。不依赖Tkinter。进入本目录运行`python main.py`，默认人机。

联机在独立终端运行`python server.py`，再分别运行`python main.py --connect 127.0.0.1 --name Alice`与`python main.py --connect 127.0.0.1 --name Bob`。

点击左棋盘放置；1/2/3选船，R旋转；随机布阵、清空、准备按钮在棋盘下方。准备后锁定，自己的回合点击右棋盘攻击。双方确认后重开，Esc退出。

完整规则、素材署名、局域网步骤与测试限制见`../README.md`。
