num = int(input("Enter a number: "))
total = 0
    ##sum
for i in range(1, num+1):
    total += i

print("Sum =", total)

### multiplication table
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")


### vowels count
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in s:
    if char in vowels:
        count += 1

print(f"Number of vowels in '{s}': {count}")