"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        pre = None
        post = head
        while(post != None):
            cur = post
            post = post.next
            cur.next = pre
            pre = cur
        return cur

    def reverseList_bst(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev


if __name__ == '__main__':
    node1 = ListNode(5)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node4 = ListNode(2)
    node5 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    head = node1
    solution = Solution().reverseList(head)
    while solution!= None:
        print(solution.val)
        solution = solution.next


"""
链表套装：
206、24、141、142、25

"""
