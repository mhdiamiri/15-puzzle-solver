import numpy as np

import visualizer
from node import Node

from dfs import *
from hill_climbing import *
from astar import *

def inv_count(arr):
    arr1=[]
    for y in arr:
        for x in y:
            arr1.append(x)
    arr = arr1
    inv_count = 0
    for i in range(15):
        for j in range(i + 1, 16):
            if (arr[j] and arr[i] and arr[i] > arr[j]):
                inv_count += 1
                
    return inv_count
 
 
def findxpos(matrix):
    for i in range(4 - 1,-1,-1):
        for j in range(4 - 1,-1,-1):
            if (matrix[i][j] == 0):
                return 4 - i
 
 # check if matrix is solvable
def is_solvable(matrix):
    invcount = inv_count(matrix)
    pos = findxpos(matrix)
    if (pos & 1):
        return invcount & 1
    else:
        return ~(invcount & 1)

def random_initial_state():
    arr = np.arange(16)
    np.random.shuffle(arr)
    matrix = arr.reshape(4,4)
    return Node(matrix)

def using_hill_climbing(initial_state, limit):
    ans = hill_climbing(initial_state, limit)
    if not ans[-1].check():
        print("[hill climbing] No Answer Found!")
    else:
        print("[hill climbing] Answer Found Successfully.")
    
    make_gif(ans, 'hill-climbing')
    
def using_dfs(initial_state, limit):
    path = []
    last_node = dfs(initial_state, limit)
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

def using_astar(initial_state, limit):
    last_node = a_star(initial_state, limit)
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
    
    if not is_solvable(initial_state.matrix):
        print('initial state:\n', initial_state.matrix)
        print("initial state is not solvable.")
        input("press enter to exit.")
        return
    
    print("\33[2J\33[1;1H")
    
    print('initial state:\n', initial_state.matrix)
    print("choose from below:")
    print("1. Solve using A* algorithm")
    print("2. Solve using Hill Climbing algorithm")
    print("3. Solve using DFS algorithm")
    answer = input()
    limit = input("Enter Maximum Number of Steps(enter -1 to run without step limit): ")
    
    if limit == '-1': 
        limit =np.inf
    else:
        limit = int(limit)
    
    if answer == "1":
        
        print(f"Solving using A*... (limit = {limit} steps)")
        
        using_astar(initial_state, limit)
    elif answer == "2":
        print(f"Solving using Hill Climbing... (limit = {limit} steps)")
        using_hill_climbing(initial_state, limit)
    else:
        print(f"Solving using DFS... (limit = {limit} steps)")
        using_dfs(initial_state, limit)

if __name__ == '__main__':
    main()



