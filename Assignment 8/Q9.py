def pallindrome(n):
    temp = n
    rev = 0


    while n > 0:
        d = n % 10
        rev = rev * 10 + d
        n = n // 10

    if temp == rev:
        print('pallindrome number')    
    else:
        print('not a pallindrome number')

n = int(input('enter number:'))

pallindrome(n)            
       