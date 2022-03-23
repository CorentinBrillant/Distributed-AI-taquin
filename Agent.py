import threading
import time
from Grille import *
from Message import *
from Astar import *
import random

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
		self.priority = -1
		self.compute_priority()

	def compute_priority(self):
		for k in range(self.__grid.__size__):
			if (self.__f_col == k or self.__f_col == self.__grid.__size__-1-k or self.__f_row == k or self.__f_row == self.__grid.__size__-1-k) and self.priority==-1:
				self.priority = (self.__grid.__size__-k)*10 + 0.01*self.id

	def __move__( self, down, right):
		assert down <= 0 and down >= -1 and right <= 1 and right >= -1
		self.__grid.move_agent(this, down, right)


	def isTerminal(self):
		return (self.col == self.__f_col and self.row == self.__f_row)

	def gameIsOver(self):
		return self.__grid.isTerminal()

	def cleanMail(self):
		idToBen = []
		for i in range(len(self.mail_box[self.id])):
			if (self.mail_box[self.id][i].content[0] != self.row or self.mail_box[self.id][i].content[1] != self.col) or (self.isTerminal() and self.priority > self.mail_box[self.id][i].priority ):
					idToBen.append(i)
		idToBen.reverse()
		for i in idToBen:
			self.mail_box[self.id].pop(i)

	def getMostUrgentMail(self):
		self.cleanMail()
		if len(self.mail_box[self.id])>0:
			higher_priority = self.mail_box[self.id][0].priority
			mail_rank = 0
			for i in range(1,len(self.mail_box[self.id])):
				if self.mail_box[self.id][i].priority > higher_priority:
					higher_priority = self.mail_box[self.id][i].priority
					mail_rank = i
			return mail_rank
		else:
			return -1

	def move_and_send(self, my_best_way):
		move_response = self.__grid.move_agent(self, my_best_way[0], my_best_way[1])
		if move_response != 0:
			self.mail_box[move_response].append(Message(self.id, move_response, [self.row + my_best_way[0], self.col + my_best_way[1]], self.priority))
			#print("agent "+str(self.id)+" :> to agent "+str(move_response)+" : move from "+str(self.row + my_best_way[0])+","+str(self.col + my_best_way[1]))
		return move_response

	def run(self):
		while not self.gameIsOver():
			time.sleep(2)
			#print("Hello from agent :"+str(self.id))
			mail_rank = self.getMostUrgentMail()
			my_best_way =[]
			if not self.isTerminal():
				adapted_grid = [[0 if (i==0) or (self.__grid.__agents__[i-1].priority <= self.priority) else 1 for i in gridy ] for gridy in self.__grid.__grid__]
				my_way = star([self.row, self.col],[self.__f_row, self.__f_col], adapted_grid)[2]
				if len(my_way)>0:
					my_best_way = my_way[0]
			#if we got an mail
			if mail_rank > -1:
				mail = self.mail_box[self.id][mail_rank]
				if mail.priority >= self.priority:
					#try to move
					ans = 1
					#print("agent "+str(self.id)+" :> mail received from "+str(mail.sender))
					if (mail.dest == self.id) and (mail.content[0]==self.row and mail.content[1]==self.col):
						ans = self.__grid.move_agent(self, 1, 0)
						if ans != 0:
							ans = self.__grid.move_agent(self, -1, 0)
							if ans != 0:
								ans = self.__grid.move_agent(self, 0, 1)
								if ans != 0:
									ans = self.__grid.move_agent(self, 0, -1)
									if  ans != 0:
										if not self.isTerminal()  and len(my_best_way)>0:
											ans = self.__grid.move_agent(self, my_best_way[0], my_best_way[1])
											self.mail_box[ans].append(Message(self.id, ans, [self.row + my_best_way[0], self.col + my_best_way[1]], mail.priority))
											#print("agent "+str(self.id)+" :> to agent "+str(ans)+" : move from "+str(self.row + my_best_way[0])+","+str(self.col + my_best_way[1]))
										else:
											down = 0
											right = 0
											if random.uniform(0, 1) < 0.5:
												down = (self.row >= self.__grid.__size__-1)*(-1)+(self.row < self.__grid.__size__-1)
											else:
												right = (self.col >= self.__grid.__size__-1)*(-1)+(self.col < self.__grid.__size__-1)
											ans = self.__grid.move_agent(self, down, right)
											self.mail_box[ans].append(Message(self.id, ans, [self.row + down, self.col + right], mail.priority))
											#print("agent "+str(self.id)+" :> to agent "+str(ans)+" : move from "+str(self.row + down)+","+str(self.col + right))
										
					#if we can move, mail goes to the ben
					if ans == 0:
						self.mail_box[self.id].pop(mail_rank)
				elif not self.isTerminal() and len(my_best_way)>0:
					self.move_and_send(my_best_way)
			#else we go on our own way
			elif not self.isTerminal() and len(my_best_way)>0:
				self.move_and_send(my_best_way)
		pass