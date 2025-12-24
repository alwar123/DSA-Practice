# 215. Kth Largest Element in an Array
# LeetCode: https://leetcode.com/problems/kth-largest-element-in-an-array/

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, -nums[i])

        for _ in range(k - 1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)
