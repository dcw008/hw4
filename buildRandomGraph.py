import random
import time

#this function generates an adjacency matrix that represents
#an undirected graph with n vertices. Each edge has 1/2 probability
#and mirrored edge is set accordingly since the matrix is symmetric

def createRandomMatrix(n):
	# create a matrix and set all values of the matrix to 0
	randomMatrix = [[0 for x in range(n)] for y in range(n)]
	symmetricSet = set()
	for i, row in enumerate(randomMatrix):
		for j, col in enumerate(randomMatrix):
			matrixRand = random.random()
			if(i == j):
				randomMatrix[i][j] = 0
				continue
			if (j, i) in symmetricSet:
				continue
			else:
				if matrixRand >= 0.5:
					randomMatrix[i][j] = 1
					randomMatrix[j][i] = 1
					symmetricSet.add((i,j))
				else:
					randomMatrix[i][j] = 0
					randomMatrix[j][i] = 0
					symmetricSet.add((i,j))

	return randomMatrix

def printMatrix(G):
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in G]))