##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 30-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 30
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3345/

############################################################################
# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

# (Here, the distance between two points on a plane is the Euclidean distance.)

# You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

# Example 1:

# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation: 
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)
 

# Note:

# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000
############################################################################

# ACCEPTED SOLUTION #1
# Ensures O(nlogn) Time and O(n) Space complexity

class Solution:
    find_distance = lambda x, y: x**2 + y**2
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distances = []
        for point in points:
            distances.append([point, Solution.find_distance(point[0], point[1])])
        distances.sort(key = lambda x: x[1]) 
        return [element[0] for element in distances[:K]]

# LEARNINGS FROM OTHER SUBMISSIONS
# FOUND THESE SOLUTIONS FROM THE SUBMISSIONS PAGE
# THEY HAVE IMPLEMENTATION IN A MUCH BETTER PYTHONIC WAY

class Solution_:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda x: x[0] * x[0] + x[1] * x[1])
        return points[:K]