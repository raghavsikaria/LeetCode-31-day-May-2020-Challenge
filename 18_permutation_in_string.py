##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 18-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 18
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3333/

############################################################################
# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

# Example 1:

# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
 

# Note:

# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
############################################################################

# ACCEPTED SOLUTION
# Ensures O(n) Time and O(1) Space complexity

class Solution:
    check_for_anagram = lambda a1,a2: a1==a2
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1_len = len(s1)
        s1_freq, s2_freq = [0]*26, [0]*26
        
        for i in range(s1_len):   
            s1_freq[ord(s1[i]) - 97] += 1
            s2_freq[ord(s2[i]) - 97] += 1

        if Solution.check_for_anagram(s1_freq,s2_freq):  return True

        first_index = 0
        for ele in s2[s1_len:]:
            s2_freq[ord(s2[first_index])-97] -= 1
            s2_freq[ord(ele)-97] += 1   
            first_index += 1 
            if Solution.check_for_anagram(s1_freq,s2_freq):  return True
        return False