##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 20-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 20
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3335/

############################################################################
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
############################################################################

# ACCEPTED SOLUTION 1
# This solution runs in O(n) Time and O(n) Space complexity

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.counter = 1
        self.answer = -1

    def inorder_traversal(self,root,k): 
        if root and self.answer == -1: 
            self.inorder_traversal(root.left,k)
            if self.counter == k:
                self.answer = root.val
            self.counter += 1
            self.inorder_traversal(root.right,k)
            
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.inorder_traversal(root,k)
        return self.answer

# ACCEPTED SOLUTION #2
# NEW LEARNING - APPLYING ITERATIVE
# APPROACH TO BST
# PICKED THIS UP THIS REALLY COOL SOLUTION FROM OTHER
# SUBMITTED SOLUTIONS IN THIS CHALLENGE
# DON'T KNOW THE ORIGINAL AUTHOR

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        counter = 1
        my_stack = []
        while True:
            while root:
                my_stack.append(root)
                root = root.left
            root = my_stack.pop()
            if counter == k: return root.val
            counter += 1
            root = root.right