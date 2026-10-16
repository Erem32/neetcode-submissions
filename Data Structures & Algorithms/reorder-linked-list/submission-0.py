# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        #Slow is at the half point of the list now or first middle if the list if list is even
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        before = None
        curr = slow.next
        slow.next = None
        
        while curr is not None:
            next = curr.next
            curr.next = before
            before = curr
            curr = next
        
        #before is the new head of the second half
      
        dummyhead = ListNode(0)
        temp = head
        
        while temp is not None and before is not None:
            #first half
            
            dummyhead.next = temp
            dummyhead = dummyhead.next
            temp = temp.next
            
            #second half
            dummyhead.next = before
            dummyhead = dummyhead.next
            before = before.next
        if temp:
            dummyhead.next = temp


       
        
        
