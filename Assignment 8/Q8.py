def reverse_number(n):
    rev = 0

    while n > 0:
        d = n % 10
        rev = rev * 10 + d
        n = n // 10

    print('reverse number:', rev)

n = int(input('enter number:')) 

reverse_number(n)