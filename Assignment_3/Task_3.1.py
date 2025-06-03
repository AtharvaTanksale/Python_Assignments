def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)
num = (int(input("Enter the number: ")))
result =factorial(num)
print(f"the factorial of {num} is {result}")
