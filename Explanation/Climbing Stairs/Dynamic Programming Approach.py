"""
Dynamic Programming Approach
Dynamic programming (DP) is a method for solving complex problems by breaking them down into simpler subproblems. 
It is particularly useful for optimization problems where the solution can be constructed from solutions to subproblems. 
The key idea is to store the results of subproblems to avoid redundant computations.

Problem: Climbing Stairs
Given a staircase with n steps, you can climb either 1 or 2 steps at a time. 
The goal is to find the number of distinct ways to reach the top.

Steps to Solve Using Dynamic Programming
Define the State:

Let dp[i] represent the number of ways to reach the i-th step.
Base Cases:

dp[1] = 1: There is only one way to reach the first step (1 step).
dp[2] = 2: There are two ways to reach the second step (1+1 steps or 2 steps).
State Transition:

For each step i from 3 to n, the number of ways to reach the i-th step is the sum of the ways to reach 
the (i-1)-th step and the (i-2)-th step.
This is because you can reach the i-th step either from the (i-1)-th step by taking 1 step or from 
the (i-2)-th step by taking 2 steps.
Therefore, dp[i] = dp[i-1] + dp[i-2].

Result:
The result is dp[n], which gives the number of ways to reach the n-th step.
"""

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

"""
Explanation
Base Cases:

If n is 1, return 1 because there is only one way to climb 1 step.

If n is 2, return 2 because there are two ways to climb 2 steps (1+1 or 2).

Dynamic Programming Array:
Initialize an array dp of size n+1 with all elements set to 0.

Set dp[1] to 1 and dp[2] to 2.

Fill the DP Array:
Iterate from 3 to n.

For each i, set dp[i] to the sum of dp[i-1] and dp[i-2].

Return the Result:
Return dp[n], which contains the number of ways to reach the n-th step.


Example Usage
Example 1:
Input: n = 2

Output: 2

Explanation: There are two ways to climb to the top: (1 step + 1 step) or (2 steps).

Example 2:
Input: n = 3

Output: 3

Explanation: There are three ways to climb to the top: (1 step + 1 step + 1 step), (1 step + 2 steps), or (2 steps + 1 step).

Benefits of Dynamic Programming

Efficiency: DP reduces the time complexity by storing the results of subproblems, avoiding redundant calculations.

Optimal Substructure: DP is suitable for problems that can be broken down into overlapping subproblems with optimal substructure.

Scalability: DP can handle large input sizes efficiently, making it suitable for a wide range of problems.

The dynamic programming approach ensures that the number of distinct ways to climb to the top is found efficiently, 
achieving a time complexity of O(n).
"""