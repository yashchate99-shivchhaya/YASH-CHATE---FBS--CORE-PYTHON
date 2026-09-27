#write a program to convert days into years, weeks and days
#input
days = int(input("Enter number of days:"))

#floor division
years = days // 365
remaining_days = days % 365

#floor division
week = remaining_days // 7
remaining_days = remaining_days % 7

#display result
print("years:", years)
print("weeks:", week)
print("days:", days)