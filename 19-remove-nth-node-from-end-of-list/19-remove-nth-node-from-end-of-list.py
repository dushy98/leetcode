# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = None
        i = 1
        
        while(p1):
            if i == n + 1:
                p2 = head
            elif i > n + 1:
                p2 = p2.next
            p1 = p1.next
            i += 1
        if p2:
            p2.next = p2.next.next
        else:
            head = head.next
        return head