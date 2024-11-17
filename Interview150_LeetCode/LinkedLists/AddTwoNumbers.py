# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy head to simplify handling of the result list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        # Traverse both lists
        while l1 or l2 or carry:
            # Get values from the nodes, defaulting to 0 if the list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10  # Extract the carry
            current.next = ListNode(total % 10)  # Create a new node with the remainder

            # Move to the next nodes
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        # Return the resulting list (skipping the dummy head)
        return dummy_head.next
