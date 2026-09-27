def fibonacci(n):
    a = 1
    b = 1

    for i in range(n):
        print(a, end = ' ')
        c = a + b
        a = b
        b = c


n = int(input('enter number of terms:'))

fibonacci(n)


