"""
To return all root-to-leaf paths in a binary tree using the Depth-First Search 
(DFS) approach, you can follow these steps. 
The DFS approach involves traversing the tree from the root to each leaf node, 
constructing the path as you go.

Method Explanation
Depth-First Search (DFS): Use DFS to traverse the tree from the root to each leaf node.

Path Construction: Construct the path as you traverse the tree and add it to the result 
list when a leaf node is reached.
"""

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

"""
Explanation
TreeNode Class: Define a TreeNode class to represent each node in the binary tree.

DFS Function: Define a helper function dfs that takes a node and the current path as 
arguments.

If the node is not None, append the node's value to the current path.

If the node is a leaf (no left and right children), add the current path to the paths list.

If the node is not a leaf, append "->" to the current path and recursively call dfs on 
the left and right children.

Initialize Paths: Initialize an empty list paths to store the root-to-leaf paths.

Call DFS: Call the dfs function starting from the root node with an empty path.

Return Paths: Return the paths list containing all root-to-leaf paths.

Example Usage
For the tree [1,2,3,null,5], the output is ["1->2->5", "1->3"].

For the tree [1], the output is ["1"].

Constraints
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100

Summary
The DFS approach is used to traverse the binary tree from the root to each leaf node. 
As you traverse, you construct the path and add it to the result list when a leaf node 
is reached. This approach ensures that all root-to-leaf paths are found efficiently using 
a depth-first search traversal.
"""
