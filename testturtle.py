"""
    作者:北辰
    功能:对turtle库一些常用函数和功能的测试
    日期:09/06/2018
"""

import turtle

#turtle库的一些基本操作(测试)
turtle.forward(100)   #向前移动100个像素
turtle.backward(100)  #向后移动100个像素
turtle.right(60) #向右旋转60度(顺时针)
turtle.left(60)  #向左旋转60度(逆时针)
turtle.exitonclick() #点击关闭图形窗口

#turtle库的补充功能
turtle.penup()  #抬起画笔,之后移动画笔不绘制形状
turtle.pendown() #落下画笔,之后移动画笔绘制形状
turtle.pensize()  #设置画笔宽度
turtle.pencolor() #设置画笔颜色

# turtle库的官方文档: https://docs.python.org/3.0/library/turtle.html