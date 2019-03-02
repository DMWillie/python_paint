"""
    作者:北辰
    功能:五角星的绘制
    版本:2.0
    日期:09/06/2018
    新增功能:加入循环操作绘制重复不同大小的图形
"""

import turtle #引入绘图库

def draw_pentagram(size):
    """
    五角星的绘制
    """
    count = 1  # 计数器
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1


def main():
    """
    主函数
    """
    #对画笔进行一些初始化操作
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    size = 50

    while size <= 150:
        #调用函数
        draw_pentagram(size)
        size+=20
    turtle.exitonclick()

if __name__=='__main__':
    main()