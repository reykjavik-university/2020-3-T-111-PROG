PROMPT = 'Would you like to continue (y/n)? '

print("Welcome to car rentals!")
answer = input(PROMPT)

while (answer == 'y'):
    code = input("Customer code (b or d): ")
    days = int(input("Number of days: "))
    start = int(input("Odometer reading at the start: "))
    end = int(input("Odometer reading at the end: "))
    miles = end - start
    
    if code == 'b':
        due = 40.0*days + 0.25*miles
    elif code == 'd':
        miles_per_day = miles/days
        due = 60.0*days
        if miles_per_day > 100: # $0.25 for each mile dreiven above the 100 mile per day limit
            due += 0.25*(miles-100*days)

    print("Miles driven:", miles)            
    print("Amount due:", round(due,1))

    answer = input(PROMPT)