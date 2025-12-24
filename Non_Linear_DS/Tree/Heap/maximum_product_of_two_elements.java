// 1464. Maximum Product of Two Elements in an Array
// LeetCode: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

// Example 1:
// Input: nums = [3,4,5,2]
// Output: 12

// Example 2:
// Input: nums = [1,5,4,5]
// Output: 16

// Example 3:
// Input: nums = [3,7]
// Output: 12

import java.util.*;

class Solution {
    public int maxProduct(int[] nums) {
        PriorityQueue<Integer> pq =
            new PriorityQueue<>(Collections.reverseOrder());

        for (int n : nums) {
            pq.add(n);
        }

        int max1 = pq.poll();
        int max2 = pq.poll();

        return (max1 - 1) * (max2 - 1);
    }
}
// Time Complexity: O(n log n)
// Space Complexity: O(n)
