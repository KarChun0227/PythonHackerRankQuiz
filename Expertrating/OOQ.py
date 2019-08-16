from math import sqrt

input_str = input("Give input: ")

numlist = input_str.split(",")

C = 50
H = 30

result = ""

for D in numlist:
    Q = sqrt(((2*C*int(D))/H))
    result = result + "," + str(int(Q))

print (result[1:])

# 100,150,180