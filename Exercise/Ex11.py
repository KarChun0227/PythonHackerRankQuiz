num = int(input("Give a number:"))

numRange = range(1,num)

result = []

for x in numRange:
    if num % x == 0:
        result.append(x)

print (result)

if len(result) == 1:
    print ("Is Prime")
else:
    print ("Not prime")
    