'''
1. 首先需要丢弃字符串前面的空格；
2. 然后可能有正负号（注意只取一个，如果有多个正负号，那么说这个字符串是无法转换的，返回0。比如测试用例里就有个“+-2”）；
3. 字符串可以包含0~9以外的字符，如果遇到非数字字符，那么只取该字符之前的部分，如“-00123a66”返回为“-123”；
4. 如果超出int的范围，返回边界值（2147483647或-2147483648）。
'''


class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        #whether there are more than one '+'、'-'
        if '-' or '+' not in s:
            if s.index('-') == s.rindex('-')  or s.index('+') == s.rindex('+'):
                s = s.lstrip()
                flag = 0
                rstr = ''
                for i,ch in enumerate(s):
                    if ch == '-':
                        flag = 1
                    elif ch in ['0','1','2','3','4','5','6','7','8','9']:
                        rstr += ch
                rstr = int(rstr)
                if flag == 1:
                    rstr = -rstr
                return rstr
            else:
                return "Cannot convert"

if __name__ == '__main__':
    mint = Solution()
    print(mint.myAtoi('4344234afas-'))

