# Six ways to create an Array
# 1. array()
# 2. linespace()
# 3. logspace()
# 4. arange()
# 5. zeros()
# 6. ones()

from numpy import *

# 1. array

                                    # When using numpy, the array value doesn't need to be stated
# arr = array([1,2,3,4,5])          # Yet you can state it if you want to

# print(arr)              # output: [1 2 3 4 5]
# print(arr.dtype)        # output: int32

# arr = array([1,2,3,4,5.0])

# print(arr)                # output: [1. 2. 3. 4. 5.]
# print(arr.dtype)          # output: float64
                            # The array converts every value to a float, in this case



# 2. linspace


# arr = linspace(0, 15, 16)            # linspace will take 3 parameters (start,stop,number of parts)
                                       # If the number of parts isn't specified, the default is 50 parts
                        # in this instance, 0 is where you start, 15 is where you stop
                        # and 16 is how many numbers you want in between the starting number and the stopping number
# print(arr)            # output: [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15.]
                        # this is a rather 'even' example

# arr = linspace(0, 10, 5)

# print(arr)            # output: [ 0.   2.5  5.   7.5 10. ]
                        # This would be a not so even example
                        # Notice that they are evenly divided parts and they're floats



# 3. logspace


# arr = logspace(1, 40, 5)

# print(arr)             # output: [1.00000000e+01 5.62341325e+10 3.16227766e+20 1.77827941e+30 1.00000000e+40]

# print('%.2f' %arr[4])  # output: 10000000000000000303786028427003666890752.00



# 4. arange
from numpy import arange, zeros

# arr = arange(1, 15, 2)      # (starting number, ending number-excluded, step/interval distance)

# print(arr)              # output: [ 1  3  5  7  9 11 13]



# 5. zeros


# arr = zeros(5)

# print(arr)              # output: [0. 0. 0. 0. 0.]



# 6. ones
from numpy.core import ones

arr = ones(5)

print(arr)              # output: [1. 1. 1. 1. 1.]