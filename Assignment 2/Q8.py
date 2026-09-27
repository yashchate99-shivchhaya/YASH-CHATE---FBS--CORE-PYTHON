#write a program to swap two numbers using third variable
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

temp = a
a = b
b = temp

# display result
print("After swpping")
print("a :=", a)
print('b :=', b)