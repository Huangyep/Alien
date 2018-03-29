class Settings():
	"""存储游戏的所有设置的类"""

	def __init__(self):
		"""初始化游戏静态设置"""
		#屏幕设置
		self.screen_width = 1200
		self.screen_height = 760
		self.bg_color = (230,230,230)
		#飞船设置
		self.ship_limit = 3
		#子弹设置
		self.bullet_width = 10
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 3
		#外星人设置	
		self.fleet_drop_speed = 10	

		#以什么速度加快游戏节奏
		self.speedup_scale = 1.1
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""初始随游戏进行而变化的设置"""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		#外星人移动方向。fleet_direction为1表示向右移，-1表示向左移
		self.fleet_direction = 1
		self.alien_points = 50

	def increase_speed(self):
		"""提高速度设置"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale