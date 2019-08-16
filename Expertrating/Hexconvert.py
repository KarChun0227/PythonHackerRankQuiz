input_str = input("Give input: ")

color = input_str.split(",")

result =""

c = 0

while c < len(color):
  convert = color[c].split("-")
  i = 0
  while i < len(convert):
    if convert[i] == "INVALID":
      continue
    if int(convert[i]) > 255:
      color[i] = "INVALID"
    i = i + 1
  c = c + 1

for y in color:
  if y == "INVALID":
    result = result + "," + "INVALID"
    continue
  convert2 = y.split("-")
  hexcolor = "#"
  for x in convert2:
    if int(x) > 16:
      hexcolor = hexcolor + hex(int(x))[2:]
    else:
      hexcolor = hexcolor + "0" + hex(int(x))[2:]
  result = result + "," + hexcolor

print (result[1:])

# 12-13-14,45-156-23,234-234-256