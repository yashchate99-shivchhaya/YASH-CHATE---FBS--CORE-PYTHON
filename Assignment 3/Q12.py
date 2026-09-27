# write a program to check if given 3 digit number is a pallindrome or not

num = int(input("Enter a 3 digit number: "))

temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
    