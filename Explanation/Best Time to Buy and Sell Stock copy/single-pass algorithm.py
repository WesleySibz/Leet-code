"""
Single-Pass Algorithm Explanation
The single-pass algorithm is designed to find the maximum profit from buying and selling a stock given an array of prices. 
The algorithm ensures that the solution is found in a single traversal of the array, achieving a time complexity of O(n).

Steps
Initialize Variables:
min_price to a very high value (infinity) to keep track of the minimum price encountered so far.

max_profit to 0 to keep track of the maximum profit encountered so far.

Iterate Through Prices:
For each price in the array:
Update min_price to be the minimum of the current min_price and the current price.

Calculate the potential profit by subtracting the current price from min_price.

Update max_profit to be the maximum of the current max_profit and the potential profit.

Return the Result:
Return max_profit.

Implementation
Here's the implementation in Python:
"""

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

"""
Explanation
Initialize Variables:
min_price is initialized to infinity to ensure that any price in the array will be less than this initial value.

max_profit is initialized to 0 because the minimum profit is 0 (no transaction).

Iterate Through Prices:
For each price in the array:
If the current price is less than min_price, update min_price to the current price.

If the potential profit (current price - min_price) is greater than max_profit, update max_profit to the potential profit.

Return the Result:
After iterating through all the prices, return max_profit.


Example Usage
Example 1:
Input: prices = [7, 1, 5, 3, 6, 4]

Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.

Example 2:
Input: prices = [7, 6, 4, 3, 1]

Output: 0

Explanation: In this case, no transactions are done and the max profit = 0.

Constraints
1 <= prices.length <= 105

0 <= prices[i] <= 104

Summary
The single-pass algorithm efficiently calculates the maximum profit by maintaining the minimum price encountered so far 
and updating the maximum profit based on the current price. 
This approach ensures that the solution is found in linear time, making it suitable for large input sizes.
"""