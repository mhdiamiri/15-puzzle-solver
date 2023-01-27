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
    ans = hill_climbing(initial_state)
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
    print("\33[2J\33[1;1H")
    
    print("choose from below:")
    print("1. Use Random Initial State")
    print("2. Enter Initial State")
    answer = input()
    
    if answer == "1":
        initial_state = random_initial_state()
        
    else:
        print("\33[2J\33[1;1H")
        matrix = np.reshape(np.zeros(16, dtype=int), (4, 4))
        for i in range(4):
            row = input(f"Please enter {i+1}'th row:").split(' ')
            for j in range(4):
                matrix[i][j] = int(row[j])
        
        initial_state = Node(matrix)
    
    print("\33[2J\33[1;1H")
    print('initial state:\n', initial_state.matrix)
    print("choose from below:")
    print("1. Solve using A* algorithm")
    print("2. Solve using Hill Climbing algorithm")
    print("3. Solve using DFS algorithm")
    answer = input()
    if answer == "1":
        print("Solving using A*...")
        using_astar(initial_state)
    elif answer == "2":
        print("Solving using Hill Climbing...")
        using_hill_climbing(initial_state)
    else:
        print("Solving using DFS...")
        using_dfs(initial_state)

if __name__ == '__main__':
    main()
