class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sorted_array_to_bst(self, nums: list[int]):
        if not nums:
            return None
        
        def helper(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(nums[mid])  # Use the platform's TreeNode
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root

        return helper(0, len(nums) - 1)
    
