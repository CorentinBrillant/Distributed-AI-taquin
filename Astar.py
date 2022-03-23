#coding:utf-8
from math import *

def find_min_f_among_nodes(matrix, nodes):
	mini = matrix[nodes[0][0]][nodes[0][1]]
	i = 0
	for j in range(len(nodes)):
		if matrix[nodes[j][0]][nodes[j][1]] < mini:
			mini = matrix[nodes[j][0]][nodes[j][1]]
			i = j
	return i

def find_max_f_among_nodes(matrix, nodes):
	mini = matrix[nodes[0][0]][nodes[0][1]]
	i = 0
	for j in range(len(nodes)):
		if matrix[nodes[j][0]][nodes[j][1]] > mini:
			mini = matrix[nodes[j][0]][nodes[j][1]]
			i = j
	return mini


def star(start, goal, grid):
	size = len(grid)
	inf = 99
	f_scores = [[inf for i in range(len(grid))] for j in range(len(grid))]
	g_scores = [[inf for i in range(len(grid))] for j in range(len(grid))]
	f_scores[start[0]][start[1]] = 0
	g_scores[start[0]][start[1]] = 0
	open_nodes = []
	closed_nodes = []
	open_nodes.append(start)
	while len(open_nodes) > 0:
		current_node = open_nodes.pop(find_min_f_among_nodes(f_scores, open_nodes))
		#print("i'm node : "+str(current_node))
		closed_nodes.append(current_node)
		if current_node == goal:
			break
		children = [[-1,0],[0,1],[1,0],[0,-1]]
		for move in children:
			child = [u+v for u,v in zip(current_node,move)]
			if child[0] >= 0 and child[0] < size and child[1] >= 0 and child[1] < size and grid[child[0]][child[1]] == 0:
				if child in closed_nodes:
					continue
				g_scores[child[0]][child[1]] = g_scores[current_node[0]][current_node[1]] + 1
				f_scores[child[0]][child[1]] = g_scores[child[0]][child[1]] + sqrt((child[0]-goal[0])**2 + (child[1]-goal[1])**2)
				if child in open_nodes:
					if g_scores[child[0]][child[1]] > find_max_f_among_nodes(g_scores, open_nodes):
						continue
				#print('im child :'+str(child)+"with f_scores :"+str(f_scores[child[0]][child[1]])+" adn g : "+str(g_scores[child[0]][child[1]]))
				open_nodes.append(child)
	best_path = []
	current_node = goal
	if f_scores[goal[0]][goal[1]] < inf:
		while current_node != start:
			best_child = [0,0]
			best_f = f_scores[current_node[0]+best_child[0]][current_node[1]+best_child[1]]
			for child in [[-1,0],[0,1],[1,0],[0,-1]]:
				if child[0]+current_node[0] >= 0 and child[0]+current_node[0] < size and child[1]+current_node[1] >= 0 and child[1]+current_node[1] < size and f_scores[current_node[0]+child[0]][current_node[1]+child[1]] <= best_f and grid[current_node[0]+child[0]][current_node[1]+child[1]]==0 and (best_path==[] or best_path[-1]!=child):
					best_child = child
					best_f = f_scores[current_node[0]+child[0]][current_node[1]+child[1]]
			best_path.append([i*j for i,j in zip(best_child,[-1,-1])])
			current_node = [i+j for i,j in zip(current_node,best_child)]
		best_path.reverse()
	
	return f_scores, g_scores, best_path



def show(matrix):
	size = len(matrix)
	for x in range(size):
		print("|\t", end="")
		for y in range(size):
			print("%.1f\t"  % matrix[x][y],end="")
		print("|")
	print("")

if __name__ == '__main__':
	m = [[0 for i in range(5)] for j in range(5)]
	m[3][3]=2
	m[1][1]=2
	m[1][0]=2
	m[1][3]=2
	m[1][2]=2
	m[3][1]=2
	m[3][2]=2
	m[3][4]=2
	m[3][0]=2

	#m[3][2]=2
	#m[4][1]=2
	a,b,c = star([0,2],[0,2],m)
	print("f_scores:\n")
	show(a)
	print("grille :\n")
	show(m)
	print(c)