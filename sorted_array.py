class Solution:
    def mergeTwoLists(self, list1, list2):
        cur = temp = ListNode() #let's initialize temp and current to empty node
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1  #point to lowest one
                list1, cur = list1.next, list1 #shift one position ahead
            else:
                cur.next = list2 
                list2, cur = list2.next, list2
                
        if list1 or list2: #if one of them is empty
            cur.next = list1 if list1 else list2 #then point to whatever is left
            
        return temp.next #return head pointer which temp pointing