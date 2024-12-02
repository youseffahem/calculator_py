'''
Write a program that acts as a simple calculator using a
switch-case statement. The program should take two numbers and an
operator (+, -, *, /) as input.
Use a switch-case on the operator to perform the corresponding
calculation (addition, subtraction, multiplication, division).
Include error handling for invalid operators or attempting to
divide by zero.
'''

num1=float(input("Enter the first number : "))
op=str(input("(chose +, -, *, /) : "))
num2=float(input("Enter the secound number : "))

sum =num1+num2
sub= num1-num2
mult=num1*num2


match op:
    case "+":
        print(f"{num1}+{num2}={sum}")    
    case "-":
        print(f"{num1} - {num2} = {sub}")            
    case "*":
        print(f"{num1} * {num2} = {mult}")            
    case "/":
        if num2 == 0:
            print("invalid")
        else:
            result = num1/num2
        print(f"{num1} / {num2} = {result}")            
            
    case _:
        print("Error")
  
    
