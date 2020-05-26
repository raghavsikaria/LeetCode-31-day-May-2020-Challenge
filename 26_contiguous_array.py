##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 26-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 26
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3341/

############################################################################
# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.
############################################################################

# ACCEPTED SOLUTION
# [PERSONAL COMMENTS]: I was wondering whether
# a question based on prefix summation will come
# in this May challenge - and here it is!
# This [SOURCE]:https://leetcode.com/problems/contiguous-array/discuss/653061/Python-Detailed-explanation-O(n)-timeandspace-cumulative-sums
# by @DBabichev explains the question and intuition really well for any beginner!
# I don't think anyone could have explained better in less than 5 mins
# I credit my understanding of Time and Space Complexity for this question to @DBabichev

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = 0 

        # Really important for the base case!
        # took me quite a while to figure this out
        all_indexes = {0:-1}

        maximum_length = -1
        for index,number in enumerate(nums):
            prefix_sum += number if number else -1
            if prefix_sum not in all_indexes:   all_indexes[prefix_sum] = index
            else:
                maximum_length = max(maximum_length, index - all_indexes[prefix_sum])
        return maximum_length