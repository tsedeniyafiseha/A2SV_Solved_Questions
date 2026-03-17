# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNodes(self, head):
        stack = []

        
        while head:
            val = head.val
            while stack and stack[-1] < val:
                stack.pop()
            stack.append(val)
            head = head.next

        
        dummy = ListNode()
        curr = dummy
        for v in stack:
            curr.next = ListNode(v)
            curr = curr.next

        return dummy.next