
# BREAK

# We are designing a code to mimic a vending machine
# av = 5

# x = int(input("how many pieces of candy"))

# i = 1                               # 'i' in this instance would represent a piece of candy
# while i <= x:                       # remember 'x' is the number of times to run the loop
                                    # the 'if' statement is setting up the break if the
#    if i > av:                      # av (available) pieces of candy is reach
#        print("out of stock")       # if it is reached it breaks out of the while loop to the last print statement
#        break

#    print("candy")
#    i +=1

# print("bye")

                    # output: how many pieces of candy6
                            # candy
                            # candy
                            # candy
                            # candy
                            # candy
                            # out of stock
                            # bye


# CONTINUE

# Print a list of numbers between 1=100, but don't print any numbers divisible by 3 or 5

# for i in range(1,101):
                                              # you could use or or and in the if statement
#    if i % 3 == 0 or i % 5 == 0:              # the if statement takes you out of the loop
#        continue                              # continue will put you back in the loop

#    print(i)


# PASS
# in pass we normally use it to skip a block(block being a loop, if statement, function, or class)
# Print a list from 1 to 100 except the odd numbers

# for i in range(1,100):

#    if(i%2!=0):
#        pass
#    else:
#        print(i)


# for i in range(5):

#    if i==3:
#        continue
#    print("hello",i)

                # output: hello 0
                        # hello 1
                        # hello 2
                        # hello 4

# for i in range(5):

#    if i==3:
#        break
#    print("hello", i)

                # output: hello 0
                        # hello 1
                        # hello 2


