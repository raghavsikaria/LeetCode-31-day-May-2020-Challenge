##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 28-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 28
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3343/

############################################################################
# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

# Example 1:

# Input: 2
# Output: [0,1,1]
# Example 2:

# Input: 5
# Output: [0,1,1,2,1,2]
# Follow up:

# It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
############################################################################

# ACCEPTED SOLUTION #1
# Ensures O(nlogn) Time complexity
# Really didn't like the ANDing with 1 
# iteratively to get the count of 1s
# So here is what I learnt today:
# [NEW LEARNING][ALGORITHM]: Brian Kernighan's Algorithm
# [SOURCE]: https://www.geeksforgeeks.org/count-set-bits-in-an-integer/

class Solution:
    @staticmethod
    def get_set_bits(number):
        count = 0
        while(number):
            number &= (number-1)
            count += 1
        return count

    def countBits(self, num: int) -> List[int]:
        answer = []
        for number in range(num+1):
            answer.append(Solution.get_set_bits(number))
        return answer


# ACCEPTED SOLUTION #2
# Wrapped my head to get this down to O(n)
# But little did I know that simple BITWISE Manipulation
# was not going to cut this time!
# And finally, I got the intuition from ODD/EVEN hint and
# kind users of LeetCode.
# Pretty straightforward and hiding in plain sight.
# [NEW LEARNING]

class Solution_:
    def countBits(self, num: int) -> List[int]:
        answer = [0]*(num+1)
        for number in range(num+1):
            answer[number] = answer[number>>1] + number%2
        return answer