# Create an array that will have its length and values specified by user input
# With a value search, specified by user input, that will return a index value



from array import *                     # * means to import all the classes from the array
                                        # creates an empty array with a given value
arr = array('i',[])
                                                       # This is asking the user how many values are needed
n = int(input("Enter the length of the array"))        # Input is usually a string so it needs to be converted
                                                       # Us the loop for repeated actions
for i in range(n):                                     # "n" is the length of the array given by the user
    x = int(input("Enter the next value"))             # "x" is the index value in the array
    arr.append(x)
                                                       # This puts the value of x into the arr variable
                                                       # with the .append function, which adds an index value
                                                       # at the end of the array
print(arr)


val = int(input("Enter the value for search"))

k = 0
for e in arr:
    if e == val:            # This is saying 'if the value that is searched matches a number inside the array
        print(k)            # then print the index number
        break               # But how do we know the index number?
                            # We create a counter variable, which in this case is "k"
    k+=1                    # Which adds 1 every time e doesn't match the value being searched

print(arr.index(val))       # This basically prints the value of the search twice



