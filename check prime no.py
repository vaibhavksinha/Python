no= int(input("enter a number to find if its a prime no or not- "))
if no>1:
    for i in range(2,no):
       if no % i == 0:
           print("the no",no," is not a prime no😢")
           break
    else:
        print("The no ",no,"is a prime no😁")
else:
    print("the no",no," is not a prime no😢")

