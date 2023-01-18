from node import Node

def HClimbing(startNode:Node):
    currentNode = startNode
    limit = 0
    path = []
    while True:
        successorsList = currentNode.successors()
        min_successor = min_h2_finder(successorsList)
        print('current state', str(currentNode))
        if currentNode.h2() <= min_successor.h2():
            return currentNode, path
        else:
            currentNode = min_successor
            limit += 1
        if limit == 1000: return currentNode, path
        
        path.append(currentNode)

def min_h2_finder(sList):
    minWeight = 10**4
    minNode = None
    for successor in sList:
        if successor.h2() <= minWeight:
            minWeight = successor.h2()
            minNode = successor
    return minNode
