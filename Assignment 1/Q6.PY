#write a program two angles from user and find third angle of the triangle
angle1 = float(input("Enter first angle:"))
angle2 = float(input("Enter second angle:"))

#sum of two angles - 180 degree is third angle
angle3 = 180 - (angle1 + angle2)

#display result
print("Third angle:", angle3)