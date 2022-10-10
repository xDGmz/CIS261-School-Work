from datetime import datetime
import locale

# Set Locale
locale.setlocale(locale.LC_ALL, "en_US")

# Variables
    # Continue
cont = "y"
    # Today
today = datetime(datetime.now().year, datetime.now().month, datetime.now().day)
    # Arrival Date
arrivalDate = today
    # Departure Date
departDate = today
    # Rates
nRate = 85
hRate = 105
    # Messages
arrivalTooSoon = "Arrival Date must be earlier than todays date\n"
invalidFormat = "Invalid format, format must be YYYY-MM-DD\n"
departTooSoon = "Departure date must be set in the future \n"
RateMessage = "(High Season)"
header = "The Vaughns Hotel Reservation\n"
rateMessage = (f"The current nightly rate is: {locale.currency(nRate)}, except in august where it is {locale.currency(hRate)}")

# Print Header
print(header + rateMessage)

while cont.lower() == "y" or cont.lower() == "yes":
    # Arrival Date
    while True:
        # Input
        arrivalDateStr = input("Please enter your arrival date (Format must be YYYY-MM-DDD): ")
        # Error checking for formatting 
        try:
            arrivalDate = datetime.strptime(arrivalDateStr, "%Y-%m-%d")
        except ValueError:
            print(invalidFormat)
            continue
        # Error Checking for date
        if arrivalDate < today:
            print(arrivalTooSoon)
        else:
            break

    # Departure Date
    while True:
        # Input
        departDateStr = input("Please enter your departure date (Format must be YYYY-MM-DDD): ")
        # Error checking for formatting 
        try:
            departDate = datetime.strptime(departDateStr, "%Y-%m-%d")
        except ValueError:
            print(invalidFormat)
            continue
        # Error Checking for date
        if departDate <= arrivalDate:
            print(departTooSoon)
        else:
            break

    if arrivalDate.month == 8:
        rate = hRate
    else:
        rate = nRate
        RateMessage = ""
    stayTotal = (departDate - arrivalDate).days
    stayCost = rate * stayTotal

    # Print Results
    dateFormat = "%B %d, %y"
    print(f"Arrival Date:     {arrivalDate:{dateFormat}}")
    print(f"Departure Date:   {departDate:{dateFormat}}")
    print(f"Nightly Rate:     {locale.currency(rate)} {RateMessage}")
    print(f"Total Nights:     {stayTotal}")
    print(f"Total Price:      {locale.currency(stayCost)}\n")
    
    # Do you wish to continue?
    cont = input("Continue? (y/n): ")

print("Have a good day!")

# Display the output as shown in the sample screen shot
# Prompt the user to continue entering data
# The program must test all possible combinations of data entry
