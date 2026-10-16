# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return None
        fast = head
        slow = head
        before_slow = None

        for i in range(n):
            fast = fast.next
        
        while fast is not None:
            before_slow = slow
            slow = slow.next
            fast = fast.next
        
        #Middle case
        if before_slow and slow.next:
            before_slow.next = slow.next
        
        if before_slow and not slow.next:
            before_slow.next = None
        if not before_slow and slow.next:
            head = slow.next
        if not before_slow and not slow.next:
            return None
        slow.next = None
        return head
    
        
        