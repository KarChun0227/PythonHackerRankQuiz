import random
def game():
    low = 1
    high = 100
    num = random.randint(low,high)
    while True:
        num = random.randint(low,high)
        print (str(num))
        anwser = input("Did i right\n")
        if anwser == "right":
            break
        else:
            if anwser == "low":
                low = num + 1
            else:
                high = num - 1

if __name__ == "__main__":
    game()

