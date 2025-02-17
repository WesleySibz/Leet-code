class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder_traversal(self, root: TreeNode) -> list[int]:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        return inorder(root)

# Example usage:
# Constructing the binary tree for example 1
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)

solution = Solution()
print(solution.inorder_traversal(root1))  # Output: [1, 3, 2]

"""
Iterative Approach
The iterative approach uses a stack to simulate the recursive call stack. 
This approach is useful when you want to avoid the overhead of recursive function calls.

Implementation (Iterative)
"""
class Solution:
    def inorder_traversal(self, root: TreeNode) -> list[int]:
        result, stack = [], []
        current = root
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        
        return result

# Example usage:
# Constructing the binary tree for example 1
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)

solution = Solution()
print(solution.inorder_traversal(root1))  # Output: [1, 3, 2]