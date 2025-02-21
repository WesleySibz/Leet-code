class Solution:
    def title_to_number(self, column_title: str) -> int:
        result = 0
        
        for char in column_title:
            result = result * 26 + (ord(char) - ord('A') + 1)
        
        return result

# Example usage:
solution = Solution()

column_title1 = "A"
print(solution.title_to_number(column_title1))  # Output: 1

column_title2 = "AB"
print(solution.title_to_number(column_title2))  # Output: 28

column_title3 = "ZY"
print(solution.title_to_number(column_title3))  # Output: 701