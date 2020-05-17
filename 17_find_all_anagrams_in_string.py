##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 17-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 17
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3332/

############################################################################
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
############################################################################

# ACCEPTED SOLUTION #1
# Seeing this question, frequency array approach was the first
# that came in my mind. This approach theoretically ensures
# O(n) Time and O(1) space complexity. However, that O(n) complexity
# also contains 'n' calls to the check_for_anagram function
# which is bound to take a toll on the algorithm even if each of 
# those calls last for a constant time

# Not really satisfied with the solution!

class Solution:
    check_for_anagram = lambda a1,a2: a1==a2
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        solution = []

        p_freq_array = [0]*26
        window_freq_array = [0]*26
        p_len = len(p)

        for ele in p:   p_freq_array[ord(ele) - 97] += 1
        for ele in s[:p_len]:   window_freq_array[ord(ele) - 97] += 1
        first_index = 0
        if Solution.check_for_anagram(p_freq_array,window_freq_array):  solution.append(first_index)
    
        for ele in s[p_len:]:
            window_freq_array[ord(s[first_index])-97] -= 1
            window_freq_array[ord(ele)-97] += 1    
            first_index += 1
            if Solution.check_for_anagram(p_freq_array,window_freq_array):  solution.append(first_index)
        return solution