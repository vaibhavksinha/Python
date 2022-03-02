#armstrong no between 1 and 1000
from pyparsing import null_debug_action

no = int(input("enter a no to find the Armstrog no"))
sum=0
temp=no
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if no==sum:
    print("the no",no," is an Armstrong number")
else:
    print("the no",no,"is not an Armstrong number")

