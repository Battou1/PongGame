import turtle

# 设置屏幕
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # 关闭自动刷新，手动更新屏幕

# 创建球
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()  # 移动时不画线
ball.goto(0, 0)
ball.dx = 0.2  # 球的水平速度
ball.dy = 0.2  # 球的垂直速度

# 创建挡板
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # 5x1 的矩形
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# 分数
score_a = 0
score_b = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# 挡板移动函数
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:  # 上边界检测
        y += 60
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:  # 下边界检测
        y -= 60
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:  # 上边界检测
        y += 60
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:  # 下边界检测
        y -= 60
    paddle_b.sety(y)

# 绑定键盘事件
screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")

# 游戏主循环
while True:
    screen.update()

    # 移动球
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # 边界检测
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # 反向移动

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score.clear()
        score.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score.clear()
        score.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # 挡板和球碰撞检测
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1