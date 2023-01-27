from node import Node
from collections import deque

stack = deque()

def dfs(initial_state:Node):
    stack.append(initial_state)
    explored = set()
    
    while len(stack) > 0:
        current_state = stack.pop()
        
        if current_state.check():
            return current_state
        
        explored.add(str(current_state))
        
        successors = current_state.successors()
        for successor in successors:
            if str(successor) not in explored:
                successor.setParent(current_state)
                stack.append(successor)

    return None
        