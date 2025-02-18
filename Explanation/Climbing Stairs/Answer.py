class Solution:
    def climb_stairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

# Example usage:
solution = Solution()

n1 = 2
print(solution.climb_stairs(n1))  # Output: 2

n2 = 3
print(solution.climb_stairs(n2))  # Output: 3