import datetime

fileName = "empl.txt"
dateFormat = "%m/%d/%Y"

def writeEmpl(emplInfo):
    with open (fileName, "w+") as outfile:
        for list in emplInfo:
            outfile.write(f"{list} | ")

def getEmpName():
    empName = input("Enter employee name: ")
    return empName

def getDatesWorked():
    #Prompt the user for the dates in the following format: mm/dd/yyyy
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

def printInfo(empDetailList):
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    with open(fileName) as file:
        for line in file:
            line = line.replace("\n", "")
            EmpFile.append(line)
    while True:
        rundate = input ("Enter start date for report (MM/DD/YYYY) or All for all data in file: ")
        if (rundate.upper() == "ALL"):
            break
        try:
            rundate = datetime.strptime(rundate, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Try again.")
            print()
            continue
    while True:
        EmpFile = empDetail
        if not empDetail:
            break
        fromdate = empList[0]
        if (str(rundate).upper() != "ALL"):
            checkdate = datetime.strptime(fromdate, "%m/%d/%Y")
            if (checkdate < rundate):
                continue
        for empList in empDetailList:
            fromDate = empList[0]
            endDate = empList[1]
            empName = empList[2]
            hours = empList[3]
            hourlyRate = empList[4]
            taxRate = empList[5]

            grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
            print(fromDate, endDate, empName, f"{hours:,.2f}",  f"{hourlyRate:,.2f}", f"{grosspay:,.2f}",  f"{taxRate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")
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

    if (empDetailList):
        printTotals(empTotals)
    else:
        print("No Detail Information to print")

def printTotals(empTotals):
    print(f'Total Number Of Employees:    {empTotals["totEmp"]}')
    print(f'Total Hours Of Employees:     {empTotals["totHours"]}')
    print(f'Total Gross Pay Of Employees: {empTotals["totGross"]}')
    print(f'Total Tax Of Employees:       {empTotals["totTax"]}')
    print(f'Total Net Pay Of Employees:   {empTotals["totNet"]}')

if __name__ == "__main__":
    EmpFile = []
    empDetailList = []
    empDetail = []
    empTotals = {}
    with open(fileName) as file:
       for line in file:
           line = line.replace("\n", "")
           EmpFile.append(line)
    while True:
        empName = getEmpName()
        if (empName.lower() == "end"):
            break
        fromDate, endDate = getDatesWorked()
        hours = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        empDetail = []
        empDetail.insert(0, empName)
        empDetail.insert(1, fromDate)
        empDetail.insert(2, endDate)
        empDetail.insert(3, hours)
        empDetail.insert(4, hourlyRate)
        empDetail.insert(5, taxRate)
        empDetailList.append(empDetail)
        writeEmpl(empDetailList)
        
    printInfo(empDetailList)
    printTotals(empTotals)
