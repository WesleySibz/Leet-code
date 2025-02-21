"""
Binary Search
Binary search is an efficient algorithm for finding an item from a sorted list of items. 

It works by repeatedly dividing the search interval in half. 

If the value of the search key is less than the item in the middle of the interval, 
narrow the interval to the lower half. Otherwise, narrow it to the upper half. 

Repeatedly check until the value is found or the interval is empty.

Key Concepts
Sorted List: Binary search requires the list to be sorted.

Divide and Conquer: The algorithm divides the search interval in half each time, reducing the problem size exponentially.

Time Complexity: Binary search has a time complexity of O(log n), making it much faster than linear search for large lists.

Steps
Initialize Pointers: Start with two pointers, low and high, representing the current search interval.

Calculate Middle: Find the middle index mid of the current interval.

Compare Middle Element:
If the middle element is equal to the target, return the middle index.

If the middle element is less than the target, move the low pointer to mid + 1.

If the middle element is greater than the target, move the high pointer to mid - 1.

Repeat: Repeat steps 2 and 3 until the target is found or the interval is empty (low exceeds high).

Implementation in Python
Here's a simple implementation of binary search in Python:
"""
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Target not found

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(arr, target)
print(f"Element {target} is at index {result}")

"""
Explanation
Initialize Pointers: The low pointer is initialized to the start of the array (index 0), 
and the high pointer is initialized to the end of the array (index len(arr) - 1).

Calculate Middle: The middle index mid is calculated as the integer division of (low + high) // 2.

Compare Middle Element:
If arr[mid] is equal to the target, the target is found, and the index mid is returned.

If arr[mid] is less than the target, the search continues in the right half by setting low to mid + 1.

If arr[mid] is greater than the target, the search continues in the left half by setting high to mid - 1.

Repeat: The process repeats until the target is found or the search interval is empty (low exceeds high).


Example Usage
Example 1:
Input: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 7

Output: 6

Explanation: The target value 7 is found at index 6.


Example 2:
Input: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 11

Output: -1

Explanation: The target value 11 is not found in the array.


Benefits of Binary Search
Efficiency: Binary search is much faster than linear search for large lists due to its O(log n) time complexity.

Simplicity: The algorithm is straightforward and easy to implement.

Applicability: Binary search can be used in various applications where the data is sorted, 
such as searching in databases, dictionaries, and more.

Binary search is a powerful and efficient algorithm for finding elements in a sorted list, 
making it a fundamental tool in computer science and programming.
"""