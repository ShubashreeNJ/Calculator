num1=float(input("enter a num1:"))
num2=float(input("enter a num2:"))
operator=input("enter an operator:")

match operator:
    case '+':
        result=num1+num2
    case '-':
        result=num1-num2
    case '*':
        result=num1*num2
    case '/':
        if (num2==0):
            print("Division by zero impossible")
            result=None
        else:
            result=num1/num2
    case '**':
        result=num1**num2
    case '//':
        result=num1//num2
    case _:
        print("invalid operator")
        result=None

print(f"{num1} {operator} {num2}= {result}")