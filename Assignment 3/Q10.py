gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

if gender == "male":
    if age >= 21:
        print("Person is eligible to marry")
    else:
        print("Person is not eligible to marry")

elif gender == "female":
    if age >= 18:
        print("Person is eligible to marry")
    else:
        print("Person is not eligible to marry")

else:
    print("Invalid gender")