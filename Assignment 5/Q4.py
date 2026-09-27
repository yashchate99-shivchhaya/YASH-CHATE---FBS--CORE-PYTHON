start = int(input("Enter start: "))
end = int(input("Enter end: "))

for n in range(start, end + 1):

    temp = n
    digits = len(str(n))
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** digits
        temp = temp // 10

    if sum == n:
        print(n)