"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            # 空链或者单节点链表
            return head
        # t指向已反转的链表顶部
        t = head
        # n指向还未反转的链表顶部
        n = head.next
        t.next = None
        while n.next:
            temp = n.next # 未反转head
            n.next = t
            t = n
            n = temp
        n.next = t
        return n


if __name__ == '__main__':
    test = [1, 2]
    head = ListNode(test[0], None)
    t = head
    for value in test[1:]:
        temp = ListNode(value, None)
        t.next = temp
        t = temp
    head = Solution().reverseList(head)
    while head:
        print(head.val)
        head = head.next