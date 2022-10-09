inDate = input("Please enter Date: ")
while inDate != -1:
    splitDate = inDate.split()
    monthDate = splitDate[0]
    if monthDate == "January":
        monthNumber = 1
    elif monthDate == "Febuary":
        monthNumber = 2
    elif monthDate == "March":
        monthNumber = 3
    elif monthDate == "April":
        monthNumber = 4
    elif monthDate == "May":
        monthNumber = 5
    elif monthDate == "June":
        monthNumber = 6
    elif monthDate == "July":
        monthNumber = 7
    elif monthDate == "August":
        monthNumber = 8
    elif monthDate == "September":
        monthNumber = 9
    elif monthDate == "October":
        monthNumber = 10
    elif monthDate == "November":
        monthNumber = 11
    elif monthDate == "December":
        monthNumber = 12
    else:
        monthNumber = 0
    if len(splitDate) >= 3 and monthNumber != 0 :
        outDate = splitDate[1]
        if outDate[len(outDate) -1] == ',':
            outDate = outDate[0:len(outDate) -1]
            year = splitDate[2]
            print(str(monthNumber)+'/'+outDate+'/'+str(year))
        else:
            print("Date entered is not valid")
    else:
        print("Date entered is not valid")
    inDate = input("Please Enter date: ")