n = int(input('Enter number of passenger:'))
ticket = int(input('Enter ticket cost:'))

total = 0

for i in range(n):
    age = int(input('Enter age:'))

    if age < 12:
        amount = ticket - (ticket * 30 / 100)
    elif age > 59:
        amount = ticket (ticket * 50 / 100) 
    else:
        amount = ticket
        total = total + amount
    print('Total ticket amount:', total)             
