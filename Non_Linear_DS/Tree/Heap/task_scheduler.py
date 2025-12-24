# 621. Task Scheduler
# LeetCode: https://leetcode.com/problems/task-scheduler/

# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8

# Example 2:
# Input: tasks = ["A","C","A","B","D","B"], n = 1
# Output: 6

# Example 3:
# Input: tasks = ["A","A","A","B","B","B"], n = 3
# Output: 10

import heapq
from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)
        time = 0
        cycle = n + 1
        while heap:
            temp = []
            i = 0
            while i < cycle and heap:
                freq = -heapq.heappop(heap)
                freq -= 1
                time += 1
                if freq > 0:
                    temp.append(freq)
                i += 1
            for f in temp:
                heapq.heappush(heap, -f)
            if heap:
                time += cycle - i
        return time
# Time Complexity: O(N log 26) ≈ O(N)
# Space Complexity: O(26) ≈ O(1)
