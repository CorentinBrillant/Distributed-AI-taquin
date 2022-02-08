import threading
from Agent import Agent

class Grille(object):

	"""docstring for Grille"""
	def __init__(self, size):
		super(Grille, self).__init__()
		self.__size = size
		self.__grid = [[0]*size]*size
		self.__agents = []
		self.grid_lock = threading.Lock()

	def move_agent(agent, down, right):
		assert down <= 0 and down >= -1 and right <= 1 and right >= -1
		self.grid_lock.acquire()
		if self.grid[self.__agents[agent.id-1].row + down][self.__agents[agent.id-1].col + right] == 0:
			self.__agents[agent.id-1].row += down
			self.__agents[agent.id-1].col += right
		self.grid_lock.release()

	def __show__(self):
		for x in range(self.__size):
			print("| ", end="")
			for y in range(self.__size):
				print(str(self.__grid[x][y])+" ",end="")
			print("|")