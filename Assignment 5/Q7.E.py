x = int(input("Enter x: "))
n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    term = x ** i
    denominator = 2 * i - 1

    if i % 2 == 1:
        sum = sum + term / denominator
    else:
        sum = sum - term / denominator

print("Sum =", sum)