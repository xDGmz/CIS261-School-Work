def getEmpName():
    empName = input("Enter employee name: ")
    return empName
    
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

def printinfo(empName, hours, hourlyRate,gPay, taxRate, incomeTax, netPay):
    print(empName, f"{hours:,.2f}",  f"{hourlyRate:,.2f}", f"{gPay:,.2f}",  f"{taxRate:,.1%}",  f"{incomeTax:,.2f}",  f"{netPay:,.2f}")

def PrintTotals(totalEmployees, totalHours, totalGrossPay, totalTax, totalNetPay):    
    print(f"\nTotal Number Of Employees: {totalEmployees}")
    print(f"Total Hours: {totalHours:,.2f}")
    print(f"Total Gross Pay: {totalGrossPay:,.2f}")
    print(f"Total Tax: {totalTax:,.2f}")
    print(f"Total Net Pay: {totalNetPay:,.2f}")

if __name__ == "__main__":
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    while True:
        empName = getEmpName()
        if (empName.upper() == "END"):
            break
        hours = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        gPay, incomeTax, netPay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
        
        printinfo(empName, hours, hourlyRate, gPay, taxRate, incomeTax, netPay)
        
        totalEmployees += 1
        totalHours += hours
        totalGrossPay += gPay
        totalTax += incomeTax
        totalNetPay += netPay

    PrintTotals (totalEmployees, totalHours, totalGrossPay, totalTax, totalNetPay)