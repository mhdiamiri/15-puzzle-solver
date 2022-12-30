import numpy as np
import visualizer
from node import Node
import dfs

def initial_state():
    arr = np.arange(16)
    np.random.shuffle(arr)
    matrix = arr.reshape(4,4)
    return Node(matrix)

if __name__ == '__main__':
    initial_state = initial_state()
    ans, path = dfs.dfs(initial_state)
    if ans:
        images = []
        i = 0
        for node in path:
            i+=1
            images.append(node.draw(str(i)))
        visualizer.make_gif(images)
    else:
        print('failed!')
    