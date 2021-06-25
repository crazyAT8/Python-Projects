
# for i in range(4):                  # i will loop j four times
#    for j in range(4):               # j will loop # four times
#        print("# ", end="")          # end="" will keep the # in the same row
                                      # the last print will take the flow back to i to start again
#    print()

                  # output: # # # #
                            # # # #
                            # # # #
                            # # # #

# for i in range(4):                      # i is the number of rows
#    for j in range(i+1):                 # j is the number of columns in each row
#        print("# ",end="")

#    print()

                # output: #
                          # #
                          # # #
                          # # # #

# for i in range(4):
#    for j in range(4-i):
#        print("# ",end="")

#    print()

                # output: # # # #
                          # # #
                          # #
                          #