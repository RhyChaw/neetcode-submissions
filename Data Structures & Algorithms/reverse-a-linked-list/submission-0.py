# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head.next is None:
    #         return head


        
    #     while head.val != None:
    #         head = head.next

    #     # after reaching the end
    #     temp : ListNode = { self.val = 0, self.next = head.prev }
    #     # Using this temporary node we shift everything
    #     # Delete the node
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev

    



