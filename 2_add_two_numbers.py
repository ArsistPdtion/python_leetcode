'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

难点: python如何实现两个单链表的输入
'''

import logging

log_file = './loging.log'
logging.basicConfig(filename=log_file,level=logging.DEBUG)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        l3 = ListNode(0)
        mod = 0
        l3.val = (l1.val + l2.val)%10
        mod = (l1.val + l2.val)//10
        #print("l1.next.val = ",l1.next.val)
        #print("the value : ",(l1.next.val + l2.next.val + mod)%10)
        logging.debug("l1.next.val = ")
        logging.debug("the value : ")
        l3.next = ListNode((l1.next.val + l2.next.val + mod)%10)
        mod = (l1.next.val + l2.next.val + mod)//10
        #print("the mod is: ",mod)
        logging.debug("the mod is: ")
        l3.next.next = ListNode((l1.next.next.val + l2.next.next.val + mod) % 10)
        return l3

if __name__ == '__main__':
    lis3 = Solution()
    l3 = ListNode(0)

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)


    l3 = lis3.addTwoNumbers(l1,l2)
    print(l3.val,l3.next.val,l3.next.next.val)
