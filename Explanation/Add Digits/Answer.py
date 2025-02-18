def addDigits(self, num: int) -> int:
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9

# Example usage:
print(addDigits(38))  # Output: 2
print(addDigits(0))   # Output: 0