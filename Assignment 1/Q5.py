#write a program to enter P, T, R and calculate the compound intrest

P = float(input("Enter Principal (P): "))
R = float(input("Enter Rate (R): "))
T = float(input("Enter Time (T): "))

#Formula of compound intrest
A = P * (1 + R / 100) ** T 
CI = A - P

#display result
#print("Compound Interest =", CI)
print("Amount =", A)