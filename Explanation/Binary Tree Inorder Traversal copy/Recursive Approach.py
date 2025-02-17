"""
Recursive Approach for Inorder Traversal
Inorder traversal of a binary tree visits nodes in the following order: left subtree, root node, right subtree. 
The recursive approach leverages the call stack to traverse the tree in this specific order.

Steps
Base Case: If the current node is None, return an empty list.

Recursive Case:
Recursively traverse the left subtree.

Visit the root node.

Recursively traverse the right subtree.

Combine Results: Concatenate the results from the left subtree, root node, and right subtree.
"""
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
print(solution.inorder_traversal(root1))  # Output: [1, 3, 2]

"""
Explanation
TreeNode Class:
Defines a node in the binary tree with a value (val), a pointer to the left child (left), and a pointer to the right child (right).

inorderTraversal Method:
Defines a helper function inorder that takes a node as an argument.

If the node is None, return an empty list (base case).

Recursively call inorder on the left subtree, visit the root node, and recursively call inorder on the right subtree.

Concatenate the results from the left subtree, root node, and right subtree, and return the final list.

Example Usage:
Construct a binary tree for the given example.

Create an instance of the Solution class.

Call the inorderTraversal method with the root of the binary tree.

Print the result, which is the inorder traversal of the tree.


Example Usage
Example 1:
Input: root = [1, null, 2, 3]

Output: [1, 3, 2]

Explanation: The inorder traversal visits nodes in the order: left subtree, root node, right subtree.

Benefits of Recursive Approach
Simplicity: The recursive approach is straightforward and easy to understand.

Natural Fit: Recursion naturally fits the tree structure, as each node can be treated as the root of its own subtree.

Concise Code: The recursive approach results in concise and readable code.

Constraints
The number of nodes in the tree is in the range [0, 100].

-100 <= Node.val <= 100

The recursive approach ensures that the inorder traversal is performed correctly, visiting nodes in the desired order. 
This method is suitable for small to moderately sized trees due to the potential for stack overflow with very deep trees.
"""