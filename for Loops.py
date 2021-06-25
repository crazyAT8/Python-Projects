# In a while loop you have to specify a certain condition but not in for loops
# For loops usually works with a sequence

x = ['william',33, 2.3]

for i in x:             # "i" represents one element of this list at a time
    print(i)

x = 'william'

for i in x:
    print(i)

for i in ['william', 33, 2.3]:      # you can just have a list there by itself with no variable
    print(i)

for i in range(10):                 # this will print ten values 0-9
    print(i)

for i in range(11,21,1):            # three things need to be specified when specifying a range
    print(i)                        # 1. the starting point which is inclusive
                                    # 2. the ending point which is exlusive
                                    # 3. how many numbers you want to count by

for i in range(20,10,-1):           # the negative one makes the list flow in descending order
    print(i)

for i in range(1,21):
    if i % 5 != 0:                  # this 'if' will make it so that 5 doesn't get printed
        print(i)                    # its saying print as long as the out come of a number that is divided by
                                    # five doesn't equal zero, and the only number between one and twenty that
                                    # equals zero when divided by five is five. So five doesn't get printed.


