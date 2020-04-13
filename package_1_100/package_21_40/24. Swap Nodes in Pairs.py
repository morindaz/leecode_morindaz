"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            a.next = b.next
            b.next = a
            pre.next = b
            pre = a
        return self.next #这里为什么不能用Head


if __name__ == '__main__':
    node1 = ListNode(5)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node4 = ListNode(2)
    # node5 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    # node4.next = node5
    head = node1
    solution = Solution().swapPairs(head)
    while(solution != None):
        print(solution.val)
        solution = solution.next

"""
链表交换两个元素的顺序
链表套装：
206、24、141、142、25
"""
