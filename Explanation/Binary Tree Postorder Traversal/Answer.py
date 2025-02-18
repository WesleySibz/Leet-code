#Implementation (Recursive)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorder_traversal(self, root: TreeNode) -> list[int]:
        def postorder(node):
            if not node:
                return []
            return postorder(node.left) + postorder(node.right) + [node.val]
        
        return postorder(root)

# Example usage:
# Constructing the binary tree for example 1
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)

solution = Solution()
print(solution.postorderTraversal(root1))  # Output: [3, 2, 1]


#Implementation (Iterative)
class Solution:
    def postorder_traversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        
        stack, output = [root], []
        
        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        
        return output[::-1]

# Example usage:
# Constructing the binary tree for example 1
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)

solution = Solution()
print(solution.postorderTraversal(root1))  # Output: [3, 2, 1]

