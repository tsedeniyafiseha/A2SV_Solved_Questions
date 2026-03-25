"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res=[]
        def preorder(node):
            if not node:
                return
            res.append(node.val)
            for e in node.children:
                preorder(e)
        preorder(root)
        return res
        