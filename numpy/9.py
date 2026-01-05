#  - Find the mean, median, standard deviation, and variance

import numpy as np 

n = np.random.randint(1,100,size = (100))



print(np.mean(n))
print(np.median(n))
print(np.std(n))
print(np.var(n))