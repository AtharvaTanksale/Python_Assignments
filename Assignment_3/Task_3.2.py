import  math
n=int(input("Enter the number: "))
#1:squareroot:
if n>= 0:
    squareroot = math.sqrt(n)
else:
    print("Cannot have square root of negative number")
#2:logarithm (n,base e)
if n >= 0:
    logarithm = math.log(n)
else:
    print("Cannot have log of negative number")
#3:sine value
sine_value = math.sin(n)

print(f"The squareroot  is {squareroot}")
print(f"The logarithm is {logarithm}")
print(f"The sine value is {sine_value}")
