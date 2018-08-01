from random import choice

class RandomWalk():
	"""一个生成随机漫步的类"""
	
	def __init__(self,num_points=5000):
		"""初始化随机漫步属性"""
		self.num_points = num_points
		
		#所有随机漫步都始于（0，0）点
		self.x_values = [0]
		self.y_values = [0]
	
	def fill_walk(self):
		"""计算随机漫步包含的所有点"""
		
		#不断漫步，直到列表达到指定长度
		while len(self.x_values) < self.num_points:
			
			x_direction = choice([1,-1])	#决定前进方向
			x_distance = choice([0,1,2,3,4])	#决定沿这个方向前进的距离
			x_step = x_direction * x_distance
			
			y_direction = choice([1,-1])
			y_distance = choice([0,1,2,3,4])
			y_step = y_direction * y_distance
			
			if x_distance == 0 and y_distance == 0:
				continue	#拒绝原地踏步
			
			#计算下一个点的x和y值
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step
			self.x_values.append(next_x)
			self.y_values.append(next_y)
			
			
