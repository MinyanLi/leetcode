# https://www.youtube.com/watch?v=XIdigk956u0



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()  # creat head as a listnode with the first value as 0 and point to next None
        tail = head   # tail and head will have the same pointers, changing the pointer in head will also change pointer in tail

        while list1 and list2:  # while list1 and list2 not empty, iterate until one of the list goes to the end
            if list1.val < list2.val:
                head.next = list1  # change the pointer of head to the first elment of list1
                list1 = list1.next # move to list1 next element
            else:
                head.next = list2
                list2 = list2.next # move to list2 next element
            head = head.next # move to the next element in head, at the end of the loop, head will only have one element

        if list1:  # if after iteration, list1 is still not empty
            head.next = list1 # point to the beginning of rest of list1

        if list2:
            head.next = list2 # point to the beginning of rest of list2

        
        return tail.next  # removing the first elemnt 0
