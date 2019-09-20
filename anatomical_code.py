""" Anatomical exercise
"""
from __future__ import division  # 1/2 == 0.5, not 0
#: Compatibility with Python 3
from __future__ import print_function  # print('me') instead of print 'me'

import numpy as np


def find_prime_facs(n):
  list_of_factors=[]
  i=2
  while n>1:
    if n%i==0:
      list_of_factors.append(i)
      n=n/i
      i=i-1
    i+=1
  return list_of_factors


#- Read file into list of float values
file = open("anatomical.txt", "r")
raw_values = file.readlines()
# close file again
file.close()
list = []
for x in raw_values:
    list.append(float(x))
list_length = len(list)
#- How many pixel values?
print("number of pixel values: ", list_length)

#- Find the size of a slice over the third dimension
Z = 32

#- Find candidates for I
td_size = list_length/Z
print("2D size: ", td_size)
factors = find_prime_facs(list_length/Z)
print(factors)

#- Find candidate pairs for I, J
candidates = []
for i in range(0, len(factors)):
    I = factors[i]
    M = td_size / I
    # insert only if it doesn't exist yet
    if ([I, M]) not in candidates:
        if ([M, I]) not in candidates:
            candidates.append([int(I), int(M)])
    for j in range(0, len(factors)):
        if i == j:
            continue
        I = int(I*factors[j])
        M = int(td_size/I)
        # insert only if it doesn't exist yet
        if ([I, M]) not in candidates:
            if ([M, I]) not in candidates:
                candidates.append([int(I), int(M)])
candidates.sort()
print(candidates)
# image will have nearly square dimension, so we can filter out the candidates where one dimension is very small ie<100
realistic_candidates = candidates[16:20]
print("realistic candidates: ", realistic_candidates)

#- Try reshaping using some candidate pairs
array = np.asarray(list)
image = np.reshape(array, (realistic_candidates[0][0], realistic_candidates[0][1], Z))


