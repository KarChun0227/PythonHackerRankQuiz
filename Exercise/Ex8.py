def winner(P1, P2):
    if P1 == P2:
        return 0
    elif P1 == "S":
        if P2 == "R":
            return 2
        else:
            return 1
    elif P1 == "R":
        if P2 == "S":
            return 1
        else:
            return 2
    elif P1 == "P":
        if P2 == "S":
            return 2
        else:
            return 1

while True:
    p1 = input("Player one:")
    p2 = input("Player two:")
    result = winner(p1,p2)
    if result == 0:
        print ("No Winner!!")
    elif result == 1:
        print ("Winner is Payer 1")
        if input("Wish to continue?") == "no":
            break
    elif result == 2:
        print ("Winner is Payer 2")
        if input("Wish to continue?") == "no":
            break



