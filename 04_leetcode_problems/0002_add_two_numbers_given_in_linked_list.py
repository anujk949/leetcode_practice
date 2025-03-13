# leetcode link -> https://leetcode.com/problems/add-two-numbers/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        output = ListNode()
        curr_o = output
        carry=0
        while curr1 and curr2:
            temp = curr1.val + curr2.val + carry
            val, carry = temp%10, temp//10
            curr_o.next = ListNode(val)
            curr_o = curr_o.next
            curr1 = curr1.next
            curr2 = curr2.next

        while curr1:
            temp = curr1.val + carry
            val, carry = temp%10, temp//10
            curr_o.next = ListNode(val)
            curr_o = curr_o.next
            curr1 = curr1.next

        while curr2:
            temp = curr2.val + carry
            val, carry = temp%10, temp//10
            curr_o.next = ListNode(val)
            curr_o = curr_o.next
            curr2 = curr2.next

        if carry != 0:
            new_node = ListNode(carry)
            curr_o.next = new_node

        return output.next
        