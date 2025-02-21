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