import math
def main():
    function = input("What function would you like? ").lower()

    #Add
    if function == "addition" or function == "add" or function == "+":
        a = int(input("What numbers do you want to add? "))
        b = int(input("and? "))
        print(a + b)

    #Subtract
    elif function == "subtract" or function == "-":
        a = int(input("What numbers do you want to subtract? "))
        b = int(input("and? "))
        print (a - b)
   
    #Multiply
    elif function == "multiply" or function == "mult" or function == "x" or function == "*":
        a = int(input("What numbers do you want to multiply? " ))
        b = int(input("times? "))
        print (a * b)

    #Divide
    elif function == "divide" or function == "div" or function == "/":
        a = int(input("What number do you want to divide? "))
        b = int(input("by? "))
        print (float(a/b))

    #Square
    elif function == "sqr" or function == "square":
        n = int(input("What number do you want squared? "))
        print(n, "squared is", square(n))

    #Cube
    elif function == "cube" :
        n = int(input("What number do you want cubed? "))
        print(n, "cubed is", cube(n))

    #Power
    elif function == "^" or function == "pow":
        a = int(input("What number do you want to raise to a power? "))
        b = int(input("to the power of? "))
        print(power(a,b))

    #Quadratic Formula
    elif function == "qf" or function == "quadratic":
      a,b,c = abc()

      d = b**2 - 4*a*c
      if d < 0:
         print ("no real roots")
      else:
         print("Your values for x are ",  quadratic1(a,b,c), "and ",  quadratic2(a,b,c))
      
def square(n):
    return pow(n,2)

def cube(n):
    return pow(n,3)

def power(a,b):
    return pow(a,b)

def quadratic1(a,b,c):
    return float(-b + math.sqrt(pow(b,2) - 4*a*c)) / (2*a)

def quadratic2(a,b,c):
    return float(-b - math.sqrt(pow(b,2) - 4*a*c)) / (2*a)

def abc():
      a = int(input("What is a? "))
      b = int(input("What is b? "))
      c = int(input("What is c? "))
      return a,b,c

main()





#input does the print function while assigning in this case "name" to the input
#name = name.strip().title(), you can tack everything onto the assignment, makes it cleaner

#name = input("whats your name? ").strip().title()
#.split("") splits and assigns different strings between spaces
#first, last = name.split(" ")
#print ("Hello,", name)

#.title() capitalizes words like its a title
#.strip() removes all the whitespace on the left and right
#dob = input("Whats your date of birth? ")

#print ("Hello, ", name, "\n","DOB:", dob)

#backslash before the quotation makes it not affect the outside quotes
#print ("Hello, \"Friend\"")

#x = float(input("What is x? "))
#y = float(input("What is y? "))

#z = round(x+y)
#print (f"{z:,}")

#a = round(x/y, 2)
#print (a)
#print ("Addition: ", x+y)
#print ("Subtraction: ", x-y)
#print ("Multiplication: ", x*y)
#print ("Division: ", x/y)
#int for integer, float for decimal points



