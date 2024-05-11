class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[]
        
        n=len(nums)
        nums.sort()
        while True:
            for i in range(len(nums)):
                if nums[i]==nums[0]:
                    a.append(nums[i])
                    if len(a)>n/2:
                        return nums[0]
            del nums[:len(a)]
                    