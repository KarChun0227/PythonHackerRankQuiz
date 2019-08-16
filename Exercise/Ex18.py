import random

def game():
    digit = str(random.randrange(1000,9999))
    while True:
        print (digit)
        num = input("Guss it!!\n")
        result = check(num,digit)
        if result[2] == False:
            print ("Cow: " + str(result[0]) + "Bulk: " + str(result[1]))
        elif result[2] == True:
            print("You right")
            break

def check(p,d):
    if p == d:
        return [4, 0, True]
    else:
        cow = 0
        bulk = 0
        if p[0] in d:
            bulk = bulk + 1
        if p[1] in d:
            bulk = bulk + 1
        if p[2] in d:
            bulk = bulk + 1
        if p[3] in d:
            bulk = bulk + 1
        if p[0] == d[0]:
            cow = cow + 1
            bulk = bulk - 1
        if p[1] == d[1]:
            cow = cow + 1
            bulk = bulk - 1
        if p[2] == d[2]:
            cow = cow + 1
            bulk = bulk - 1
        if p[3] == d[3]:
            cow = cow + 1
            bulk = bulk - 1
    return [cow, bulk, False]




if __name__=="__main__":
    game()

