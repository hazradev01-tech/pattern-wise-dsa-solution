class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        fastp = head
        slowp = head
        
        # 1. Advance fast pointer n steps ahead
        for _ in range(n):
            if fastp is None:
                return head
            fastp = fastp.next
            
        # If fastp is None, it means we need to remove the head node (n equals the length of the list)
        if fastp is None:
            return head.next
            
        # 2. Move both pointers until fastp reaches the last node
        while fastp.next is not None:
            fastp = fastp.next
            slowp = slowp.next
            
        # 3. Remove the nth node from the end
        slowp.next = slowp.next.next
        return head
        