def main():
    # Str Variable Definition
    factRes = "Factoral results using"
    itFun = "an iterative function"
    recFun = "a recursive funciton"
    # Header
    print(f"{factRes} {itFun} vs {recFun}")
    # Recursive Function
    print(f"{factRes} {recFun}")
    print("0! =", factRecursive(0))
    print("5! =", factRecursive(5))
    print("10! =", factRecursive(10))
    print("25! =", factRecursive(25))
    print("50! =", factRecursive(50))
    print("100! =", factRecursive(100))
    # Iterative Function
    print(f"{factRes} {itFun}")
    print("0! =", factIterate(0))
    print("5! =", factIterate(5))
    print("10! =", factIterate(10))
    print("25! =", factIterate(25))
    print("50! =", factIterate(50))
    print("100! =", factIterate(100))
def factIterate(num):
    factorial = 1
    for number in range(2,num+1):
        factorial = number * factorial
    return factorial
def factRecursive(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factRecursive(num-1)

if __name__ == "__main__":
    main()
# 1 Write an iterative function that calculates the factorial for a number passed into the function using a for loop.
# 2 Write a recursive function that calculates the factorial for the same number passed into the iterative function.
# 3 Call each function from a print statement five times, using the numbers shown in the sample screen shot.
