from Grille import *
from Agent import *
from Message import *

import random
import time

def randomAgentsGenerator(grid, nb_agents):

	random_start_positions = []
	random_end_positions = []
	agents = []
	c = 1
	obj = [[0 for i in range(grid.__size__)] for j in range(grid.__size__)]
	while len(random_start_positions)<nb_agents:
		[x,y] = [random.randint(0,grid.__size__-1),random.randint(0,grid.__size__-1)]
		if [x,y] not in random_start_positions:
			random_start_positions.append([x,y])
	while len(random_end_positions)<nb_agents:
		[x,y] = [random.randint(0,grid.__size__-1),random.randint(0,grid.__size__-1)]
		if [x,y] not in random_end_positions:
			random_end_positions.append([x,y])
			obj[x][y] = c
			c += 1
	mail_box = [[] for i in range(nb_agents+1)]
	for i in range(nb_agents):
		agents.append(Agent(random_start_positions[i][0],random_start_positions[i][1],random_end_positions[i][0],random_end_positions[i][1],grid,mail_box))
	print("Agents generated")
	return mail_box, agents, obj

if __name__ == '__main__':
	n = 5
	grid = Grille(n)

	nb_agents = 24

	mail_box, agents, obj = randomAgentsGenerator(grid, nb_agents)

	grid.__show__()

	print("Objective : \n")

	for x in range(len(obj)):
		print("|\t", end="")
		for y in range(len(obj)):
			print(str(obj[x][y])+"\t",end="")
		print("|")
	print("")

	time.sleep(5)
	for i in range(len(agents)):
		agents[i].start()

	"""
	mail_box = [[],[],[],[],[],[],[],[]]
	# agent_1 = Agent(1,1,4,4,grid, mail_box)
	# agent_2 = Agent(0,0,3,4,grid, mail_box)
	agent_1 = Agent(4,1,1,2,grid, mail_box)
	agent_2 = Agent(3,1,2,3,grid, mail_box)
	agent_3 = Agent(2,0,0,2,grid, mail_box)
	agent_4 = Agent(1,2,4,0,grid, mail_box)
	agent_5 = Agent(3,3,0,0,grid, mail_box)
	agent_6 = Agent(2,2,2,4,grid, mail_box)
	agent_7 = Agent(1,1,4,4,grid, mail_box)
	agent_1.start()
	agent_2.start()
	agent_3.start()
	agent_4.start()
	agent_5.start()
	agent_6.start()
	agent_7.start()
	"""

	while not grid.isTerminal():
		time.sleep(3)
		for box in mail_box:
			for mail in box:
				print(mail.toString())
		grid.__show__()