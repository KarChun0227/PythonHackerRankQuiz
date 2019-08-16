import random

num = random.randint(1,10)
print(num)

while True:
    anwser = int(input("Guess a number:"))
    if anwser == num:
        print ("You are Right")
        num = random.randint(1,10)
    elif anwser > num:
        print ("Too High")
    elif anwser < num:
        print ("Too low")
    if input("Wish to continue?") == "no":
        break