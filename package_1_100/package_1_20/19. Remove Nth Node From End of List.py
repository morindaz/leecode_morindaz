# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        to_be_removed = head
        to_be_end = head
        to_be_before = None
        for i in range(n):
            to_be_end = to_be_end.next

        while to_be_end != None:
            to_be_before = to_be_removed
            to_be_removed = to_be_removed.next
            to_be_end = to_be_end.next

        if to_be_before == None:
            head = to_be_removed.next
        else:
            to_be_before.next = to_be_removed.next
        return head




if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    solution = Solution()
    head = solution.removeNthFromEnd(node1, 5)
    # head = node1
    while head != None:
        print(head.val)
        head = head.next

