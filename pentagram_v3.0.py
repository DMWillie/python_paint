"""
    作者:北辰
    功能:五角星的绘制
    版本:3.0
    日期:10/06/2018
    2.0新增功能:加入循环操作绘制重复不同大小的图形
    3.0新增功能:使用迭代函数绘制重复不同大小的图形
"""

import turtle #引入绘图库

def draw_recursive_pentagram(size):
    """
    迭代绘制五角星
    """
    count = 1  # 计数器
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1

    #五角星绘制完成,更新参数
    size+=20
    if size <= 150:
        draw_recursive_pentagram(size)



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
    draw_recursive_pentagram(size) #利用递归函数
    # while size <= 150: (利用循环)
    #     #调用函数
    #     draw_pentagram(size)
    #     size+=20
    turtle.exitonclick()

if __name__=='__main__':
    main()