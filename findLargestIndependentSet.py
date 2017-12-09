import buildRandomGraph
#given a matrix representation of nxn graph G
#find the largest independent set
def largestIndependentSet(G):

    #compute the degrees of all vertices in our list
    degrees = getDegrees(G)

    #sort counts by their degree
    degrees.sort(key=lambda tup: tup[1])

    independentSet = []
    for vertex in degrees:
        independentSet.append(vertex)

        #look up all the edges with that vertex in the adjacency matrix
        vertexIndex = vertex[0]
        neighbors = getNeighbors(vertexIndex, G)

        #remove the vertices from our counts list that are connected to the vertex we added to I
        removeNeighbors(neighbors, degrees)

    return len(independentSet)

#gets the degrees of each vertex in the graph
def getDegrees(G):
    counts = []
    #create a list of the degree of each vertex
    for i, row in enumerate(G):
        degreeCount = 0
        for j, col in enumerate(row):
            if(col == 1):
                degreeCount += 1
        #keep of the tuple where the first is the vertex and the second is the degree
        counts.append((i,degreeCount))
    return counts



#given some vertex and its graph, output all of its neighboring nodes
def getNeighbors(vertex, G):
    neighbors = []
    row = G[vertex]
    for i, element in enumerate(row):
        if(element == 1):
            neighbors.append(i)
    return neighbors

#removes associated neighbors from counts
def removeNeighbors(neighbors, counts):
    #remove all the neighbors from the counts
    for neighbor in neighbors:
        for element in counts:
            if(element[0] == neighbor):
                counts.remove(element)
                break
    return counts


# list = [(0, 10), (3, 9), (5, 2), (1, 6)]
# list.sort(key=lambda tup: tup[1])
# neighbors = [3, 5]
# counts = removeNeighbors(neighbors, list)

G = buildRandomGraph.createRandomMatrix(2)
buildRandomGraph.printMatrix(G)
# degrees = getDegrees(G)
# print(degrees)
I = largestIndependentSet(G)
print(I)




