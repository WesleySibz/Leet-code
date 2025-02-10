class Solution:
    def add_binary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            carry = total // 2
            result.append(str(total % 2))
        
        return ''.join(result[::-1])

# Example usage:
solution = Solution()

a1 = "11"
b1 = "1"
print(solution.add_binary(a1, b1))  # Output: "100"

a2 = "1010"
b2 = "1011"
print(solution.add_binary(a2, b2))  # Output: "10101"