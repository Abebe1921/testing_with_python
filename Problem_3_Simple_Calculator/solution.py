#simple calculator
num1=int(input("Enter the first number:"))
opp=input("oprator: ")
num2=int(input("Enter the second number: "))
if opp=='+':
    result=num1+num2
    print(f"The sum of the numbers are:",result)
elif opp=='-':
    result=num1-num2
    print(f"The diverence of the numbers are:",result)
elif opp=='/':
    if num2!=0:
        result=num1/num2
        print(f"The diviion of the numbers are:",result)
    elif num2 ==0: #We can not divided by 0. 
        print("Any number divisible by 0 is imposible.")
elif opp=='*':  
    result=num1*num2
    print(f"The multiplication of the numbers are:",result)
