# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head) -> int:
        result = []
        while head is not None:
            result.append(str(head.val))
            head = head.next
        
        return int("".join(result), 2)