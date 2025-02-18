#Implementation (Recursive)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorder_traversal(self, root: TreeNode) -> list[int]:
        def preorder(node):
            if not node:
                return []
            return [node.val] + preorder(node.left) + preorder(node.right)
        
        return preorder(root)

# Example usage:
# Constructing the binary tree for example 1
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)

solution = Solution()
print(solution.preorderTraversal(root1))  # Output: [1, 2, 3]


#Implementation (Iterative)
class Solution:
    def preorder_traversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        
        stack, output = [root], []
        
        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        
        return output

# Example usage:
# Constructing the binary tree for example 1
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)

solution = Solution()
print(solution.preorderTraversal(root1))  # Output: [1, 2, 3]