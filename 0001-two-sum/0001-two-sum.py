class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for i in range(len(nums)):
            compliment = target-nums[i]
            if compliment in hashmap:
                return [i, hashmap[compliment]]
            hashmap[nums[i]]=i
        return []



        

        
        