class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_balanced(self, root: TreeNode) -> bool:
        def height(node: TreeNode) -> int:
            if node is None:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1
        
        return height(root) != -1

# Example usage:
# Constructing the binary tree for example 1
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20, TreeNode(15), TreeNode(7))

solution = Solution()
print(solution.is_balanced(root1))  # Output: true

# Constructing the binary tree for example 2
root2 = TreeNode(1)
root2.left = TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3))
root2.right = TreeNode(2)

print(solution.is_balanced(root2))  # Output: false

# Constructing the binary tree for example 3
root3 = None

print(solution.is_balanced(root3))  # Output: true