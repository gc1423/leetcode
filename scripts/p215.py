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
        """
        插入排序解法
        :param nums:
        :param k:
        :return:
        """
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

    def partition(self, nums: List[int], l, r) -> int:
        i, j = l, r
        value = nums[l]
        while i < j:
            while j > i and nums[j] <= value:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] >= value:
                i += 1
            nums[j] = nums[i]
            # nums[i], nums[j] = nums[j], nums[i]
        nums[i] = value
        print(nums)
        return i

    def quickSort(self, nums: List[int], l, r) -> int:
        if l >= r:
            return l
        middle = self.partition(nums, l, r)
        return middle

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        """快速排序
        """
        l, r = 0, len(nums) - 1
        middle = self.quickSort(nums, l, r)
        while middle != k-1:
            if middle < k-1:
                middle = self.quickSort(nums, middle+1, r)
            else:
                middle = self.quickSort(nums, l, middle - 1)
        return nums[k-1]



if __name__ == '__main__':
    obj = Solution()
    # lst = [3,2,3,1,2,4,5,5,6]
    # lst = [28, 2, 3235, 4]
    # obj.quickSort(lst, 0, len(lst)-1)
    #
    # # print(obj.findKthLargest2( 2))
    # # 5
    print(obj.findKthLargest2([3,2,3,1,2,4,5,5,6], 4))
    # 4
