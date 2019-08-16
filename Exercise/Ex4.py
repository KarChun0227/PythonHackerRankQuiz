num = int(input("Give a number:"))

numRange = range(1, num)

def div(numRange,num):
    divisor = []
    for elem in numRange:
        mod = num % elem
        if mod == 0:
            divisor.append(elem)
    return divisor

for x in div(numRange,num):
    print(x, end=" ")


