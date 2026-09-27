def sum_digits(n):
    sum = 0

    while n > 0:
        d = n % 10
        sum = sum + d
        n = n // 10

    print('sum of digits=', sum)

n  = int(input('enter number:'))

sum_digits(n)