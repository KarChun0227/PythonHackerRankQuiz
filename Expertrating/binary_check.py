input_str = input()

result =""

binary = input_str.split(",")

for x in binary:
  num = int(x,2)
  print(num)
  if num % 3 == 0:
    result = result + "," + str(x)

result = result[1:]
print (result)

# 0011,0100,0101,1001