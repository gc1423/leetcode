"""
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """ 模拟
        >>> Solution().convert('PAYPALISHIRING', 3)
        PAHNAPLSIIGYIR
        >>> Solution().convert('PAYPALISHIRING', 4)
        PINALSIGYAHRPI
        >>> Solution().convert('A', 1)
        'A'
        """
        if numRows < 1:
            return s
        t = numRows + (numRows - 2)
        strs = [s[i: i+t]for i in range(0, len(s), t)]
        temp = []
        for st in strs:
            temp.append(st[:numRows])
            for i in range(len(st[numRows:])):
                temp.append(' ' * (numRows - i - 2) + st[numRows+i] + ' ' * (i + 1))
        res = []
        for i in range(numRows):
            for each in temp:
                if len(each) > i and each[i].strip():
                    res.append(each[i])
        return ''.join(res)

    def convert2(self, s: str, numRows: int) -> str:
        """ 模拟
        >>> Solution().convert2('PAYPALISHIRING', 3)
        'PAHNAPLSIIGYIR'
        >>> Solution().convert2('PAYPALISHIRING', 4)
        'PINALSIGYAHRPI'
        >>> Solution().convert2('A', 1)
        'A'
        """
        if numRows < 2:
            return s
        res = ['' for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            # print(i)
            res[i] += c
            if i == numRows - 1 or i == 0: flag = -flag
            i += flag
        return ''.join(res)
        # print(res)


if __name__ == '__main__':
    Solution().convert('PAYPALISHIRING', 3)
