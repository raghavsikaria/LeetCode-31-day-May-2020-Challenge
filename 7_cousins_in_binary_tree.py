##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 7-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 7
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3322/

############################################################################
# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

# Return true if and only if the nodes corresponding to the values x and y are cousins.

 

# Example 1:


# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# Example 2:


# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# Example 3:



# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
 

# Note:

# The number of nodes in the tree will be between 2 and 100.
# Each node has a unique integer value from 1 to 100.
############################################################################

# ACCEPTED SOLUTION #1
# This solution ensures O(n) Time and O(n) Space Complexity

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_node_parent(self,value,node,parent):
        if node is None: return 0
        if node.val == value: return parent
        else:
            return self.find_node_parent(value,node.left,node.val) or self.find_node_parent(value,node.right,node.val)
    
    def find_node_level(self,value,root):
        level = 0
        q = [root,None]
        candidate_parent = None
        while(q != []):
            parent = q[0]            
            q.pop(0)
            if parent == None:  
                if q[0] != None: q.append(None)
                level += 1
            else:    
                if parent.val == value: break                
                if parent.left is not None: q.append(parent.left)
                if parent.right is not None: q.append(parent.right)
        return level
            
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parent_x, level_x = self.find_node_parent(x,root,root.val), self.find_node_level(x,root)
        parent_y, level_y = self.find_node_parent(y,root,root.val), self.find_node_level(y,root)
        return (parent_y != parent_x and level_x == level_y)


# ACCEPTED SOLUTION #2
# This solution ensures O(n) Time and O(1) Space Complexity
# [NEW][LEARNING] Utilising Parent recursion to maintain level values!
# Personal Comments: Hate trees which are not BST!!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_:
    def find_node_data(self,value,node,parent,level):
        if node is None: return 0
        if node.val == value: return [parent,level]
        else:
            return self.find_node_data(value,node.left,node.val,level+1) or self.find_node_data(value,node.right,node.val,level+1)
     
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parent_x, level_x = self.find_node_data(x,root,root.val,0)
        parent_y, level_y = self.find_node_data(y,root,root.val,0)
        return (parent_y != parent_x and level_x == level_y)