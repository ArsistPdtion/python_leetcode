#input；一个列表，一个目标数
#output：一个列表，里面的数据是元祖
#思路:
#1.类似于插入排序

'''
def two_sum(list1,target):
	target_list = []
	for i in range(len(list1)):
		j = i+1
		while j>i and j<len(list1):
			if list1[i] + list1[j] == target:
				target_list.append((i,j))
			j = j+1
			
	return target_list
	

'''

def two_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        list_num = []
        for index,value in enumerate(nums):
            sub = target - value
            if sub in dic:
                #return [dic[sub],index]
                list_num.append((dic[sub],index))
            else:
                dic[value] = index
        return list_num

			

if __name__ == '__main__':
	list1 = [1,5,6,2,8,3,9,4]
	target = 7
	target_list = two_sum(list1,target)
	print(target_list)
	

