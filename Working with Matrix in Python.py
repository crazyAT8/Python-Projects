from numpy import *
from numpy import array

# arr1 = array([
#                [1, 2, 3],
#                [4, 5, 6]

#              ])

# print(arr1.ndim)                     # ndim function is 'number of dimensions' to check
                                      # output: 2
# print(arr1.shape)
                                      # output: (2, 3)
                                      # which is 2 rows and 3 columns
# print(arr1.size)
                                      # output: 6
                                      # total number of values in the multi dimensional array
# arr2 = arr1.flatten()

# print(arr2)
                                    # output: [1 2 3 4 5 6]
                                    # '.flatten' function turns a multi dimensional array into a single dimension
# vice versa

arr1 = array([
                [1, 2, 3, 6, 2, 9],
                [4, 5, 6, 7, 5, 3]

            ])

arr2 = arr1.flatten()

arr3 = arr2.reshape(3, 4)
                                    # the reshape parameters are number of rows and number of columns
print(arr3)
                                    # output:
                                    #    [[1 2 3 6]
                                    #     [2 9 4 5]
                                    #     [6 7 5 3]]
