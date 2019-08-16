import random

randomList = random.sample(range(1,21), 20)

def setList(a):
    b = set(a)
    return b

print (randomList)
print (setList(randomList))