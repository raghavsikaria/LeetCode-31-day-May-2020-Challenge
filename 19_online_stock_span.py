##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 19-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 19
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3334/

############################################################################
# Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

# The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

# For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

 

# Example 1:

# Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
# Output: [null,1,1,1,2,1,4,6]
# Explanation: 
# First, S = StockSpanner() is initialized.  Then:
# S.next(100) is called and returns 1,
# S.next(80) is called and returns 1,
# S.next(60) is called and returns 1,
# S.next(70) is called and returns 2,
# S.next(60) is called and returns 1,
# S.next(75) is called and returns 4,
# S.next(85) is called and returns 6.

# Note that (for example) S.next(75) returned 4, because the last 4 prices
# (including today's price of 75) were less than or equal to today's price.
 

# Note:

# Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
# There will be at most 10000 calls to StockSpanner.next per test case.
# There will be at most 150000 calls to StockSpanner.next across all test cases.
# The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.
############################################################################

# ACCEPTED SOLUTION #1
# This solution runs in O(n) Time and Space complexity
# Below is a more readable solution I came with first,
# And after submitting I realised - last case really
# takes care of the entire logic
# So #2 is a more compressed solution

class StockSpanner:

    def __init__(self):
        self.my_stack = []

    def next(self, price: int) -> int:
        if self.my_stack == []:
            self.my_stack.append([price,1])
            answer = 1
        else:
            if price < self.my_stack[-1][0]:    
                self.my_stack.append([price,1])
                answer = 1
            else:
                current_price_counter = 1
                while self.my_stack != [] and self.my_stack[-1][0] <= price:
                    last_element_till_now = self.my_stack.pop()
                    current_price_counter += last_element_till_now[1]
                self.my_stack.append([price,current_price_counter])
                answer = current_price_counter
        
        return answer


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# ACCEPTED SOLUTION #1a - COMPRESSED
class StockSpanner_:

    def __init__(self):
        self.my_stack = []

    def next(self, price: int) -> int:
        current_price_counter = 1
        while self.my_stack != [] and self.my_stack[-1][0] <= price:
            last_element_till_now = self.my_stack.pop()
            current_price_counter += last_element_till_now[1]
        self.my_stack.append([price,current_price_counter])
        return current_price_counter


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)