def odd_even(x,y):
    final_list = []
    for num1 in x:
        if num1 % 2 != 0:
            final_list.append(num1)
    for num2 in y:
        if num2 % 2 == 0:
            final_list.append(num2)
    return final_list

def add(x):
    numlist = x
    num = int(input("Give a number: "))
    if num in x:
        x.remove(num)
    x.insert(2,num)
    x.append(num)
    return numlist

if __name__ == "__main__":
    listOne = [3, 6, 9, 12, 15, 18, 21]
    listTwo = [4, 8, 12, 16, 20, 24, 28]
    print (add(listTwo))
