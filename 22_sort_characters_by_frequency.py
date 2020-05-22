##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 22-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 22
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3337/

############################################################################
# Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:

# Input:
# "tree"

# Output:
# "eert"

# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input:
# "cccaaa"

# Output:
# "cccaaa"

# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input:
# "Aabb"

# Output:
# "bbAa"

# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
############################################################################

# ACCEPTED SOLUTION #1
# Ensures O(n) Time and O(1) Space complexity

class Solution:
    def frequencySort(self, s: str) -> str:
        answer = ""
        case_freq = [0]*255
        case_map = []
        for element in s:   case_freq[ord(element)] += 1
        for element in range(255):  case_map.append([chr(element),case_freq[element]])
        case_map.sort(key = lambda x: x[1], reverse = True) 
        for ele in case_map:
            if ele[1] == 0: break
            answer += ele[0]*ele[1]
        return answer


# ACCEPTED SOLUTION #2
# Same as above, but a new learning for me
# Found the below solution in submissions
# Don't know the author
# [NEW LEARNING][MORE PYTHONIC WAY]

class Solution:
    def frequencySort(self, s: str) -> str:
        a = Counter(s)
        return "".join(cr*c for cr, c in sorted(a.items(), key=lambda x:x[1], reverse=True))