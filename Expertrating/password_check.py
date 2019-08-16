import string

input_str = input("Give input: ")

passwordlist = input_str.split(",")

result = ""

for x in passwordlist:
    if len(x) > 7 or len(x)<3 or " " in x:
        continue
    if "*" in x or "#" in x or "+" in x or "@" in x:
        if any(c.islower() for c in x) and any(c.isupper() for c in x):
            result = result + "," + x

result = result[1:]
print (result)

  # AbcA@1,a B1#,sW3e*,2We#3345wq