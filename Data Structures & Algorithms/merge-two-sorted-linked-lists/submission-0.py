# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(0)
        currhead = dummyhead
        while list1 is not None and list2 is not None:
            if list1.val<=list2.val:
                currhead.next = list1
                list1 = list1.next
            elif list2.val<list1.val:
                currhead.next = list2
                list2 = list2.next
            currhead = currhead.next
        
        if not list1:
             currhead.next = list2
        if not list2:
             currhead.next = list1

        return dummyhead.next
