import threading
from Agent import *

class Grille:

	"""docstring for Grille"""
	def __init__(self, size):
		super(Grille, self).__init__()
		self.__size__ = size
		self.__grid__ = [[0 for i in range(size)] for j in range(size)]
		self.grid_lock = threading.Lock()
		self.__agents__ = []

	def move_agent(self, agent, down, right):
		retour = 0
		assert down <= 1 and down >= -1 and right <= 1 and right >= -1
		self.grid_lock.acquire()
		if self.__grid__[agent.row + down][agent.col + right] == 0:
			self.__grid__[agent.row][agent.col] = 0
			agent.row += down
			agent.col += right
			self.__grid__[agent.row][agent.col] = agent.id	
			print("Agent "+str(agent.id)+" moved")
			self.__show__()
		else:
			retour = self.__grid__[agent.row + down][agent.col + right]
		self.grid_lock.release()
		return retour

	def isTerminal(self):
		over = True
		for a in self.__agents__:
			over &= a.isTerminal()
		return over

	def registerNewAgent(self,agent):
		if self.__grid__[agent.row][agent.col] == 0 :
			if agent not in self.__agents__:
				self.__agents__.append(agent)
				self.__grid__[agent.row][agent.col] = agent.id
			else:
				print("Agent already registered")
		else:
			print("Can't add Agent, this place is already occuped")

	def __show__(self):
		for x in range(self.__size__):
			print("| ", end="")
			for y in range(self.__size__):
				print(str(self.__grid__[x][y])+" ",end="")
			print("|")
		print("")