##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 9-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 9
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3324/

############################################################################
# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 14
# Output: false
############################################################################

# ACCEPTED SOLUTION #1
# This solution ensures O(sqrt(n)) Time and O(1) Space Complexity
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        answer = False
        i = 0
        while i*i < num + 1:
            if i*i == num:
                answer = True
                break
            i += 1
        return answer

# ACCEPTED SOLUTION #2
# This solution ensures O(logn) Time and O(1) Space Complexity
class Solution_:
    def isPerfectSquare(self, num: int) -> bool:
        answer = False
        l = 1
        r = num
        while(l<=r):
            mid = int((l + r)/2)
            if mid * mid == num:
                answer = mid
                break
            elif mid * mid > num:
                r = mid - 1
            else:   l = mid + 1
        return answer