
def divdide(a, b):
    if a < 0 or b < 0:
        return "Error: Negative numbers are not allowed"
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b