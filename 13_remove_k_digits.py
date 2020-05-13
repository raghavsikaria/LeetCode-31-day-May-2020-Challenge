##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 13-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 13
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3328/

############################################################################
# Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:

# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.
############################################################################

# ACCEPTED SOLUTION
# This solution ensures O(n) Time and O(n) Space Complexity
# [NEW LEARNING][SOURCE]: https://stackoverflow.com/questions/28223580/how-to-get-the-least-number-after-deleting-k-digits-from-the-input-number
# Personal Comments: This case made me feel so helpless! The problem was so simple, yet so mind-boggling
# Brute Force comes quite easy as always, but optimization required for this appeared quite unconventional to me
# Finally, the mentioned SO Post opened my mind!
# NOTE: The inequality in While loop condition can surely be simplified further. Have left so for readability!

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        answer = "-1"
        if len(num) == k: answer = "0"
        elif k == 0: answer = num
        else:
            my_stack = []
            stack_size = 0
            n = len(num)
            for index,number in enumerate(num):
              while my_stack != [] and number < my_stack[-1] and (n - index - 1) >=  (n - k - stack_size):
                my_stack.pop(-1)
                stack_size -= 1

              if len(my_stack) < n - k:
                my_stack.append(number)
                stack_size += 1

            answer = ''.join(my_stack).lstrip("0") or "0"
        return answer