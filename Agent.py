import threading

class Agent(threading.Thread):
	"""docstring for Agent"""
	def __init__(self, row, col, f_row, f_col):
		super(Agent, self).__init__()
		self.__row = row
		self.__col = col
		self.__f_row = f_row
		self.__f_col = f_col

	def __move__( down, right):
		assert down <= 0 and down >= -1 and right <= 1 and right >= -1
		self.__row += down
		self.__col += right

	def __isTerminal__(self):
		return (self.__col == self.__f_col and self.__row == self.__f_row)

	def run(self):
		while not self.__isTerminal__():
			pass