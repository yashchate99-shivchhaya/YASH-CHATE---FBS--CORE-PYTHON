#program to find roots of a quadratic equation
a = float(input("Enter value of a :"))
b = float(input("Enter value of b :"))
c = float(input("Enter value of c :"))


#ax **2 + bx +c = 0 is quadratic equation

#for findings its root D = b**2 - 4*a*c

D = b**2 - 4*a*c

#taking 2 roots for both cases of + and -

root1 = (-b + D**0.5)/ (2*a)
root2 = (-b - D**0.5) / (2*a)

print("Root 1:", root1)
print("Root 2:", root2)