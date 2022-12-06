def main():
    print("The Fibonacci Series for 16")
    for i in range(16):
        print(fibonacci(i), end=", ")
    print("...")

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    main()

# Create a function to calculate and return the Fibonacci series for the number 16
