string = input("Give a string:")
strlen = int(len(string))
reverse = ""
i = 1

while i <= strlen:
    reverse = reverse + string[strlen-i]
    i = i + 1

if string == reverse:
    print ("Yes")
else:
    print ("No")
