import numpy as np
a = np.zeros((4, 3, 2))  # make zero array whose size is (4,3,2)
a[0:2, 1:2, 1] = 1  # Note that, 0:2 means 0 to (2-1), and 1:2 means 1.
print(a)
print(np.average(a))
print(np.max(a))
#(matrix a)0:2 is 0,1 no2 
# / (row)1:2 is 1, no2 
# / (column)1 is index 1 only