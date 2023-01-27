from node import Node
import numpy as np

def hill_climbing(start_node:Node, LIMIT=np.inf):
    current_node = start_node
    
    path = []
    limit = 0
    
    while not current_node.check():
        limit += 1
        path.append(current_node)
        successors = current_node.successors()
        
        changed = False
        
        for successor in successors:
            
            if successor.h() < current_node.h():
                
                current_node = successor
                changed = True
        
        if not changed:
            return path
        
        if limit >= LIMIT:
            print("Limit Reached!")
            return None