##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 25-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 25
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3340/

############################################################################
# We write the integers of A and B (in the order they are given) on two separate horizontal lines.

# Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

# A[i] == B[j];
# The line we draw does not intersect any other connecting (non-horizontal) line.
# Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

# Return the maximum number of connecting lines we can draw in this way.

 

# Example 1:


# Input: A = [1,4,2], B = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
# Example 2:

# Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
# Output: 3
# Example 3:

# Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
# Output: 2
 

# Note:

# 1 <= A.length <= 500
# 1 <= B.length <= 500
# 1 <= A[i], B[i] <= 2000
############################################################################

# ACCEPTED SOLUTION
# Standard DP problem
# I am glad I could do it
# But disheartened at the same time, 
# that this was only because of my ADA Subject
# during my majors in CSE @ VIT
# Coming up with a bottom-up solution
# for a DP problem - is well - quite difficult!
# Ensures O(nm) Time and O(nm) Space complexity

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        len_a = len(A)
        len_b = len(B)

        memoization_matrix = [[0]*(len_a+1) for i in range(len_b+1)]

        for i in range(1,len_b+1):
            for j in range(1,len_a+1):
                if A[j-1] != B[i-1]:
                    memoization_matrix[i][j] = max(memoization_matrix[i][j-1], memoization_matrix[i-1][j])
                else:
                    memoization_matrix[i][j] = memoization_matrix[i-1][j-1] + 1
        
        return memoization_matrix[-1][-1]