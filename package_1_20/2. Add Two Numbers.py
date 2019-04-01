# -*- coding: utf-8 -*-
'''
You are given two non-empty linked lists representing two non-negative integers. T

he digits are stored in reverse order and each of their nodes contain a single digit.

Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# class List(object):
#     def __init__(self):
#         self.cur_node = None
#     def add(self,data):
#         node = ListNode(data)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = 0

        head_val = l1.val + l2.val
        if head_val >= 10:
            head_val -= 10
            head = ListNode(head_val)
            flag = 1
        else:
            head = ListNode(head_val)
        res = head
        l1 = l1.next
        l2 = l2.next

        while(l1 != None and l2 != None):
            tmp_val = l1.val + l2.val+ flag
            flag = 0
            if tmp_val >= 10:
                tmp_list = ListNode(tmp_val - 10 )
                flag = 1
            else:
                tmp_list = ListNode(tmp_val)
            head.next = tmp_list
            head = head.next
            l1 = l1.next
            l2 = l2.next
        if l1 == None and l2!= None:
            self.append_rest(flag, l2, head)
        elif l2 == None and l1 != None:
            self.append_rest(flag, l1, head)
        elif flag!= 0:
            tmp_list = ListNode(flag)
            head.next = tmp_list
        return res

    def append_rest(self, flag, rest_list, head):
        while(rest_list != None):
            tmp_val = rest_list.val + flag
            flag = 0
            if tmp_val >= 10:
                tmp_list = ListNode(tmp_val - 10)
                flag = 1
            else:
                tmp_list = ListNode(tmp_val)
            head.next = tmp_list
            head = head.next
            rest_list = rest_list.next
        if flag != 0:
            tmp_list = ListNode(flag)
            head.next = tmp_list
            # l2 = l2.next

if __name__ == '__main__':
    a1 = ListNode(5)
    # a2 = ListNode(8)
    # a3 = ListNode(3)
    # a1.next = a2
    # a2.next = a3
    b1 = ListNode(5)
    # b2 = ListNode(9)
    # b3 = ListNode(4)
    # b1.next = b2
    # b2.next = b3
    l1 = a1
    l2 = b1

    solution = Solution().addTwoNumbers(l1, l2)
    while(solution!=None):
        print(solution.val)
        solution = solution.next
        # l2 = l2.next
