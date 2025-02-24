# PongGame项目文档

## 1. 项目概述
Pong 是一款经典的双人弹球游戏，玩家通过控制挡板击打球，防止球从自己一侧的屏幕边缘漏出。本项目使用 Python 的 `turtle` 模块实现。

## 2. 功能描述
- **双人对战模式**：玩家 A 使用键盘的 `W` 和 `S` 键控制左侧挡板，玩家 B 使用键盘的上下箭头键控制右侧挡板。
- **得分系统**：当球从玩家一侧漏出时，对方得分。分数实时显示在屏幕顶部。
- **边界检测**：球和挡板在屏幕边界处反弹，挡板不会移出屏幕范围。
- **简单的图形界面**：使用 `turtle` 模块绘制游戏界面。

## 3. 技术栈
- **编程语言**：Python
- **图形库**：`turtle`（Python 内置库）
- **其他库**：无

## 4. 项目结构
```
PongGame/
├── pong_game.py          # 主程序代码
├── README.md             # 项目文档
```

## 5. 安装与运行
### 5.1 环境准备
确保你的系统已安装 Python 3.6 或更高版本。你可以从 [Python 官方网站](https://www.python.org/downloads/) 下载并安装。

### 5.2 获取代码
1. 克隆或下载本项目代码到本地。
2. 确保项目目录中包含 `pong_game.py` 文件。

### 5.3 运行游戏
在终端或命令提示符中，运行以下命令启动游戏：
```bash
python pong_game.py
```

### 5.4 游戏操作
- **玩家 A（左侧挡板）**：
  - `W` 键：向上移动
  - `S` 键：向下移动
- **玩家 B（右侧挡板）**：
  - 上箭头键：向上移动
  - 下箭头键：向下移动

## 6. 代码说明
### 6.1 主程序 (`pong_game.py`)
以下是代码的主要模块和功能：

#### 6.1.1 屏幕设置
```python
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # 关闭自动刷新，手动更新屏幕
```
- 设置游戏窗口的标题、背景颜色、大小，并关闭自动刷新以优化性能。

#### 6.1.2 球的创建与移动
```python
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()  # 移动时不画线
ball.goto(0, 0)
ball.dx = 0.2  # 球的水平速度
ball.dy = 0.2  # 球的垂直速度
```
- 创建球对象，设置其形状、颜色和初始位置。
- 定义球的移动速度（`dx` 和 `dy`）。

#### 6.1.3 挡板创建与控制
```python
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # 5x1 的矩形
paddle_a.penup()
paddle_a.goto(-350, 0)
```
- 创建挡板对象，设置其形状、颜色、大小和初始位置。
- 定义挡板的上下移动逻辑，防止挡板移出屏幕范围。

#### 6.1.4 边界检测与碰撞处理
```python
if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1  # 反向移动
```
- 检测球是否触碰屏幕边界，并反转其移动方向。
- 检测球是否与挡板碰撞，并反转球的水平移动方向。

#### 6.1.5 得分系统
```python
score_a = 0
score_b = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
```
- 初始化玩家分数，并在屏幕顶部显示分数。

### 6.2 游戏主循环
```python
while True:
    screen.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # 其他逻辑...
```
- 游戏主循环负责更新屏幕、移动球、检测碰撞和更新分数。

## 7. 测试
### 7.1 测试环境
- 操作系统：Windows
- Python 版本：3.12

### 7.2 测试用例
1. **挡板控制测试**：
   - 玩家 A 和 B 分别使用键盘操作挡板，确保挡板移动正常且不会移出屏幕范围。
2. **球的移动测试**：
   - 球应正常移动，并在触碰屏幕边界时反弹。
3. **碰撞检测测试**：
   - 球与挡板碰撞时，应正确反弹。
4. **得分测试**：
   - 当球从一侧漏出时，对方得分，分数应正确更新。

## 10. 联系方式
- **作者**：[毕涛]
- **邮箱**：[1459476432]
- **GitHub**：[https://github.com/Battou1]
