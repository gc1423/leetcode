"""
给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。

提示：
0 <= s.length <= 5 * 104
s由英文字母、数字、符号和空格组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        >>> Solution().lengthOfLongestSubstring("abcabcbb")
        3
        >>> Solution().lengthOfLongestSubstring("bbbbb")
        1
        >>> Solution().lengthOfLongestSubstring("pwwkew")
        3
        >>> Solution().lengthOfLongestSubstring("")
        0
        """
        i = 0
        l = 0
        while i + l < len(s):
            t = s[i:i + l + 1]
            if len(set(t)) == l + 1:
                l += 1
            else:
                i += 1
        return l


if __name__ == '__main__':
    import doctest

    doctest.testmod()
