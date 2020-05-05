##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 5-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 5
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320/

############################################################################
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.
############################################################################

# ACCEPTED SOLUTION
# Personal Comments: Really not satisfied with any solution. Submitted the first 1 with hashmap, but that required
# 2 iterations of the input string which was really irritating me!
# This solution ensures O(n) Time (only 1 iteration of input string) and O(1) Space Complexity

class Solution:
    def firstUniqChar(self, s: str) -> int:
        target_index = -1
        min_index = len(s)
        frequency_array = [0]*26
        index_array = [0]*26
        
        for index,i in enumerate(s): 
            frequency_array[ord(i)-97] += 1
            index_array[ord(i)-97] = index
        
        for i in range(26):
            if frequency_array[i] == 1:
                if index_array[i] < min_index: min_index = index_array[i]
        
        return target_index if min_index == len(s) else min_index