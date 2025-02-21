"""
Sliding Window Approach
The sliding window approach is a technique used to solve problems that involve a subset of a sequence (such as an array or string). 
It involves maintaining a window that slides over the sequence to examine different parts of it. 
This technique is particularly useful for problems involving subarrays or substrings.

Key Concepts
Window Size: The size of the window can be fixed or variable, depending on the problem.

Sliding the Window: The window slides over the sequence, one element at a time, to examine different parts of the sequence.

Efficiency: The sliding window approach often reduces the time complexity of problems that would otherwise require nested loops.

Example: Finding the Index of the First Occurrence of a Substring
Let's use the sliding window approach to find the index of the first occurrence of a substring (needle) in a string (haystack).

Steps
Initialize Window: The window size is equal to the length of the needle.

Slide the Window: Slide the window over the haystack from the start to the end, 
checking each substring of the same length as the needle.

Check Substring: For each position of the window, check if the substring matches the needle.

Return Index: If a match is found, return the starting index of the window. If no match is found, return -1.
"""
class Solution:
    def str_str(self, haystack: str, needle: str) -> int:
        # Get the lengths of haystack and needle
        haystack_len = len(haystack)
        needle_len = len(needle)
        
        # Edge case: if needle is empty, return 0
        if needle_len == 0:
            return 0
        
        # Iterate through haystack with a sliding window
        for i in range(haystack_len - needle_len + 1):
            # Check if the substring matches needle
            if haystack[i:i + needle_len] == needle:
                return i
        
        # If needle is not found, return -1
        return -1

# Example usage:
solution = Solution()

haystack1 = "sadbutsad"
needle1 = "sad"
print(solution.str_str(haystack1, needle1))  # Output: 0

haystack2 = "leetcode"
needle2 = "leeto"
print(solution.str_str(haystack2, needle2))  # Output: -1

"""
Explanation
Class Definition: The Solution class is defined to encapsulate the strStr method.

strStr Method: This method finds the index of the first occurrence of needle in haystack.

Lengths: Use the len() function to get the lengths of haystack and needle.

Edge Case: If needle is empty, return 0.

Sliding Window: Iterate through haystack with a sliding window of length equal to needle.

Substring Check: For each position, check if the substring of haystack matches needle.

Return Index: If a match is found, return the starting index.

Return -1: If needle is not found in haystack, return -1.


Example Usage
Example 1:

Input: haystack = "sadbutsad", needle = "sad"

Output: 0

Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"

Output: -1

Explanation: "leeto" did not occur in "leetcode", so we return -1.

Benefits of Sliding Window Approach
Efficiency: The sliding window approach often reduces the time complexity of problems that would otherwise require nested loops.

Simplicity: It provides a straightforward way to examine subsets of a sequence.

Flexibility: The window size can be adjusted based on the problem requirements.

The sliding window approach is a powerful technique for solving problems involving subarrays or substrings efficiently.
"""