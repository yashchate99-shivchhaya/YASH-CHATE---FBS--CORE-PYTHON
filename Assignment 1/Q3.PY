#program to find quotient and remainder of two numbers

num1 = int(input('Enter the first number :'))
num2 = int(input('Enter the second number :'))


#quotient we taking floor division
quotient = num1 // num2

#remainder we taking modulus
remainder = num1 % num2 

#display result sepratly for the quotient and remainder
print('quotient :', quotient)
print('Remainder :', remainder)