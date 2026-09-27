m1 = int(input("Enter mark1:"))
m2 = int(input("Enter mark2:"))
m3 = int(input("Enter mark3:"))
m4 = int(input("Enter mark4:"))
m5 = int(input("Enter mark5:"))

total = m1 + m2 + m3 + m4 + m5

percentage = total / 5


if percentage >= 60:
    print("first class")
elif percentage >= 50:
    print("second class")
elif percentage >= 35:
    print("pass")
else:
    print('fail')    