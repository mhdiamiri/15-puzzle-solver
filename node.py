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
        this = self.__str__()
        target = Node(np.array([
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,0]
        ]))
        checker = set()
        checker.add(this)
        checker.add(str(target))
        if len(checker) == 1: return True
        return False
    
    def h1(self) -> int:
        h = 0
        arr = self.matrix.reshape(16,)
        for (a, i) in zip(arr[:-1], range(15)):
            if a != i + 1:
                h += 1
        if arr[15] != 0:
            h += 1
        return h
    
    #TODO 
    def successors() -> list:
        successors_list = []
        
        pass
    
    #TODO
    def h2(self) -> int: #FIX IT. does not work.
        h = 0
        arr = list(self.matrix.reshape(16,))
    
        for i in range(4):
            for j in range(4):
                if i == 4 and j == 4: pos = arr.index(0)
                else: pos = arr.index(i + j + 1)
                ii = int(pos / 4)
                jj = pos % 4
                print(abs(ii - i) + abs(jj - j))
                h += abs(ii - i) + abs(jj - j)
                
        return h

    def __str__(self) -> str:
        arr = self.matrix.reshape(16,1)
        string = ''
        for a in arr:
            string += str(a)
        return string
    
def test_case_1():
    arr = np.arange(16)
    np.random.shuffle(arr)
    matrix = arr.reshape(4,4)
    node = Node(matrix)
    img = node.draw('caption')
    img.show()
    
    up_node = node.up()
    if up_node is not None:
        img = up_node.draw('up')
        img.show()
    else:
        print("doesn't have up node.")
        
    down_node = node.down()
    if down_node is not None:
        img = down_node.draw('down')
        img.show()
    else:
        print("doesn't have down node.")
    
    left_node = node.left()
    if left_node:
        img = left_node.draw('left')
        img.show()
    else:
        print("doesn't have left node.")
        
    right_node = node.right()
    if right_node is not None:
        img = right_node.draw('right')
        img.show()
    else:
        print("doesn't have right node.")   

def test_case_2():
    matrix = np.array([
       [1,3,2,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,0]
    ])
    node = Node(matrix)
    print(node.check())
    print(node.h1())
    print(node.h2())
    
def test_case_3():
    arr = np.arange(16)
    np.random.shuffle(arr)
    matrix =  arr.reshape(4,4)
    node = Node(matrix)
    print(matrix)
    print(node.h1())
    print(node.h2())
    
if __name__ == "__main__":
    #test_case_1()
    test_case_2()
    # test_case_3()