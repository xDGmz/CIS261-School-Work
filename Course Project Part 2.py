def getEmpName():
    empName = input("Enter employee name: ")
    return empName

def getDatesWorked():
    #Prompt the user for the dates in the following format: mm/dd/yyyy
    fromDate = input("Please enter start date in the following format MM/DD/YYYY: ")
    endDate = input("Please enter end date in the following format MM/DD/YYYY: ")
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

def printTotals(empTotals):
    print(f'Total Number Of Employees:    {empTotals["totEmp"]}')
    print(f'Total Hours Of Employees:     {empTotals["totHours"]}')
    print(f'Total Gross Pay Of Employees: {empTotals["totGross"]}')
    print(f'Total Tax Of Employees:       {empTotals["totTax"]}')
    print(f'Total Net Pay Of Employees:   {empTotals["totNet"]}')

if __name__ == "__main__":
    empDetailList = []
    empTotals = {}
    while True:
        empName = getEmpName()
        if (empName.lower() == "end"):
            break
        fromDate, endDate = getDatesWorked()
        hours = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        empDetail = []
        empDetail.insert(0, fromDate)
        empDetail.insert(1, endDate)
        empDetail.insert(2, empName)
        empDetail.insert(3, hours)
        empDetail.insert(4, hourlyRate)
        empDetail.insert(5, taxRate)
        empDetailList.append(empDetail)
    printInfo(empDetailList)
    printTotals(empTotals)



#def printinfo(empName, hours, hourlyRate,gPay, taxRate, incomeTax, netPay):
#    print(empName, f"{hours:,.2f}",  f"{hourlyRate:,.2f}", f"{gPay:,.2f}",  f"{taxRate:,.1%}",  f"{incomeTax:,.2f}",  f"{netPay:,.2f}")

#def PrintTotals(totalEmployees, totalHours, totalGrossPay, totalTax, totalNetPay):    
#    print(f"\nTotal Number Of Employees: {totalEmployees}")
#    print(f"Total Hours: {totalHours:,.2f}")
#    print(f"Total Gross Pay: {totalGrossPay:,.2f}")
#    print(f"Total Tax: {totalTax:,.2f}")
#    print(f"Total Net Pay: {totalNetPay:,.2f}")

# if __name__ == "__main__":
#     #totalEmployees = 0
#     #totalHours = 0.00
#     #totalGrossPay = 0.00
#     #totalTax = 0.00
#     #totalNetPay = 0.00
#     while True:
#         empName = getEmpName()
#         if (empName.upper() == "END"):
#             break
#         hours = getHoursWorked()
#         hourlyRate = getHourlyRate()
#         taxRate = getTaxRate()
#         gPay, incomeTax, netPay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
        
#         printinfo(empName, hours, hourlyRate, gPay, taxRate, incomeTax, netPay)
        
#         totalEmployees += 1
#         totalHours += hours
#         totalGrossPay += gPay
#         totalTax += incomeTax
#         totalNetPay += netPay

#     PrintTotals (totalEmployees, totalHours, totalGrossPay, totalTax, totalNetPay)