class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=sorted(nums)
        ret=[]
        d={}
        for i in range(len(l)):
            if l[i] not in d:
                d[l[i]]=i
        for i in range(len(nums)):
            ret.append(d[nums[i]])
        return ret