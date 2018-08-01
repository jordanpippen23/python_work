import matplotlib.pyplot as plt

#运用scatter（）绘制一系列点，给定坐标列表
x_value = [1,2,3,4,5]
y_value = [1,4,9,16,25]

plt.scatter(x_value,y_value,edgecolor='red',s=100)	#edgecolor删除点轮廓

plt.title("Square Nummer",fontsize=18)
plt.xlabel('Square of Value',fontsize=14)
plt.ylabel('Value',fontsize=14)

#设置刻度标记的大小
plt.tick_params("axis = 'both',which = 'major',fontsize=14")

plt.show()
