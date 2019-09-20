""" Anatomical exercise
"""
from __future__ import division  # 1/2 == 0.5, not 0
#: Compatibility with Python 3
from __future__ import print_function  # print('me') instead of print 'me'

#- Our usual imports

#- Read file into list of float values
file = open("anatomical.txt", "r")
raw_values = file.readlines()
# close file again
file.close()
list = []
for x in raw_values:
    list.append(float(x))

#- How many pixel values?
print("number of pixel values: ", len(list))
#- Find the size of a slice over the third dimension
Z = 32
#- Find candidates for I

#- Find candidate pairs for I, J

#- Try reshaping using some candidate pairs


