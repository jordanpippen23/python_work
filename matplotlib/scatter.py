import matplotlib.pyplot as plt

#运用scatter（）绘制单个点，给定坐标
plt.scatter(2,4,s=200)

plt.title("Square Nummer",fontsize=18)
plt.xlabel('Square of Value',fontsize=14)
plt.ylabel('Value',fontsize=14)

#设置刻度标记的大小
plt.tick_params("axis = 'both',which = 'major',fontsize=14")

plt.show()
