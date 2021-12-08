"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        >>> Solution().findMedianSortedArrays([1, 3], [2])
        2.0000
        >>> Solution().findMedianSortedArrays([1, 2], [3, 4])
        2.5000
        >>> Solution().findMedianSortedArrays([0, 0], [0, 0])
        0.0000
        >>> Solution().findMedianSortedArrays([], [1])
        1.0000
        >>> Solution().findMedianSortedArrays([2], [])
        2.0000
        """
        total_length = len(nums1) + len(nums2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
