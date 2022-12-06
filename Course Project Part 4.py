import datetime
import getpass

emplFile = "empl.txt"
dateFormat = "%m/%d/%Y"
userFile = "users.txt"

def getEmpName():
    empName = input("Enter employee name: ")
    return empName

def getDatesWorked():
    fromValid = False
    toValid = False
    while not fromValid:
        try:
            fromDate = input("Please enter start date in the following format MM/DD/YYYY: ")
            dateObject = datetime.datetime.strptime(fromDate, dateFormat)
            fromValid = True
        except ValueError:
            print("Incorrect Date Format. Should be MM/DD/YYY")
    while not toValid:
        try:
            endDate = input("Please enter end date in the following format MM/DD/YYYY: ")
            dateObject = datetime.datetime.strptime(fromDate, dateFormat)
            toValid = True
        except ValueError:
            print("Incorrect Date Format. Should be MM/DD/YYY")
    return fromDate, endDate
    
def getHoursWorked():
    hours = float(input("Enter Hours: "))
    return hours

def getHourlyRate():
    hourlyRate = float(input("Enter Hourly Rate: "))
    return hourlyRate

def getTaxRate():
    taxRate = float(input("Enter Tax Rate: "))
    taxRate = taxRate / 100
    return taxRate

def CalcTaxAndNetPay(hours, hourlyRate, taxRate):
    gPay = hours * hourlyRate
    incomeTax = gPay * taxRate
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay

def printInfo(DetailsPrinted):
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    openFile = open(emplFile, "r")
    while True:
        rundate = input ("Enter start date for report (MM/DD/YYYY) or All for all data in file: ")
        if (rundate.upper() == "ALL"):
            print("\n")
            break
        try:
            rundate = datetime.strptime(rundate, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Try again.\n")
            continue
    while True:
        empDetail = openFile.readline()
        if not empDetail:
            break
        empDetail = empDetail.replace("\n", "")
        empList = empDetail.split("|")
        fromdate = empList[0]
        if (str(rundate).upper() != "ALL"):
            checkdate = datetime.strptime(fromdate, "%m/%d/%Y")
            if (checkdate < rundate):
                continue
        todate = empList[1]
        empname = empList[2]
        hours = float(empList[3])
        hourlyrate  = float(empList[4])
        taxrate = float(empList[5])
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")
        totalEmployees += 1
        totalHours += hours
        totalGrossPay += grosspay
        totalTax += incometax
        totalNetPay += netpay
        empTotals["totEmp"] = totalEmployees
        empTotals["totHours"] = totalHours
        empTotals["totGross"] = totalGrossPay
        empTotals["totTax"] = totalTax
        empTotals["totNet"] = totalNetPay
        DetailsPrinted = True   
    if (DetailsPrinted):
        printTotals(empTotals)
    else:
        print("No detail information to print")

def printTotals(empTotals):
    print(f'\nTotal Number Of Employees:  {empTotals["totEmp"]}')
    print(f'Total Hours Worked:           {empTotals["totHours"]:,.2f}')
    print(f'Total Gross Pay Of Employees: {empTotals["totGross"]:,.2f}')
    print(f'Total Tax Of Employees:       {empTotals["totTax"]:,.2f}')
    print(f'Total Net Pay Of Employees:   {empTotals["totNet"]:,.2f}')

def getUser():
    user = input("Enter username or 'end' to quit: ")
    return user

def getPassword():
    password = getpass.getpass()
    return password

def getRole():
    role = input("Enter role (Admin or User): ")
    while True:
        if role.lower() == "admin" or role.lower() == "user":
            return role
        else:
            role = input("Enter role (Admin or User): ")

def printUser():
    openFile = open(userFile, "r")
    while True:
        userDetail = openFile.readline()
        if not userDetail:
            break
        userDetail = userDetail.replace("\n", "")
        userList = userDetail.split("|")
        user = userList[0]
        password = userList[1]
        role = userList[2]
        print(f"\nUsername: {user}\nPassword: {password}\nRole: {role}")

def createUser():
    print("##### CREATE USERS, PASSWORDS, AND ROLES #####")
    openFile = open(userFile, "a+")
    while True:
        user = getUser()
        if user.lower() == "end":
            break
        password = getPassword()
        role = getRole()
        userDetail = user + "|" + password + "|" + role + "\n"
        openFile.write(userDetail)
    openFile.close()
    printUser()

def login():
    openFile = open(userFile, "r")
    userList = []
    user = input ("Enter User Name: ")
    role = "None"
    while True:
        userDetail = openFile.readline()
        if not userDetail:
            return user, role
        userDetail = userDetail.replace("\n", "")
        userList = userDetail.split("|")
        if user == userList[0]:
            role = userList[2]
            return user, role
    return user, role

if __name__ == "__main__":
    createUser()
    print("\n##### DATA ENTRY #####")
    role, user = login()
    DetailsPrinted = False
    empTotals = {}
    if role.lower() == "none":
        print(f"{user} is invalid.")
    else:
        if role.lower() == "admin":
            openFile = open(emplFile, "a+")
            while True:
                empName = getEmpName()
                if (empName.lower() == "end"):
                    break
                fromDate, endDate = getDatesWorked()
                hours = getHoursWorked()
                hourlyRate = getHourlyRate()
                taxRate = getTaxRate()
                empDetail = fromDate + "|" + endDate + "|" + empName + "|" + str(hours) + "|" + str(hourlyRate) + "|" + str(taxRate) + "\n"
                openFile.write(empDetail)
            openFile.close()
        printInfo(DetailsPrinted)
