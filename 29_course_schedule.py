##########################################################
# Author: Raghav Sikaria
# LinkedIn: https://www.linkedin.com/in/raghavsikaria/
# Github: https://github.com/raghavsikaria
# Last Update: 29-5-2020
# Project: LeetCode May 31 Day 2020 Challenge - Day 29
##########################################################

# QUESTION
# This question is from the abovementioned challenge and can be found here on LeetCode: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3344/

############################################################################
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
 

# Constraints:

# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 1 <= numCourses <= 10^5
############################################################################

# DISCUSSION!
# My favourite concept - Loop Detection
# and that too with Graphs!
# My go to data structure in this
# scenario is Disjoint Sets
# However, this question calls for an
# directed graph where this data structure
# will not be optimal

class Solution:    
    @staticmethod
    def find_parent(node, parent_information):
        while parent_information[node] != node:
            immediate_parent_of_node = parent_information[node]
            parent_information[node] = parent_information[immediate_parent_of_node]
            node = immediate_parent_of_node
        return node

    @staticmethod
    def union(node1, node2, parent_information):
        parent_node1 = Solution.find_parent(node1, parent_information)
        parent_node2 = Solution.find_parent(node2, parent_information)
        if parent_node1 != parent_node2:    parent_information[parent_node2] = parent_node1

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        parent_information = [i for i in range(numCourses)]
        for pair in prerequisites:
            parent_node1 = Solution.find_parent(pair[0], parent_information)
            parent_node2 = Solution.find_parent(pair[1], parent_information)
            if parent_node1 == parent_node2: return False
            Solution.union(pair[0],pair[1], parent_information)
        
        return True


# ACCEPTED SOLUTION #1
# This is a much less elegant solution
# to me and has left me unsatisfied!

class Solution_:    

    @staticmethod
    def conduct_dfs(node, visited_information, children_information, graph_information):
        stack = []
        stack.append(node)

        while(stack):
            parent = stack[-1]

            if not visited_information[parent]:
                visited_information[parent] = True
                children_information[parent] = True
            else:
                children_information[parent] = False
                stack.pop()
            for neighbour in graph_information[parent]:
                if not visited_information[neighbour]:  stack.append(neighbour)
                elif children_information[neighbour]: return False

        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited_information = [False]*numCourses
        children_information = [False]*numCourses

        graph_information = defaultdict(list)
        for edge in prerequisites:
            graph_information[edge[1]].append(edge[0])

        for node in range(numCourses):
            if not visited_information[node]:        
                if not Solution.conduct_dfs(node, visited_information, children_information, graph_information): return False
        return True

# ACCEPTED SOLUTION #2
# [NEW LEARNING][BFS-INDEGREES APPROACH]
# [SOURCE]: https://www.geeksforgeeks.org/detect-cycle-in-a-directed-graph-using-bfs/?ref=rp
# This solution is one of my best new learnings so far in the May challenge!

class Solution__:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0]*numCourses
        graph_information = defaultdict(list)
        for edge in prerequisites:
            graph_information[edge[1]].append(edge[0])
            indegrees[edge[0]] += 1

        queue=[] 
        for i in range(numCourses): 
            if indegrees[i] == 0: 
                queue.append(i)

        count_of_visited_nodes = 0
        while(queue): 
            parent_node = queue.pop(0) 

            for neighbour in graph_information[parent_node]: 
                indegrees[neighbour]-=1
                if indegrees[neighbour] == 0:   queue.append(neighbour) 
            
            count_of_visited_nodes += 1

        return count_of_visited_nodes == numCourses