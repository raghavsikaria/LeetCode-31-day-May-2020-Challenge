##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 31-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 31
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3346/

############################################################################
# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

# You have the following 3 operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
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
    def minDistance(self, word1: str, word2: str) -> int:
        len_w1 = len(word1)
        len_w2 = len(word2)

        memoization_matrix = [[0]*(len_w1+1) for i in range(len_w2+1)]

        for i in range(len_w2+1):
            for j in range(len_w1+1):
                if j == 0:  memoization_matrix[i][j] = i
                elif i == 0:    memoization_matrix[i][j] = j
                elif word1[j-1] == word2[i-1]: memoization_matrix[i][j] = memoization_matrix[i-1][j-1]
                else:   
                    memoization_matrix[i][j] = min(memoization_matrix[i-1][j-1], memoization_matrix[i-1][j], memoization_matrix[i][j-1]) + 1
        
        return memoization_matrix[-1][-1]