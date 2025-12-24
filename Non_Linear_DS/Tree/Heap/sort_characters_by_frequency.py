# 451. Sort Characters By Frequency
# LeetCode: https://leetcode.com/problems/sort-characters-by-frequency/

# Example 1:
# Input: s = "tree"
# Output: "eert"

# Example 2:
# Input: s = "cccaaa"
# Output: "aaaccc"

# Example 3:
# Input: s = "Aabb"
# Output: "bbAa"

import heapq
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        heap = []
        res = ""

        for ch, count in freq.items():
            heapq.heappush(heap, (-count, ch))

        while heap:
            count, ch = heapq.heappop(heap)
            res += (-count) * ch

        return res

# Time Complexity: O(n log k)
# Space Complexity: O(n)