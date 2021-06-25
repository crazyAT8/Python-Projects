# Arrays must have only one data type
# Arrays in python do not have a specific size
# need to import a module

from array import *                   # * means you want to work with all the functions in a module

vals = array('i',[5,9,-8,4,2])        # when using an array, you have to specify a particular TypeCode
                                      # google python TypeCode for the whole table
        # this dot(.) then name is a function
# print(vals.buffer_info())             # .buffer_info will print the address and the size of the array
        # output: (1901942179824, 5)

        # .typecode will return the array type, which is 'i'

# this is how you print all the values
# for i in range(len(vals)):
#    print(vals[i])

# or

for e in vals:
    print(e)

# working with characters

vals2 = array('u',['a','e','i'])      # 'u' is unicode character in typecode

for e in vals2:
    print(e)