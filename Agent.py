import threading
import time
from Grille import *
from Message import *

class Agent(threading.Thread):
	"""docstring for Agent"""

	agent_id = 0

	def __init__(self, row, col, f_row, f_col, grid, mail_box):
		super(Agent, self).__init__()
		self.row = row
		self.col = col
		self.__f_row = f_row
		self.__f_col = f_col
		self.__grid = grid
		Agent.agent_id += 1
		self.id = Agent.agent_id
		grid.registerNewAgent(self)
		self.mail_box = mail_box

	def __move__( self, down, right):
		assert down <= 0 and down >= -1 and right <= 1 and right >= -1
		self.__grid.move_agent(this, down, right)


	def isTerminal(self):
		return (self.col == self.__f_col and self.row == self.__f_row)

	def gameIsOver(self):
		return self.__grid.isTerminal()

	def run(self):
		while not self.gameIsOver():
			time.sleep(2)
			print("Hello from agent :"+str(self.id))
			if len(self.mail_box[self.id]) > 0:
				mail = self.mail_box[self.id].pop(0)
				print("agent "+str(self.id)+" :> mail received from "+str(mail.sender))
				if (mail.dest == self.id) and (mail.content[0]==self.row and mail.content[1]==self.col):
					if self.__grid.move_agent(self, 1, 0) != 0:
						if self.__grid.move_agent(self, -1, 0) != 0:
							if self.__grid.move_agent(self, 0, 1) != 0:
								self.__grid.move_response(self, 0, -1)
			else:
				down = (((self.__f_row - self.row) > 0)*2 - 1)*(self.row != self.__f_row)
				right = (((((self.__f_row - self.row) > 0)*2 - 1)*(self.row != self.__f_row))==0)*(((self.__f_col - self.col) > 0)*2 - 1)*(self.col != self.__f_col)
				move_response = self.__grid.move_agent(self, down, right)
				if move_response > 0:
					self.mail_box[move_response].append(Message(self.id, move_response, [self.row + down, self.col + right]))
					print("agent "+str(self.id)+" :> to agent "+str(move_response)+" : move from "+str(self.row + down)+","+str(self.col + right))
			pass