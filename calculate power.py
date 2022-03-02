po=0
while True:
    no =int(input("Enter the no of which power you want to find- "))
    power=int(input("Enter the power- "))
    po=no**power
    print(no,"to the power of",power,"= ",po)
    con=int(input("do you want to try again \n enter yes=1 & no=0?"))
    if con == 1:
        continue
    if con == 0:
        break