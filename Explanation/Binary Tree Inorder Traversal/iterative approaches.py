"""
Iterative Approaches for Inorder Traversal
The iterative approach for inorder traversal of a binary tree uses a stack to simulate the recursive call stack. 
This method is useful for avoiding the overhead of recursive function calls and is suitable for environments with limited stack space.

Steps
Initialize Stack and Result List: Use a stack to keep track of nodes and a list to store the traversal result.

Traverse the Tree:
Use a pointer current to traverse the tree.

While current is not None or the stack is not empty:
Traverse to the leftmost node, pushing each node onto the stack.

Pop a node from the stack, visit it by appending its value to the result list, and move to its right subtree.

Return the Result: Return the list containing the inorder traversal of the tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

"""
Explanation
TreeNode Class:
Defines a node in the binary tree with a value (val), a pointer to the left child (left), and a pointer to the right child (right).

inorderTraversal Method:
Initializes an empty list result to store the traversal result and an empty stack stack to simulate the recursive call stack.

Uses a pointer current to traverse the tree starting from the root.

While current is not None or the stack is not empty:
Traverse to the leftmost node, pushing each node onto the stack.

Pop a node from the stack, visit it by appending its value to result, and move to its right subtree.

Returns the result list containing the inorder traversal of the tree.


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

Benefits of Iterative Approach
Avoids Recursion Overhead: The iterative approach avoids the overhead of recursive function calls, 
making it suitable for environments with limited stack space.

Handles Large Trees: The iterative approach can handle larger trees without the risk of stack overflow.

Explicit Stack Management: The use of an explicit stack provides better control over the traversal process.

Constraints
The number of nodes in the tree is in the range [0, 100].

-100 <= Node.val <= 100

The iterative approach ensures that the inorder traversal is performed correctly, visiting nodes in the desired order. 
This method is suitable for both small and large trees, providing an efficient and reliable solution for inorder traversal.
"""