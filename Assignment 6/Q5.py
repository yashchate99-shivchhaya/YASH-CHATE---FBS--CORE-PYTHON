for i in range(1, 6):
    # spaces
    for j in range(1, 6 - i):
        print(" ", end=" ")

    # stars
    for j in range(1, 2 * i):
        print("*", end=" ")

    print()