"""
给你一个整数数组 nums，请你将该数组升序排列。

 

示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        pass

    def partision(self, nums: List[int], l: int, r: int) -> int:
        value = nums[l]
        i, j = l, r
        while i < j:
            while j > i and nums[j] >= value:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= value:
                i += 1
            nums[j] = nums[i]
        nums[i] = value
        return i

    def quickSort(self, nums: List[int], l: int = None, r: int = None):
        l = l if l else 0
        r = r if r else len(nums) - 1
        if l >= r:
            return
        middle = self.partision(nums, l, r)
        self.quickSort(nums, 0, middle - 1)
        self.quickSort(nums, middle+1, r)
        return nums

    def popSort(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)-1):
            swaped = False
            for j in range(0, len(nums)-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swaped = True
            if not swaped:
                break
        return nums

    def insertSort(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            position = -1
            for j in range(0, i):
                if nums[j] > nums[i]:
                    value = nums[i]
                    for k in range(i, position, -1):
                        nums[k] = nums[k-1]
                    nums[j] = value
                    break
        return nums


if __name__ == '__main__':
    nums = [5, 4, 3, 2, 1]
    nums = [3, 2, 1]
    # print(Solution().popSort(nums))
    Solution().quickSort(nums)
    print(nums)
