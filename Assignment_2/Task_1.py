#to check whether the input number is odd or even
num1 = input("Enter the Number: ")
num_int=int(num1)
if num_int % 2 == 0:
    print(f"{num1} is even")
else:
    print(f"{num1} is odd")