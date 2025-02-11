class Solution:
    def max_profit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit

# Example usage:
solution = Solution()

prices1 = [7, 1, 5, 3, 6, 4]
print(solution.max_profit(prices1))  # Output: 5

prices2 = [7, 6, 4, 3, 1]
print(solution.max_profit(prices2))  # Output: 0