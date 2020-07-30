import sys

#print(sys.executable)
#print(sys.version)


def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting


print(greet('Jeff'))
print(greet('World'))
