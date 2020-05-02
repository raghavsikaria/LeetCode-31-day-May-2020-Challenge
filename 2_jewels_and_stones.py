##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 1-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 2
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/

############################################################################
# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:

# Input: J = "aA", S = "aAAbbbb"
# Output: 3
# Example 2:

# Input: J = "z", S = "ZZ"
# Output: 0
# Note:

# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.
############################################################################

# ACCEPTED SOLUTION 1
# This solution is way better as it ensures O(n) Time and O(1) Space Complexity for Large strings

class Solution:
    def populate_frequency_array(self,given_string,lcase_array,ucase_array):
        for character in given_string: 
            if character.isupper(): ucase_array[ord(character) - 65] += 1
            else:   lcase_array[ord(character) - 97] += 1

    def numJewelsInStones(self, J: str, S: str) -> int:
        number_of_stone_jewels = 0
        j_lcase_freq_array = [0]*26
        j_ucase_freq_array = [0]*26
        s_lcase_freq_array = [0]*26
        s_ucase_freq_array = [0]*26
        
        self.populate_frequency_array(J,j_lcase_freq_array,j_ucase_freq_array)
        self.populate_frequency_array(S,s_lcase_freq_array,s_ucase_freq_array)

        for alphabet in range(0,26):
            if s_ucase_freq_array[alphabet] > 0 and j_ucase_freq_array[alphabet] > 0: 
                number_of_stone_jewels += s_ucase_freq_array[alphabet]
            if s_lcase_freq_array[alphabet] > 0 and j_lcase_freq_array[alphabet] > 0: 
                number_of_stone_jewels += s_lcase_freq_array[alphabet]
        
        return number_of_stone_jewels


# ACCEPTED SOLUTION 2
# Somehow this gives a better 'run-time' on LeetCode - and the Time Complexity hits O(nm)

class Solution_:
    def numJewelsInStones(self, J: str, S: str) -> int:
        c = 0
        for s in S: 
            if s in J:  c+=1        
        return c