class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def count_nodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def get_depth(node):
            depth = 0
            while node.left:
                node = node.left
                depth += 1
            return depth
        
        def exists(index, depth, node):
            left, right = 0, 2**depth - 1
            for _ in range(depth):
                mid = (left + right) // 2
                if index <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1
            return node is not None
        
        depth = get_depth(root)
        if depth == 0:
            return 1
        
        left, right = 1, 2**depth - 1
        while left <= right:
            mid = (left + right) // 2
            if exists(mid, depth, root):
                left = mid + 1
            else:
                right = mid - 1
        
        return (2**depth - 1) + left

# Example usage:
# Constructing the tree [1,2,3,4,5,6]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

solution = Solution()
print(solution.count_nodes(root))  # Output: 6