def armstrong(num):
    temp = num
    sum = 0
    digits = len(str(num))

    while num > 0:
        digit = num % 10
        sum = sum + digit ** digits
        num = num // 10

    if sum == temp:
        return "Armstrong Number"
    else:
        return "Not an Armstrong Number"


num = int(input("Enter number: "))

print(armstrong(num))