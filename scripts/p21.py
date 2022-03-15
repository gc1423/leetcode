"""
coding=utf-8
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例 1：


输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]
 

提示：

两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h = None
        current = None
        while list1 and list2:
            if list1.val < list2.val:
                node = list1
                list1 = list1.next
            else:
                node = list2
                list2 = list2.next
            if not h:
                h = node
                current = node
            else:
                current.next = node
                current = current.next
        left = list1 if list1 else list2
        if not h:
            return left
        else:
            current.next = left
        return h


def list2head(lst):
    head = None
    current = head
    for each in lst:
        node = ListNode(each)
        if not head:
            head = node
            current = node
        else:
            current.next = node
            current = current.next
    return head


def printList(head):
    while head:
        print(head.val)
        head = head.next


def test(l1, l2):
    list1 = list2head(l1)
    list2 = list2head(l2)
    obj = Solution()
    printList(obj.mergeTwoLists(list1,list2))


if __name__ == '__main__':
    l1 = [1,2,4]
    l2 = [1,3,4]
    l1 = []
    l2 = []
    l1 = []
    l2 = [0]
    test(l1, l2)


