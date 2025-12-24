// K Sorted Array
// GeeksforGeeks: https://www.geeksforgeeks.org/problems/k-sorted-array1610/1

// Example 1:
// Input: arr = [3, 2, 1, 5, 6, 4], k = 2
// Output: Yes

// Example 2:
// Input: arr = [13, 8, 10, 7, 15, 14, 12], k = 1
// Output: No

import java.util.*;
class Solution {
    static String isKSortedArray(int arr[], int n, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> a[0] - b[0]
        );

        for (int i = 0; i < n; i++) {
            pq.offer(new int[]{arr[i], i});
        }

        int i = 0;
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            if (Math.abs(curr[1] - i) > k) {
                return "No";
            }
            i++;
        }

        return "Yes";
    }
}
// Time Complexity: O(n log n)
// Space Complexity: O(n)