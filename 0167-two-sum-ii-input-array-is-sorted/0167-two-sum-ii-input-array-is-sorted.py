class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for i in range(len(numbers)):
            compliment = target-numbers[i]
            if compliment in hashmap:
                return [hashmap[compliment]+1,i+1]
            hashmap[numbers[i]]=i
        return []