# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
       
        prefix = {0: 1}
        
        def dfs(node, cSum):
            if not node:
                return 0
            cSum+=node.val
            count= prefix.get(cSum-targetSum,0)
            prefix[cSum]=prefix.get(cSum,0)+1

            count += dfs(node.left, cSum)
            count += dfs(node.right, cSum)
            
            prefix[cSum] -= 1
            
            return count
        
        return dfs(root, 0)