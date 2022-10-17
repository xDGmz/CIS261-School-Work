def Title():
    print("Welcome to the Celsius to Fahrenheit converter (and Fahrenheit to Celsius converter)")

def fahrenheitC(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsiusF(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def Main():
    Title()
    for temp in range(0, 212, 40):
        print(temp, "Fahrenheit =", round(fahrenheitC(temp), 2),
              "Celsius")
    
    for temp in range(0, 100, 20):
        print(temp, "Celsius =", round(celsiusF(temp), 2),
              "Fahrenheit")
    ff = input("Would you like to hear a fun fact about the temperature? (Yes/No) ")
    if ff == "y" or ff == "yes":
        print("-40 is the same in Fahrenheit and in Celcius")

Main()