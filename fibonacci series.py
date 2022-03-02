# Fibonacci series
no =int(input("enter the number of fibonacci series- "))
start=0
second=1
count=1 
print("fibonacci series between ",no,"is- \t")
for count in range(start,no+1):
    sum=start+second
    start=second
    second=sum
    print(sum)
    