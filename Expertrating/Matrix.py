input_str = input("Give input: ")

x,y = input_str.split(",")

print(x)
print(y)

num = 0

allList = []

a = []

for i in range(int(x)):
    a = []
    for i in range(int(y)):
        num = num + 1
        a.append(num)
    allList.append(a)


print (allList)