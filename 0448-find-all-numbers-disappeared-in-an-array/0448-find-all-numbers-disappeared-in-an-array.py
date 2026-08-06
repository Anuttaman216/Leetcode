class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        l=[]
        for i in nums : 
            if i not in d:
                d[i]=1
        for j in range(1,len(nums)+1):
            if j not in d:
                l.append(j)
        return l