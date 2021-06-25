# x = input("Enter 1st number")
# y = input("Enter 2nd number")
# z = x + y
# print(z)
    # this first line of code will interpret the two inputs as strings not int
    # if you were to enter 9 and a 5
    # the output would be '95' concatinizing the two strings
    # so you will have to use an extra variable to convert the string to an int



# x = input("Enter 1st number")
# a = int(x)
# y = input("Enter 2nd number")
# b = int(y)
# z = a + b
# print(z)

    # this variable conversion works, the output of 9 + 5 is 14
    # but there are to many lines of code, you always want to save lines if possible


# x = int(input("Enter 1st number"))
# y = int(input("Enter 2nd number"))
# z = x + y
# print(z)

    # this works just fine; the output of 9 + 5 is 14


# Now lets input a character


# ch = input("enter a character")
# print(ch)
    # this lets the user input as many characters as they would like

# ch = input("enter a character")
# print(ch[0])
    # this will only print the first integer
    # or you could do it this way
# ch = input("enter a character")[0]
# print(ch)


# result = eval(input('enter an expr'))
# print(result)
    # input: 2 + 6 - 1
    # ouput: 7