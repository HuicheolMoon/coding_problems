# Problem : https://leetcode.com/problems/median-of-two-sorted-arrays/
# Date : 2021-04-03
# Median of Two Sorted Arrays


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        is_even = True if total % 2 == 0 else False
        mid = total // 2
        idx = 0
        now = 0
        while idx <= mid:
            pre = now
            if len(nums1) == 0:
                target = nums2
            elif len(nums2) == 0:
                target = nums1
            elif nums1[0] <= nums2[0]:
                target = nums1
            else:
                target = nums2
            now = target.pop(0)
            idx += 1
        return (pre+now)/2 if is_even else now
