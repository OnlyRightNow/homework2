""" Cameraman exercise
"""
#: Compatibility with Python 2

from __future__ import division  # 1/2 == 0.5, not 0
from __future__ import print_function  # print('me') instead of print 'me'

import numpy as np
from matplotlib import pyplot as plt


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


#- Read lines from file and convert to list of floats
file = open("camera.txt", "r")
raw_values = file.readlines()
# close file again
file.close()
list = []
for x in raw_values:
    list.append(float(x))
list_length = len(list)
print("number of pixel values: ", list_length)

#- Guess M, N
factors = find_prime_facs(list_length)
print(factors)
print("length of factors: ", len(factors))

i = 0
M = 1
a = int((len(factors))/2)
while i < a:
    M = M*factors.pop()
    i = i + 1
N = int(list_length/M)
print("M: %d, N: %d" % (M, N))

#- Convert list to array and reshape
array = np.asarray(list)
image = np.reshape(array, (M, N))

#- Show image using plt module
plt.figure(0)
plt.subplot(2, 3, 1)
plt.imshow(image)

#- A nicer version of the original plot
rotated = np.rot90(image, 3)
plt.subplot(2, 3, 2)
plt.imshow(rotated, interpolation='nearest', vmin=min(list), vmax=max(list))

#- A plot of the pixel position in x and the pixel value in y, for an image line.
plt.subplot(2, 3, 3)
plt.plot(np.arange(0, len(array), 1), array)

#- Apply threshold to make new binary image, and show binary image
threshold = 0.5
# make a proper copy of the rotated image, so that we only modify the copy
binary = rotated.copy()
binary[rotated < threshold] = 0
binary[rotated >= threshold] = 1
plt.subplot(2, 3, 4)
plt.imshow(binary)

#- Extra points - a good image of the man's pocket.
pocket = rotated[250:400, 325:475]
plt.subplot(2, 3, 5)
plt.imshow(pocket)
# because it's fun
plt.subplot(2, 3, 6)
rotated.sort(axis=1)
plt.imshow(rotated)
plt.show()
