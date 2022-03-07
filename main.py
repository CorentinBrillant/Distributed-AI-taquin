from Grille import *
from Agent import *
import time

if __name__ == '__main__':
	n = 5
	grid = Grille(n)

	mail_box = [[],[],[]]
	# agent_1 = Agent(1,1,4,4,grid, mail_box)
	# agent_2 = Agent(0,0,3,4,grid, mail_box)
	agent_1 = Agent(1,1,3,5,grid, mail_box)
	agent_2 = Agent(0,0,3,4,grid, mail_box)
	agent_1.start()
	agent_2.start()
	grid.__show__()