#convert the time entered in hh,min and sec into seconds.
#take input
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

total_seconds = (hours * 60 * 60) + (minutes * 60) + seconds

#display result
print("Total seconds =", total_seconds)