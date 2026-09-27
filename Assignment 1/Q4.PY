#write a program to enter P ,T ,R and calculate simple intrest

p =  int(input("Enter the principal:"))
R = int(input("Enter the rate:"))
T = int(input("Enter the time:"))

#calcute the simple intrest

SI = (p* T * R) / 100

#display result
print("simple intrest:", SI)