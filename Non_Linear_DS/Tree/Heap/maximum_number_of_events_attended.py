# 1353. Maximum Number of Events That Can Be Attended
# LeetCode: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

# Example 1:
# Input: events = [[1,2],[2,3],[3,4]]
# Output: 3

# Example 2:
# Input: events = [[1,2],[2,3],[3,4],[1,2]]
# Output: 4


import heapq

class Solution:
    def maxEvents(self, events):
        events.sort(key=lambda x: x[0])
        heap = []

        day = 0
        i = 0
        n = len(events)
        count = 0

        while i < n or heap:
            if not heap:
                day = events[i][0]

            while i < n and events[i][0] == day:
                heapq.heappush(heap, events[i][1])
                i += 1

            while heap and heap[0] < day:
                heapq.heappop(heap)

            if heap:
                heapq.heappop(heap)
                count += 1

            day += 1

        return count
# Time Complexity: O(n log n)
# Space Complexity: O(n)