# 第8天：两台电脑交换消息

本课2小时。知识：字典、消息、客户端/服务器、JSON概念。

## 运行

在已激活的Python 3.13环境中进入本目录：

```bash
python server.py
# 另开两个终端，分别运行：
python main.py --name Alice
python main.py --name Bob
```

`starter.py` 是课堂起点，`main.py` 是参考完成版。本课新开一个终端消息实验；starter.py已经包含收发支架，学生修改消息内容。

## 学生任务

先本机两个终端互发消息；修改name/text字段；再用局域网IP连接。

## 老师提供

server.py与network.py由老师提供；线程、TCP分帧和锁不要求学生独立实现。

## 挑战与验收

交换昵称，试试中文和星号；把消息内容改成坐标文本。

先说预测，运行验证，再解释原因。每次保存一个可运行版本。本目录包含独立素材，可单独复制；无需访问相邻天的目录。

素材：Water+ / ninjikin（海面）；Sea Warfare set（舰船）。具体来源见teaching/README.md。
