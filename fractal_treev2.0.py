"""
    作者:北辰
    功能:利用递归函数绘制分形树
    版本:2.0
    日期:11/06/2018
    2.0新增功能:使分形树树枝末梢颜色为绿色
"""

import turtle

def draw_branch(branch_length):
    """
    绘制分形树
    """
    if branch_length > 5:
        # 绘制右侧树枝
        turtle.pencolor('brown')  # 设置画笔绘制树根的颜色为棕色
        turtle.pensize(3) # 设置画笔绘制树根的粗细为3
        print('画笔 棕色')
        turtle.forward(branch_length)
        print('向前 ',branch_length)
        turtle.right(20) #向右转20°
        print('右转 20°')
        draw_branch(branch_length-15)
        # 递归回调时将画笔颜色设为棕色
        turtle.pencolor('brown')
        print('画笔 棕色')

        # 绘制左侧树枝
        turtle.left(40)
        print('左转 40°')
        draw_branch(branch_length-15)
        # 递归回调时将画笔颜色设为棕色
        turtle.pencolor('brown')
        print('画笔 棕色')

        # 返回之前的树枝
        turtle.right(20)
        print('右转 20°')
        turtle.backward(branch_length)
        print('向后 ',branch_length)
        # 这里是判断位于最后一层的树枝
        if branch_length < 20:
            turtle.pencolor('green')
            turtle.pensize(2)
            print('画笔 绿色')
            turtle.forward(branch_length)
            print('向前 ', branch_length)
            turtle.right(20)
            print('右转 20°')
            draw_branch(branch_length - 15)
            turtle.left(40)
            print('左转 40°')
            draw_branch(branch_length - 15)
            turtle.right(20)
            print('右转 20°')
            turtle.backward(branch_length)
            print('向后 ', branch_length)


def main():
    """
    主函数
    """
    turtle.left(90)  #使画笔朝上
    # 使画笔初始位置向下移
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    # 调用递归函数绘制分形树
    draw_branch(100)
    turtle.exitonclick()

if __name__=='__main__':
    main()