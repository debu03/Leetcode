class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while curr and curr.next: #while both are not null
            if curr.val==curr.next.val:
                curr.next=curr.next.next #skips the same number
            else:
                curr=curr.next
        return head