#导入matplotlib.pyplot，并取别名plt
import matplotlib.pyplot as plt

#确定输入值
input_values = [1,2,3,4,5]
#创建列表squares，存储平方数
squares = [1,4,9,16,25]

#将列表传递给plot
plt.plot(input_values,squares,linewidth=3)	#linewidth用来决定绘制的线条的粗度
plt.title("Square Numbers",fontsize=18)	#添加图表标题，设置字体
plt.xlabel("Value",fontsize=14)	#添加X轴标题，设置字体
plt.ylabel("Square of Value",fontsize=14)	#添加Y轴标题，设置字体
plt.tick_params(axis='both',labelsize=14)	#设置刻度标记的大小

#用show（）打开matplotlib查看器，并现实绘制的图形
plt.show()
