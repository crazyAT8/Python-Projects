# Declare functions using the keyword "def".
# As with all code blocks, function bodies are indented underneath the function declaration.
# no arguments
# Returns "None" (invoked for its side effects)

def greet():
    print("hello!")

greet()

x = greet()

print(x)

# one argument
# returns a value
# pure function (no side effects)



def increment(x):
    return x + 1

print(increment(4))


# Lambda function
# computing without any state
# a stateful design can be represented by a stateless design

# foo = lambda x: x["greeting"]

foo = reversed([1,2,3,4,5])
bar = [6,7,8,9,10]
baz = [x for x in zip(foo, bar)]
print(baz)

print(sorted(baz, key=lambda t: t[0]))