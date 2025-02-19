def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    index_map = {}
    
    for i, num in enumerate(nums):
        if num in index_map and i - index_map[num] <= k:
            return True
        index_map[num] = i
    
    return False

# Example usage:
print(contains_nearby_duplicate([1, 2, 3, 1], 3))  # Output: True
print(contains_nearby_duplicate([1, 0, 1, 1], 1))  # Output: True
print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))  # Output: False