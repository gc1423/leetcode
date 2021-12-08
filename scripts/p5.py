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
        """
        >>> Solution().longestPalindrome2("babad")
        'bab'
        >>> Solution().longestPalindrome2('cbbd')
        'bb'
        >>> Solution().longestPalindrome2('a')
        'a'
        >>> Solution().longestPalindrome2('ac')
        'a'
        """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
