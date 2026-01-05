# - Find the index of the maximum and minimum elements.

import numpy as np 

n = np.random.randint(1,100,size = (100))


print(np.argmax(n))
print(np.argmin(n))