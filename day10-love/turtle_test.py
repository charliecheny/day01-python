# ! usr/bin/eny python

import turtle
import datetime


# 生日快乐
# Python学习群548377875
def love():
    def func(x, y):
        main()

    turtle.Screen().title('帅逼专用程序')
    lv = turtle.Turtle()
    lv.hideturtle()
    lv.getscreen().bgcolor('light skyblue') # 画布背景颜色
    lv.color('yellow', 'red')  # 画笔颜色
    lv.pensize(3) # 画笔粗细
    lv.speed(3)  # 画笔速度
    lv.up()
    lv.goto(0, -150)
    # 开始画爱心
    lv.down()
    lv.begin_fill()
    lv.goto(0, -150)
    lv.goto(-175.12, -8.59)
    lv.left(140)
    pos = []
    for i in range(19):
        lv.right(10)
        lv.forward(20)
        pos.append((-lv.pos()[0], lv.pos()[1]))
    for item in pos[::-1]:
        lv.goto(item)
    lv.goto(175.12, -8.59)
    lv.goto(0, -150)
    lv.left(50)
    lv.end_fill()
    # 写字
    lv.up()
    lv.goto(0, 80)
    lv.down()
    lv.write("张兴帅逼", font=(u"方正舒体", 36, "normal"), align="center")
    # lv.up()
    # lv.goto(0, 10)
    # lv.down()
    # lv.write("你个贱人又瘦了！", font=(u"方正舒体", 30, "normal"), align="center")
    lv.up()
    lv.goto(0, 0)
    lv.down()
    lv.write("生日快乐！", font=(u"方正舒体", 48, "normal"), align="center")
    lv.up()
    lv.goto(100, -210)
    lv.down()
    lv.write("点我点我快点我！", font=(u"华文琥珀", 26, "bold"), align="right")
    lv.up()
    lv.goto(160, -190)
    lv.resizemode('user')
    lv.shapesize(4, 4, 10)  # 调整小乌龟大小，以便覆盖“点我”文字
    lv.color('red', 'red')
    lv.onclick(func)
    # lv.showturtle()
    window = turtle.Screen()
    window.exitonclick()


def main():
    pass


if __name__ == '__main__':
    if datetime.date.today() == datetime.date(2019, 4, 17):  # YYYY年,MM月,DD日
        love()
    else:
        main()