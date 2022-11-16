print("Invoice Line Item Calculator")

def inPrice():
    Valid = False
    global price
    while not Valid:
        try:
            price = float(input("Enter Price: "))
            Valid = True
        except ValueError:
            print("Invalid decimal number. Please try again.")
def inQty():
    Valid = False
    global qty
    while not Valid:
        try:
            qty = int(input("Enter Qty: "))
            Valid = True
        except ValueError:
            print("Invalid decimal number. Please try again.")
def qtyPrice():
    global totalPrice
    totalPrice = price * qty
def printTotals():
    print(f"Price:       ${price:,.2f}")
    print(f"Quantity:    {qty}")
    print(f"Total:       ${totalPrice:,.2f}")
cont = True
while cont:
    inPrice()
    inQty()
    qtyPrice()
    printTotals()
    contIn = input("Enter another line item? (y/n): ")
    if contIn.lower() == "y" or contIn.lower() == "yes":
        print("")
        cont = True
    elif contIn.lower() == "n" or contIn.lower() == "no":
        print("")
        cont = False
if not cont:
    print("Goodbye!")