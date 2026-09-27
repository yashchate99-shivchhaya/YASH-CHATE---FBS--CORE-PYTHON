sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub4 = float(input("Enter marks of Subject 4: "))
sub5 = float(input("Enter marks of Subject 5: "))

#obtained marks
total = sub1 + sub2 + sub3 + sub4 + sub5


#percentage
percentage = (total / 500) * 100



#display result
print("Total Marks =", total)
print("Percentage =", percentage, "%")