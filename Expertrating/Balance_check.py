input_str = input()

statu = input_str.split(",")

balance = 0

for x in statu:
  amount, act = x.split("-")
  if act == "D":
    balance = balance + int(amount)
  if act == "W":
    balance = balance - int(amount)

if balance > 5000:
  print (balance*1.05)
else:
  print (balance)

  # 2000-D,4000-D,500-W
