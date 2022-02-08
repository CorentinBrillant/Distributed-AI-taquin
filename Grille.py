class Grille(object):

	"""docstring for Grille"""
	def __init__(self, size):
		super(Grille, self).__init__()
		self.__size = size
		self.__grid = [[0]*size]*size

	def __show__(self):
		for x in range(self.__size):
			print("| ", end="")
			for y in range(self.__size):
				print(str(self.__grid[x][y])+" ",end="")
			print("|")