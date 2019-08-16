numlist = range(1000,1200)

list1 = []
list2 = []

outcome = ""

for i in numlist:
    if i % 7 == 0:
        list1.append(i)

for i in list1:
    if i % 5 == 0:
        list2.append(i)

for i in list2:
    outcome = outcome + "," + str(i)


print(outcome[1:])
