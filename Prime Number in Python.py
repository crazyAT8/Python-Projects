# we are going to write a code to see is a given number is prime or not

num = 7

for i in range(2,num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")