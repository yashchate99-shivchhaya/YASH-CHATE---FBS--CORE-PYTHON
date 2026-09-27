n = int(input("Enter number of students: "))

total_percentage = 0

for i in range(1, n + 1):
    print("Student", i)

    m1 = float(input("Enter marks 1: "))
    m2 = float(input("Enter marks 2: "))
    m3 = float(input("Enter marks 3: "))
    m4 = float(input("Enter marks 4: "))
    m5 = float(input("Enter marks 5: "))

    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    print("Percentage =", percentage)

    total_percentage = total_percentage + percentage

average = total_percentage / n

print("Average Percentage =", average)