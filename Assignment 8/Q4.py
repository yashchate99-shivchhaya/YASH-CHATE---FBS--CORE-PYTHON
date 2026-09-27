def odd_sum(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            sum = sum + i
    return sum
print(odd_sum(10))        