##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 27-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 27
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3342/

############################################################################
# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

# Each person may dislike some other people, and they should not go into the same group. 

# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

# Return true if and only if it is possible to split everyone into two groups in this way.

 

# Example 1:

# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
# Example 2:

# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
# Example 3:

# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
 

# Note:

# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# There does not exist i != j for which dislikes[i] == dislikes[j].
############################################################################

# ACCEPTED SOLUTION
# BFS - My saviour!

class Solution:
    @staticmethod
    def bfs_util(i, visited_bfs, color_status, graph_info):
        visited_bfs[i] = True
        color_status[i] = 1
        bfs_queue = []
        bfs_queue.append(i)
        while(bfs_queue != []):
            popped_i = bfs_queue.pop(0)
            color_popped_i = color_status[popped_i]
            color_to_apply = int(not color_popped_i)
            for neighbour_i in graph_info[popped_i]:
                if visited_bfs[neighbour_i] is False:
                    bfs_queue.append(neighbour_i)
                    visited_bfs[neighbour_i] = True
                    color_status[neighbour_i] = color_to_apply
                else:
                    if color_status[neighbour_i] == color_popped_i: return False
        return True

    @staticmethod
    def conduct_bfs(n, graph_info):
        visited_bfs = n * [False]
        color_status = n * [None]
        for i in range(1,n):
            if visited_bfs[i] is False:
                verdict = Solution.bfs_util(i, visited_bfs, color_status, graph_info)
                if not verdict: return False
        return True

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph_info = defaultdict(list)
        for dislike_edge in dislikes:
            graph_info[dislike_edge[0]].append(dislike_edge[1])
            graph_info[dislike_edge[1]].append(dislike_edge[0])
        return Solution.conduct_bfs(N+1, graph_info)