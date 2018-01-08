'''
Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = []
        for i,ch in enumerate(s):
            li = []
            for j in s[i:len(s)]:
                #print(j)
                if j not in li:
                    li.append(j)
                else:
                    if len(li) > len(max_length):
                        max_length = li
                    break
        #max_str = str(max_length)
        max_str = ''.join(max_length)
        return max_str

if __name__ == '__main__':
    s = 'adbcdfafa'
    max = Solution()
    max_str = max.lengthOfLongestSubstring(s)
    print(max_str)