
# i = 1                       # Initialization

# while i<=5:                 # Condition
#    print("william")
#    i = i + 1               # Increment/Decrement

    # the objective here is to print my name 5 times in a row
    # without the Increment/Decrement the loop would go on forever
    # when using while loops you have to keep track of the end/stopping point
    # this would also work in reverse order
        # i = 5
        # while i>=1:
        #   print("william")
        #   i = i - 5

# i = 1

# while i<=5:
#    print(i,"william")
#    i = i + 1

        # the output: 1 william
                    # 2 william
                    # 3 william
                    # 4 william
                    # 5 william

    # Nested Loops
    # The objective here is to print out "william rocks rocks rocks rocks" 5 times in a row


# i = 1
# j = 1

# while i<=5:
#    print("william ")
#    while j<=4:                 # this is the nested loop
#        print("rocks ")
#        j=j+1

#    i=i+1

                # output: william               # this is because the nested loop will be completed first
                        # rocks                 # think of the outer loop as a day and the inner loop as hours
                        # rocks                      # all the hours of a day have to pass before the next day comes
                        # rocks                 # the other problem is that "rocks needs to be on the same line
                        # rocks
                        # william
                        # william
                        # william
                        # william


i = 1

while i<=5:
    print("william ",end="")    # end="" will stop the loop from going to a new line
    j = 1                       # declaring the value after the first loop and before the nested
    while j<=4:                 # will get 4 'rocks' for every 'william
        print("rocks ",end="")
        j=j+1

    i=i+1
    print()                     # but the output would put everything on one line so we need to put a print at the end

    # output: william rocks rocks rocks rocks
            # william rocks rocks rocks rocks
            # william rocks rocks rocks rocks
            # william rocks rocks rocks rocks
            # william rocks rocks rocks rocks