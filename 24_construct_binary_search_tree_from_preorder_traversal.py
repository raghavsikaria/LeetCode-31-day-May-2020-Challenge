##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 23-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 23
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3339/

############################################################################
# Return the root node of a binary search tree that matches the given preorder traversal.

# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

# It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

# Example 1:

# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

 

# Constraints:

# 1 <= preorder.length <= 100
# 1 <= preorder[i] <= 10^8
# The values of preorder are distinct.
############################################################################

# ACCEPTED SOLUTION #1
# [NEW LEARNING][SOURCE]: https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversal-set-2/?ref=rp
# BST and Order conversions have always intrigued and frightened me
# ALWAYS!
# It was about time I owned up to it and gave some attention
# Ensures O(n) Time and O(n) Space complexity

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        my_stack = []
        root_node = TreeNode(val=preorder[0])
        my_stack.append(root_node)

        for node_data in preorder[1:]:
            this_node_data = None
            while my_stack and node_data > my_stack[-1].val:    this_node_data = my_stack.pop()

            if this_node_data:
                this_node_data.right = TreeNode(val=node_data)
                my_stack.append(this_node_data.right)
            else:
                this_node_data = my_stack[-1]
                this_node_data.left = TreeNode(val=node_data)
                my_stack.append(this_node_data.left)
        
        return root_node




# SOLUTIONS FROM OTHER SUBMISSIONS
# Found this enlightening and quite intuitive
# solution from the submissions page
# Putting it over here, since it's so good
# Don't know the author though!
# This one ensures O(1) Space complexity
# Although it does take a toll on the time complexity!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        head = TreeNode(preorder[0])
        for node in preorder[1:]:
            newnode = TreeNode(node)
            searchnode = head
            while 1:
                if searchnode.val > newnode.val:
                    if searchnode.left == None: 
                        searchnode.left = newnode
                        break
                    searchnode = searchnode.left
                else:
                    if searchnode.right == None: 
                        searchnode.right = newnode
                        break
                    searchnode = searchnode.right
        return head