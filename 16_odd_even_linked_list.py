##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 16-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 16
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3331/

############################################################################
# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

# Example 1:

# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# Example 2:

# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
# Note:

# The relative order inside both the even and odd groups should remain as it was in the input.
# The first node is considered odd, the second node even and so on ...
############################################################################

# ACCEPTED SOLUTION

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None: return None
        odd_node = head
        even_node = head.next
        even_head = even_node
        
        while even_node is not None:
            if odd_node is None or even_node.next is None: break
            odd_node.next = even_node.next
            odd_node = odd_node.next
            even_node.next = odd_node.next
            even_node = even_node.next
        odd_node.next = even_head
        return head