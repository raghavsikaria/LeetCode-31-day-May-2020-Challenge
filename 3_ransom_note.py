##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 3-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 3
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/

############################################################################
# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
############################################################################

# ACCEPTED SOLUTION
# This solution ensures O(n) Time and O(1) Space Complexity for Large strings

class Solution:
    def populate_frequency_array(self,given_string,lcase_array):
        for character in given_string: 
            lcase_array[ord(character) - 97] += 1

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        answer = True
        r_lcase_freq_array = [0]*26
        m_lcase_freq_array = [0]*26
        
        self.populate_frequency_array(ransomNote,r_lcase_freq_array)
        self.populate_frequency_array(magazine,m_lcase_freq_array)

        for alphabet in range(0,26):
            if r_lcase_freq_array[alphabet] > m_lcase_freq_array[alphabet]: answer = False
        
        return answer