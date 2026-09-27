n = int(input("Enter n: "))

term = 1
sum = 0

for i in range(1, n + 1):
    sum = sum + term
    term = term * 2

print("Sum =", sum)