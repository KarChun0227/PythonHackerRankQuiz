import random
 
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)

c = []

for x in a:
    if x in b:
        c.append(x)

print (c)
        