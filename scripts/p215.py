"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。


提示：

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
"""

"""
第K个最大， 从大到小排序， 第K个数字
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lst = [nums[0]]
        for num in nums[1:]:
            if len(lst) == k and lst[-1] < num:
                del lst[-1]
            if len(lst) < k:
                i = 0
                while lst[i] > num and i < len(lst):
                    i += 1
                lst.insert(i, num)
        return lst[-1]