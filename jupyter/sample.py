import numpy as np

# Numpy offers additional data structures
# the arange is an array-range object
n = np.arange(2,8,0.5) # start, stop-before, step
n # all members must be the same data type
print( n.dtype ) # numpy will choose the relevant dtype: int or float