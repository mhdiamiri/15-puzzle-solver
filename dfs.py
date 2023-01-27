from node import Node
from collections import deque
import numpy as np

stack = deque()

def dfs(initial_state:Node, LIMIT=np.inf):
    stack.append(initial_state)
    explored = set()
    limit = 0
    while len(stack) > 0:
        limit += 1
        current_state = stack.pop()
        
        if current_state.check():
            return current_state
        
        explored.add(str(current_state))
        
        successors = current_state.successors()
        for successor in successors:
            if str(successor) not in explored:
                successor.setParent(current_state)
                stack.append(successor)
        
        if limit >= LIMIT:
            print("Limit Reached!")
            return None
    return None
        