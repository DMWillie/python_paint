"""
    作者:北辰
    功能:五角星的绘制
    版本:1.0
    日期:09/06/2018
"""

import turtle #引入绘图库

def main():
    """
    主函数
    """
    # # turtle库的一些基本操作(测试)
    # turtle.forward(300)   #向前移动300个像素
    # turtle.backward(300)  #向后移动300个像素
    # turtle.right(60) #向右旋转60度(顺时针)
    # turtle.left(60)  #向左旋转60度(逆时针)
    # turtle.exitonclick() #点击关闭图形窗口

    # 五角星的绘制
    count = 1 #计数器
    while count <= 5:
        turtle.forward(100)
        turtle.right(144)
        count+=1
    turtle.exitonclick()

if __name__=='__main__':
    main()