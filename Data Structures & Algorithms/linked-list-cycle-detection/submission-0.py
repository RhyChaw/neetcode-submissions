
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        curr = head

        while curr is not None:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next
        
        return False
