import numpy as np
import visualizer

class Node:
    def __init__(self, matrix) -> None:
        self.matrix = matrix
        
        self.pos = None
        
        for i in range(4):
            for j in range(4):
                if matrix[i][j] == 0:
                    self.pos = (i, j)
                    break
                
        self.parent = None

    def getParent(self):
        return self.parent
    
    def setParent(self, parent):
        self.parent = parent
    
    def up(self):
        (i,j) = self.pos
        new_matrix = np.copy(self.matrix)
        if j > 0:
            new_matrix[i][j], new_matrix[i][j-1] = self.matrix[i][j-1], self.matrix[i][j]
            return Node(new_matrix)
        return None
            
    def down(self):
        (i,j) = self.pos
        new_matrix = np.copy(self.matrix)
        if j < 3:
            new_matrix[i][j], new_matrix[i][j+1] = self.matrix[i][j+1], self.matrix[i][j]
            return Node(new_matrix)
        return None
    
    def left(self):
        (i,j) = self.pos
        new_matrix = np.copy(self.matrix)
        if i > 0:
            new_matrix[i][j], new_matrix[i-1][j] = self.matrix[i-1][j], self.matrix[i][j]
            return Node(new_matrix)
        return None
    
    def right(self):
        (i,j) = self.pos
        new_matrix = np.copy(self.matrix)
        if i < 3:
            new_matrix[i][j], new_matrix[i+1][j] = self.matrix[i+1][j], self.matrix[i][j]
            return Node(new_matrix)
        return None
    
    def draw(self, caption):
        return visualizer.draw(self.matrix, caption)
    
    def check(self) -> bool:
        arr = np.reshape(self.matrix, (16, ))
        print(arr)
        for i in range(16):
            if arr[i] != i: 
                return False
        return True
    
    def successors(self) -> list:
        successors_list = []
        node_up = self.up()
        node_left = self.left()
        node_down = self.down()
        node_right = self.right()
        if node_up: successors_list.append(node_up)
        if node_left: successors_list.append(node_left)
        if node_down: successors_list.append(node_down)
        if node_right: successors_list.append(node_right)
        return successors_list
    
    def h(self) -> int: 
        h = 0

        arr = list(self.matrix.reshape(16,))
        for i in range(4):
            for j in range(4):
                val = self.matrix[i][j]
                exp_i = int((val) / 4)
                exp_j = val % 4
            
                d = np.abs(i - exp_i) + np.abs(j - exp_j)
           
                h += d
                
        return h

    def __str__(self) -> str:
        arr = self.matrix.reshape(16,1)
        string = ''
        for a in arr:
            string += str(a)
        return string
    
def test_case_3():
    arr = np.arange(16)
    np.random.shuffle(arr)
    matrix =  arr.reshape(4,4)
    node = Node(matrix)
    print(node.check())
    print(matrix)
    print(node.h())
    print(str(node))
    return str(node)
    
def str2node(arr:str):
    arr = arr.replace("[", "")
    arr = arr.replace("]", " ")
    arr2 = []

    arr = arr.split(" ")
    for s in arr:
        if s!= '':
            arr2.append(int(s))

    matrix =  np.reshape(np.array(arr2), (4, 4))
    
    return Node(matrix)

    
