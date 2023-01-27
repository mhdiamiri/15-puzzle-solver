import numpy as np
from node import *

arr = np.arange(16)

matrix =  arr.reshape(4,4)
node = Node(matrix)

d = {str(node): node}

print(d[str(node)])