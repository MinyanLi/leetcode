# Runtime 71 ms Beats 92.18%
# Memory 14 MB Beats 43.46%

# add all to l1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        suml = l1

        while l1 and l2:
            l1.val = l1.val + l2.val
            if l1.val > 9:
                l1.val = l1.val - 10
                if l1.next != None:
                    l1.next.val += 1
                if l1.next == None:
                    l1.next = ListNode(1)
            if l1.next == None and l2.next != None:
                l1.next = ListNode(0)
            if l1.next != None and l2.next == None:
                l2.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next

        return suml

        
