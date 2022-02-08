import threading
from Grille import Grille

class Agent(threading.Thread):
	"""docstring for Agent"""

	agent_id = 0

	def __init__(self, row, col, f_row, f_col, grid):
		super(Agent, self).__init__()
		self.row = row
		self.col = col
		self.__f_row = f_row
		self.__f_col = f_col
		self.__grid = grid
		Agent.agent_id += 1
		self.id = Agent.agent_id

	def __move__( self, down, right):
		assert down <= 0 and down >= -1 and right <= 1 and right >= -1
		self.__grid.move_agent(this, down, right)

	def __isTerminal__(self):
		return (self.__col == self.__f_col and self.__row == self.__f_row)

	def run(self):
		while not self.__isTerminal__():
			pass