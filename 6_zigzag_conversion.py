'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if(len(s) == 0 or numRows < 2):
            return s
        restr = ''
        lag = 2*(numRows-1)
        for i in range(numRows):
            for j in range(i,len(s),lag):
                restr += s[j]
                if(i>0 and i<numRows-1):
                    t = j + lag -2*i
                    if(t<len(s)):
                        restr += s[t]
        return restr


if __name__ == '__main__':
    zigzag = Solution()
    print(zigzag.convert('PAYPALISHIRING',3))
