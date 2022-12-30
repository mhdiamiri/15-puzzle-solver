from node import Node
from collections import deque

stack = deque()

def dfs(initial_state:Node):
    path = []
    stack.append(initial_state)
    explored = set()
    limit = 0
    while len(stack) > 0:
        limit += 1
        current_state = stack.pop()
        print('current state', str(current_state))
        
        if current_state.check():
            print('found!')
            return current_state, path
        if limit == 1000: return current_state, path
        
        explored.add(str(current_state))
        path.append(current_state)
        
        left =  current_state.left()
        right = current_state.right()
        up = current_state.up()
        down = current_state.down()
        
        i = 0
        if left:
            if str(left) not in explored:
                stack.append(left)
                i += 1
        if right:
            if str(right) not in explored:
                stack.append(right)              
                i += 1
        if up:
            if str(up) not in explored:
                stack.append(up)
                i += 1
        if down:
            if str(down) not in explored:
                stack.append(down)
                i += 1
                
        if i == 0: path = path[:-1]
                
    return None
        