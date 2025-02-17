class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        def dfs(node, path):
            if node:
                path += str(node.val)
                if not node.left and not node.right:  # if leaf node
                    paths.append(path)
                else:
                    path += "->"
                    dfs(node.left, path)
                    dfs(node.right, path)
        
        paths = []
        dfs(root, "")
        return paths

# Example usage:
# Constructing the tree [1,2,3,null,5]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

solution = Solution()
print(solution.binaryTreePaths(root))  # Output: ["1->2->5", "1->3"]

# Constructing the tree [1]
root = TreeNode(1)

print(solution.binaryTreePaths(root))  # Output: ["1"]