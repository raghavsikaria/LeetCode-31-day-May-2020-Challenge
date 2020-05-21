##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 21-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 21
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3336/

############################################################################
# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

# Example 1:

# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation: 
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.
# Example 2:

# Input: matrix = 
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# Output: 7
# Explanation: 
# There are 6 squares of side 1.  
# There is 1 square of side 2. 
# Total number of squares = 6 + 1 = 7.
 

# Constraints:

# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1
############################################################################

# ACCEPTED SOLUTION
# This solution runs in O(n^2) Time and O(1) Space complexity
# Seeing this question straight away reminded of
# Maximum Square with 1s problem which is a standard
# DP problem
# I had learnt the algorithm long back from this source:
# [SOURCE] https://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/
# Added some optimization for space to not have a second matrix of m x n
# [PERSONAL COMMENTS] After submission I realised from other submissions that
# maybe having the 2nd matrix and then iterating through it to ge sum of all values
# can give better solution, but I did not understand the 
# reason - hence skipping that!

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0
        r,c = len(matrix),len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 1:
                    if (i == 0 or j == 0): count += 1    
                    else:
                        number_of_squares_ending_here = min(matrix[i-1][j],matrix[i-1][j-1],matrix[i][j-1]) + matrix[i][j]
                        matrix[i][j] = number_of_squares_ending_here
                        count += number_of_squares_ending_here
        return count