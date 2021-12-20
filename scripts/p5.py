"""
给你一个字符串 s，找到 s 中最长的回文子串。

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s[:int(len(s)/2)] == s[round(len(s)/2):][::-1]

    def longestPalindrome(self, s: str) -> str:
        """
        >>> Solution().longestPalindrome("babad")
        'bab'
        >>> Solution().longestPalindrome('cbbd')
        'bb'
        >>> Solution().longestPalindrome('a')
        'a'
        >>> Solution().longestPalindrome('ac')
        'a'
        """
        j = len(s)
        res = ''
        while j >= 0:
            i = 0
            while i + j < len(s):
                res = s[i:i+j+1]
                if self.isPalindrome(res):
                    return res
                else:
                    i += 1
            j -= 1
        return res

    def longestPalindrome2(self, s: str) -> str:
        """  动态规划
        >>> Solution().longestPalindrome2("babad")
        'bab'
        >>> Solution().longestPalindrome2('cbbd')
        'bb'
        >>> Solution().longestPalindrome2('a')
        'a'
        >>> Solution().longestPalindrome2('ac')
        'a'
        """
        n = len(s)
        t = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(n):
            t[i][i] = 1
        max_len = 1
        res = s[0]
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                if j > n:
                    break
                if s[i] == s[j] and (j-i < 3 or t[i+1][j-1]):
                    t[i][j] = 1
                    if l > max_len:
                        res = s[i:j+1]
        return res

    def longestPalindrome3(self, s: str) -> str:
        """  中心拓展
        >>> Solution().longestPalindrome3("babad")
        'bab'
        >>> Solution().longestPalindrome3('cbbd')
        'bb'
        >>> Solution().longestPalindrome3('a')
        'a'
        >>> Solution().longestPalindrome3('ac')
        'a'
        """
        n = len(s)
        res = ''
        for i in range(n):
            l1 = self.expend(i, i, s)
            if len(l1) > len(res):
                res = l1
            l2 = self.expend(i, i+1, s)
            if len(l2) > len(res):
                res = l2
        return res

    def expend(self, left, right, s):
        while left >= 0 and right<len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]


if __name__ == '__main__':
    # Solution().longestPalindrome2("babad")

    import doctest
    doctest.testmod()
