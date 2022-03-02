#odd even between a given range
s=int(input("Enter the starting point of the range-"))
e=int(input("ENter the end point of the range- "))
for num in range(s,e+1):
    if num %2 == 0:
        print("\n even no -",num,end = " ")
    else: print("\n odd no -",num,end="")
    

