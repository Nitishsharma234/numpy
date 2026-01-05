#- A 5×5 identity matrix.


import numpy as np

n = np.zeros((5,5),dtype=int)

for i in range(5):
    for j in range(5):
        if i == j:
            n[i][j] = 1

        else:
            n[i][j] = 0

print(n)               