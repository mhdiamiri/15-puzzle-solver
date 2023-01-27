from node import Node

def hill_climbing(start_node:Node):
    current_node = start_node
    
    path = []
    
    while not current_node.check():
        path.append(current_node)
        successors = current_node.successors()
        
        changed = False
        
        for successor in successors:
            
            if successor.h() < current_node.h():
                
                current_node = successor
                changed = True
        
        if not changed:
            return path
        