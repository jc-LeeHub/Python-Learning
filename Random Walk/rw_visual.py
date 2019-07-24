import matplotlib.pyplot as plt

from random_walk import RandomWalk

#多次获取散点图
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    #颜色随步数逐渐加深
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=1)
    
    #绘制起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none',s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running=='n':
        break
    
