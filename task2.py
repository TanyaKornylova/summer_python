import numpy as np
import random 

n = int((input()))
a = [0.0 for j in range(n)]

for i in range(n):
  rand_num = random.uniform(-1, 1)
  print("%.4f"% (rand_num))
  a[i] = rand_num

arr_mean = np.mean(a)
print("Arithmetical mean: ")
print(arr_mean)
