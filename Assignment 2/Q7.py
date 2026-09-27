#find the sum of the three digit number
num = int(input("Enter a three digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

#perform addition
sum = a + b + c

#display result
print("Sum of digits =", sum)