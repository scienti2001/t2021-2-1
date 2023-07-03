class Calculator:   #Class creation
    def __init__(self, a, b):   #Intilization of class
        self.a = a
        self.b = b
    def add(self):    #Addition
        return self.a + self.b
    def subtract(self): #substraction
        return self.a - self.b
    def multiply(self): #Multiplication
        return self.a * self.b
    def divide(self):  #Division
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: Division by zero"
#Inputs
a = float(input("Enter the value of a"))
b = float(input("Enter the value of b"))
op = input("Enter the type of operator (+, -, *, /)")

# Instance creation for calculator
cal = Calculator(a, b)

# Operations to be performed
if op == '+':
    result = cal.add()
elif op == '-':
    result = cal.subtract()
elif op == '*':
    result = cal.multiply()
elif op == '/':
    result = cal.divide()
else:
    result = "Error: Invalid operator"

#Result Display
print("Result:",str(round(result,6)))