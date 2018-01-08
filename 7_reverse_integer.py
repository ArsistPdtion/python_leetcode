class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>0:
            x = str(x)
            x = x[::-1]
            return int(x)
        else:
            x = -x
            x= str(x)
            x = x[::-1]
            x = int(x)
            x = -x
            return x

if __name__ == '__main__':
    mint = Solution()
    print(mint.reverse(123))
    print(mint.reverse(-123))
