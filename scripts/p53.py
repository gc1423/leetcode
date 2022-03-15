"""
coding=utf-8
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。

 

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23
 

提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划
        dp = [0 for i in range(len(nums))]
        max = nums[0]
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] if dp[i-1] <=0 else dp[i-1] + nums[i]
            if dp[i] > max:
                max = dp[i]
        return max

    def maxSubArray2(self, nums: List[int]) -> int:
        # 分治法 TODO
        ...


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    obj = Solution()
    print(obj.maxSubArray(nums))
    nums = [1]
    print(obj.maxSubArray(nums))
    nums = [5,4,-1,7,8]
    print(obj.maxSubArray(nums))
