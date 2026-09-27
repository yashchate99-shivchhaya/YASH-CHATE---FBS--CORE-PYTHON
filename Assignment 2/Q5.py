#take  input
cp = float(input("Enter cost price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = cp * discount / 100
sp = cp - discount_amount
#display result
print("Selling Price =", sp)