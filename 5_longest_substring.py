'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example:
Input: "cbbd"
Output: "bb"
'''
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxStr = ''
        for i ,ch in enumerate(s):
            print('the i and ch is:',i,ch)
            m = i-1
            n = i+1
            while m>=0 and n<len(s):
                print("jin ru while")
                if s[m] == s[n]:
                    m = m-1
                    n = n+1
                else:
                    print("bu xiang deng1")
                    if n-m-1 > len(maxStr):
                        maxStr = s[m+1:n]
                        print(m+1)
                        print(n-1)
                        print("maxStr:",maxStr)
                        print("s[]:",s[m+1:n-1])
                    break
        return maxStr

if __name__ == '__main__':
    test = Solution()
    str1 = test.longestPalindrome('asdfgfdsawerwrew')
    print('the max str is :',str1)








