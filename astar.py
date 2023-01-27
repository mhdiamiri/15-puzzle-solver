from node import *
from heapdict import heapdict

def a_star(node_start:Node) -> list or None:
    frontier = heapdict()
    
    mapping = dict()
    mapping[str(node_start)] = node_start
    
    explored = set()
    g = dict()
    
    frontier[str(node_start)] = node_start.h() + 1
    
    g[str(node_start)] = 0
    
    while len(frontier.heap) != 0:
        str_node_current, f_node_current = frontier.popitem()
        
        node_current = mapping[str_node_current]
        
        if node_current.check():
            return node_current
        
        successors = node_current.successors()
        
        for node_successor in successors:
            mapping[str(node_successor)] = node_successor
            
            successor_cost = g[str(node_current)] + 1
            
            if node_successor in frontier:
                if g[str(node_successor)] <= successor_cost:
                    continue
                
            elif str(node_successor) in explored: 
                if g[str(node_successor)] <= successor_cost:
                    continue

            else:
                frontier[str(node_successor)] = f_node_current + 1
                
            g[str(node_successor)] = successor_cost
            node_successor.setParent( node_current)
            
        explored.add(str(node_current))
        
    return None
