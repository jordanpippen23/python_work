import matplotlib.pyplot as plt

from random_walk import RandomWalk

#创建一个Randomalk实例，并将其包含的点描绘出来
rw = RandomWalk()	#将Randomalk实例保存至rw
rw.fill_walk()	#调用fill_walk() 
plt.scatter(rw.x_values,rw.y_values,s=15)	#将随机漫步包含的x与y值传递

plt.show()
