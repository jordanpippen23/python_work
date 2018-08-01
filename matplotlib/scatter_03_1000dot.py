import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none',s=30)
#colormap颜色映射，起始颜色渐变到终结色
#还可以用参数c的RGB颜色模式: c=(0,0,0.8)  0~1之间的数值，越靠近0越浓，反之则淡

plt.title("Square Nummer",fontsize=18)
plt.xlabel('Square of Value',fontsize=14)
plt.ylabel('Value',fontsize=14)

#设置刻度标记的大小
plt.tick_params("axis = 'both',which = 'major',fontsize=14")

plt.axis = ([0,1100,0,1100000])

#自动保存图表，保存地址为此文件所在目录
plt.savefig("scatter_03_1000dot.png", bbox_inches = "tight")

plt.show()
