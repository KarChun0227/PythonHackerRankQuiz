fibonnaciNum = []

numLen = int(input("number of fibonnac:"))

i = 0

num = 1

while i < numLen:
    fibonnaciNum.append(num)
    num = num + num
    i = i + 1

print (fibonnaciNum)
    

