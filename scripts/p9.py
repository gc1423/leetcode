"""

给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        >>> Solution().isPalindrome(121)
        True
        >>> Solution().isPalindrome(-121)
        False
        >>> Solution().isPalindrome(10)
        False
        >>> Solution().isPalindrome(-101)
        False
        """
        if x < 0:
            return False
        st = str(x)
        n = len(st)
        for i in range(int(n/2)):
            if st[i] != st[n-i-1]:
                return False
        return True

    def isPalindrome2(self, x: int) -> bool:
        """ 进阶: 你能不将整数转为字符串来解决这个问题吗？
        >>> Solution().isPalindrome2(121)
        True
        >>> Solution().isPalindrome2(-121)
        False
        >>> Solution().isPalindrome2(10)
        False
        >>> Solution().isPalindrome2(-101)
        False
        """
        if x < 0:
            return False
        t = 0
        n = x
        while n > 0:
            temp = n % 10
            t = t * 10 + temp
            n = int(n / 10)
        return t == x
