# leetcode link -> https://leetcode.com/problems/reorder-list/description/


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        self.head = head
        self.mid = self.break_and_find_mid()
        self.next_half = self.reverse(self.mid)

        cur1, cur2 = self.head, self.next_half
        while cur1 and cur2:
            temp1, temp2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = temp1
            cur2 = temp2
            cur1 = temp1


    def break_and_find_mid(self):
        slow = fast = self.head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        temp = slow.next
        slow.next = None
        return temp

    def get_printable(self, head):
        if head == None:
            return "Linked List is empty"
        curr = head
        ll_str = ""
        while curr.next:
            ll_str += f"{curr.val} -> "
            curr = curr.next
        ll_str += f"{curr.val}"
        return ll_str

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    