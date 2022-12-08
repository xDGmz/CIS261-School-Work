def disMenu():
    print("The Vaughn Family Country Code List Program\n")
    print("COMMAND MENU")
    print("LS - List all Country codes")
    print("ADD  - Add a Country code")
    print("DEL  - Delete a Country code")
    print("EXIT - Exit program\n")

def disCodes(countryList):
    codes = list(countryList.keys())
    codes.sort()
    codes_line = "Country codes: "
    for code in codes:
        codes_line += code + " "
    print(codes_line)

def disCountry(countryList):
    disCodes(countryList)
    code = input("Enter country code: ")
    code = code.upper()
    if code in countryList:
        name = countryList[code]
        print(f"Country name: {name}.\n")
    else:
        print("There is no country with that code.\n")

def addCountry(countryList):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countryList:
        name = countryList[code]
        print(f"{name} is already using this code.\n")
    else:
        name = input("Enter country name: ")
        name = name.title()
        countryList[code] = name
        print(f"{name} was added.\n")

def delCountry(countryList):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countryList:
        name = countryList.pop(code)
        print(f"{name} was deleted.\n")
    else:
        print("There is no country with that code.\n")

def main():
    countryList = {"CA" : "Canada",
                 "US" : "United States",
                 "MX" : "Mexico",
                 "NO" : "Norway",
                 "DK" : "Denmark"}
    
    disMenu()
    while True:        
        command = input("Command: ")
        command = command.lower()
        if command.lower() == "ls" or command.lower() == "list":
            disCountry(countryList)   
        elif command == "add":
            addCountry(countryList)
        elif command.lower() == "del" or command.lower() == "delete":
            delCountry(countryList)  
        elif command.lower() == "exit" or command.lower() == "quit":
            print("Goodbye!")
            print("Ha det!")
            print("Auf wiedersehen!")
            break
        else:
            print(f" {command} is not a valid command. Please try again.\n")

main()
