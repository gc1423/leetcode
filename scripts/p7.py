"""
coding=utf-8
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。
 

示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0
 

提示：

-231 <= x <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import math


class Solution:
    def reverse(self, x: int) -> int:
        """
        >>> 123
        321
        >>> -123
        -321
        >>> 210
        12
        >>> 0
        0

        :param x:
        :return:
        """
        flag = x < 0
        x = abs(x)
        res = 0
        while x >= 10:
            t = x % 10
            res = res * 10 + t
            x = int(x / 10)
        res = res * 10 + x
        res = -res if flag else res
        if -math.pow(2, 31) <= res <= math.pow(2, 32) - 1:
            return res
        else:
            return 0
        # return res


if __name__ == '__main__':
    print(Solution().reverse(10))
