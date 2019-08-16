input_str = input()

number = input_str.split("\n")

def amount(num):
  x = 0
  y = 0
  z = 0

  if num > 100:
    x = 100
  else:
    x = num

  if num > 300:
    y = 200
    z = num - 300
  else:
    y = num - 100

  return (x*60+y*70+z*80)

if __name__ == "__main__":
  for x in num:
    print (amount(int(x)))