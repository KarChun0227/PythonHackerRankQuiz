input_str = input()

result = ""

word = input_str.split(",")

sortedword = sorted(word)

for x in sortedword:
    result = result + "," + x

result = result[1:]
print(result)

# order,hello,would,test