'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''
class Solution:
    def insertListSort(self,nums1,nums2):
        for i in nums1:
            for j in range(len(nums2)):
                if i < nums2[j]:
                    nums2.insert(j,i)
                    break

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = []
        if nums1[len(nums1)-1] < nums2[0]:
            nums3 = nums1 + nums2
        elif nums1[0] > nums2[len(nums2)-1]:
            nums3 = nums2 + nums1
        else:
            if len(nums1) > len(nums2):
                self.insertListSort(nums2,nums1)
                nums3 = nums1
            else:
                self.insertListSort(nums1, nums2)
                nums3 = nums2
        str_len = len(nums3)
        print(nums3)
        print(str_len)
        if str_len % 2 == 0:
            mid_num = (nums3[int(str_len/2-1)] + nums3[int(str_len/2)])/2
        else:
            mid_num = nums3[int((str_len-1)/2)]
        return mid_num


if __name__ == '__main__':
    li1 = [1,5,7]
    li2 = [2,4,6,8]
    li = Solution()
    li3 = li.findMedianSortedArrays(li1,li2)
    print(li3)