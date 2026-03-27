# main.py
# Leader file: integrates all operations


def main():
    print("Welcome to the Calculator App!")
    
    # Example usage of all operations
    a = 10
    b = 5
    
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    print(f"{a} / {b} = {divide(a, b)}")

if __name__ == "__main__":
    main()