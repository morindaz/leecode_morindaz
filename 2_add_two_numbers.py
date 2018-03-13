# -*- coding: utf-8 -*-
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

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


class List(object):
    def __init__(self):
        self.cur_node = None
    def add(self,data):
        node = ListNode(data)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
a1 = ListNode(2)
a2 = ListNode(4)
a3 = ListNode(3)
a1.next = a2
a2.next = a3
b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(4)
b1.next = b2
b2.next = b3
l1 = a1
l2 = b1
while((l1!=None and l2!=None)):
    print(l1.val, l2.val)
    l1 = l1.next
    l2 = l2.next
