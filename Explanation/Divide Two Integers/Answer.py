class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit signed integer range
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        # Handle edge cases
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        if divisor == 0:
            raise ValueError("Divisor cannot be zero")
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive values
        dividend, divisor = abs(dividend), abs(divisor)
        
        # Initialize the quotient
        quotient = 0
        
        # Subtract divisor from dividend until dividend is less than divisor
        while dividend >= divisor:
            temp_divisor, num_divisors = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                num_divisors <<= 1
            dividend -= temp_divisor
            quotient += num_divisors
        
        # Apply the sign to the quotient
        if negative:
            quotient = -quotient
        
        # Ensure the quotient is within the 32-bit signed integer range
        return max(MIN_INT, min(MAX_INT, quotient))

# Example usage:
solution = Solution()

dividend1 = 10
divisor1 = 3
print(solution.divide(dividend1, divisor1))  # Output: 3

dividend2 = 7
divisor2 = -3
print(solution.divide(dividend2, divisor2))  # Output: -2