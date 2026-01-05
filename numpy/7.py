
# ● From the array np.arange(1, 21), extract:
# ● - Even numbers
# ● - Odd numbers
# ● - Every 3rd element


import numpy as np

n = np.arange(1,21)

print(n[n%2 == 0])
print(n[n%2 == 1])
print(n[n%3 == 0])
