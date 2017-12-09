import findLargestIndependentSet
import buildRandomGraph
import matplotlib.pyplot as graph

n_list = []
size_list = []
for i in range(12):
    if(i <= 1): continue
    n = 2**i
    runningTotal = 0
    for j in range(10):
        G = buildRandomGraph.createRandomMatrix(n)
        I = findLargestIndependentSet.largestIndependentSet(G)
        runningTotal += I
    average = runningTotal/10
    n_list.append(i)
    size_list.append(average)

    print('n = ' + str(n) + ' average size of I: ' + str(average))
graph.scatter(n_list, size_list)
graph.xlabel('log(n)')
graph.ylabel('size of independent set')
graph.show()






