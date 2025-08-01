a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a>b:
    print(f"{a} is larger.")
else:
    print(f"{b} is larger.")

if a>0:
    print(f"{a} is positive.")
elif a<0:
    print(f"{a} is negative.")
else:
    print("The number is zero.")

if b>0:
    print(f"{b} is positive.")
elif b<0:
    print(f"{b} is negative.")
else:
    print("The number is zero.")