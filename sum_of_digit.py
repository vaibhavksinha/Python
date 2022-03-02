from pyparsing import null_debug_action

no =int(input("Enter a number -"))
sum=0
temp=no
while no>0:
    digit = temp % 10
    sum+=digit
    temp//=10
print("sum of the digits -",sum)
