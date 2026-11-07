# 第9天：完成双人联机

本课2小时。知识：请求、服务器裁决、快照、阶段同步。

## 运行

在已激活的Python 3.13环境中进入本目录：

```bash
python main.py  # 先试玩人机
# 联机：以下每条在独立终端运行
python server.py
python main.py --connect 127.0.0.1 --name Alice
python main.py --connect 127.0.0.1 --name Bob
```

`starter.py` 是课堂起点，`main.py` 是参考完成版。starter.py是第7天的人机版本；main.py是老师提供的联网集成参考。通过对照和演示完成过渡，不把底层联网当作独立作业。

## 学生任务

观察ready/attack请求怎样改变服务器比赛；比较发起操作与得到结果的区别。

## 老师提供

main.py/match.py/network.py/server.py是集成样板；学生主要阅读submit调用和状态显示。不要要求从第7天手写全部网络。

## 挑战与验收

完成一次有效双人对局；重复点击不多扣回合；双方确认后重开。

先说预测，运行验证，再解释原因。每次保存一个可运行版本。本目录包含独立素材，可单独复制；无需访问相邻天的目录。

素材：Water+ / ninjikin（海面）；Sea Warfare set（舰船）。具体来源见teaching/README.md。
