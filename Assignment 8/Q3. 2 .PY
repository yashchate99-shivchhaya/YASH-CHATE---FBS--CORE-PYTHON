def factorial_sum(n):
    sum = 0
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i
        sum = sum + fact
    return sum
print(factorial_sum(5))    