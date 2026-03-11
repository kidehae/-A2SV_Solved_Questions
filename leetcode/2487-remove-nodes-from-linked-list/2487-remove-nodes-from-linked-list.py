# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        mono = []
        while head :
            while mono and head.val > mono[-1]:
                mono.pop()
            mono.append(head.val)
            head = head.next
        print(mono)
        head = ListNode(mono.pop(0))
        res = head
        for i in mono:
            new_node = ListNode(i)
            res.next = new_node
            res = res.next
        return head

       
        