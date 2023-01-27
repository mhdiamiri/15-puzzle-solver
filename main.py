import numpy as np

import visualizer
from node import Node

from dfs import *
from hill_climbing import *
from astar import *

def random_initial_state():
    arr = np.arange(16)
    np.random.shuffle(arr)
    matrix = arr.reshape(4,4)
    return Node(matrix)

def using_hill_climbing(initial_state):
    ans = hill_climbing.hill_climbing(initial_state)
    if not ans[-1].check():
        print("[hill climbing] No Answer Found!")
    else:
        print("[hill climbing] Answer Found Successfully.")
    
    make_gif(ans, 'hill-climbing')
    
def using_dfs(initial_state):
    path = []
    last_node = dfs(initial_state)
    if last_node is not None:
        print("[DFS] Answer Found Successfully.")
        current_node = last_node
        
        path.append(current_node)
        while current_node.getParent() is not None:
            current_node = current_node.getParent()
            path.append(current_node)
        
        make_gif(path[::-1], 'dfs')
        
    else:
        print("[DFS] No Answer Found!")

def using_astar(initial_state):
    last_node = a_star(initial_state)
    path = []
    if last_node is not None:
        print("[A*] Answer Found Successfully.")
        current_node = last_node
        
        path.append(current_node)
        while current_node.getParent() is not None:
            current_node = current_node.getParent()
            path.append(current_node)
        
        make_gif(path[::-1], 'A-Star')
    else:
        print("[A*] No Answer Found!")
        
def make_gif(path, filename):
    images = []
    i = 0
    for node in path:
        i+=1
        images.append(node.draw("Step: "+str(i)))
    visualizer.make_gif(images, filename)
    
    print(f"GIF generated.\nfilename: {filename}.gif")
   
def main():
    matrix = np.reshape(np.zeros(16, dtype=int), (4, 4))
    for i in range(4):
        row = input(f"Please enter {i+1}'th row:").split(' ')
        for j in range(4):
            matrix[i][j] = int(row[j])
    
    using_astar(Node(matrix))
                 
if __name__ == '__main__':
    main()
