

import turtle
import time

turtle1 = turtle.Turtle()
# 画心形圆弧
def hart_arc():
    for i in range(200):
        turtle1.right(1)
        turtle1.forward(2)


def move_pen_position(x, y):
    turtle1.hideturtle()  # 隐藏画笔（先）
    turtle1.up()  # 提笔
    turtle1.goto(x, y)  # 移动画笔到指定起始坐标（窗口中心为0,0）
    turtle1.down()  # 下笔
    turtle1.showturtle()  # 显示画笔


love = input("请输入表白话语，默认为‘I Love You’：")
signature = input("请签署你的大名，不填写默认不显示：")

if love == '':
    love = 'I Love You'

# 初始化
turtle.Screen().setup(width=800, height=500)  # 窗口（画布）大小
turtle1.getscreen().bgcolor('light skyblue') # 画布背景颜色
turtle1.color('red', 'pink')  # 画笔颜色
turtle1.pensize(3)  # 画笔粗细
turtle1.speed(10)  # 描绘速度
# 初始化画笔起始坐标
move_pen_position(x=0, y=-180)  # 移动画笔位置
turtle1.left(140)  # 向左旋转140度

turtle1.begin_fill()  # 标记背景填充位置

# 画心形直线（ 左下方 ）
turtle1.forward(224)  # 向前移动画笔，长度为224
# 画爱心圆弧
hart_arc()  # 左侧圆弧
turtle1.left(120)  # 调整画笔角度
hart_arc()  # 右侧圆弧
# 画心形直线（ 右下方 ）
turtle1.forward(224)

turtle1.end_fill()  # 标记背景填充结束位置

# 在心形中写上表白话语
move_pen_position(0, 0)  # 表白语位置
turtle1.hideturtle()  # 隐藏画笔
turtle1.color('#CD5C5C', 'pink')  # 字体颜色
# font:设定字体、尺寸（电脑下存在的字体都可设置）  align:中心对齐
turtle1.write(love, font=('Arial', 30, 'bold'), align="center")

# 签写署名
if signature != '':
    turtle1.color('red', 'pink')
    time.sleep(2)
    move_pen_position(180, -180)
    turtle1.hideturtle()  # 隐藏画笔
    turtle1.write(signature, font=('Arial', 20), align="center")

# 点击窗口关闭程序
window = turtle.Screen()
window.exitonclick()