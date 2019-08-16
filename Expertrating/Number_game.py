input_str = input("Give input: ")

numlist = input_str.split(",")

numlist = sorted(numlist, reverse = True)

result = ""

for x in numlist:
    y = 9 - int(x)
    result = result + "," + ("9"*y) + x

print (result[1:])

#2,5,8