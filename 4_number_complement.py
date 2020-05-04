##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 4-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 4
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/

############################################################################
# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

# Example 1:

# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 

# Example 2:

# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

# Note:

# The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# You could assume no leading zero bit in the integer’s binary representation.
# This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
############################################################################

# ACCEPTED SOLUTION #1
# This solution ensures O(n) Time and O(logn) Space Complexity

class Solution:
    def findComplement(self, num: int) -> int:
        reverse_binary_number = []
        while(num > 0):
            reverse_binary_number.append(num % 2)
            num = int(num/2)

        flipped_binary_number = [not bit for bit in reverse_binary_number]

        complement_number = 0
        for index,i in enumerate(flipped_binary_number):
            if i:   complement_number += 2**index

        return complement_number

# ACCEPTED SOLUTION #2
# [NEW][LEARNING] BITWISE Operation magic
# SOURCE: https://www.geeksforgeeks.org/invert-actual-bits-number/
# Brief summary: Utilise left shifting and XOR operation for bitwise manipulation
# This solution ensures O(logn) Time and O(1) Space Complexity

import math
class Solution:
    def findComplement(self, num: int) -> int:
        number_of_bits_in_num = int(math.log2(num)) + 1
        complement_number = num
        for i in range(number_of_bits_in_num):  
            complement_number ^= (1 << i)
        return complement_number