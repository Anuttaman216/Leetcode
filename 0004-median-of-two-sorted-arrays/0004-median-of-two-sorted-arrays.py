class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i=0
        j=0
        l1=[]
        med=0
        mid=0
        while(i<len(nums1) and j<len(nums2)):
            if(nums1[i]<nums2[j]):
                l1.append(nums1[i])
                i+=1
            else:
                l1.append(nums2[j])
                j+=1
        while(i<len(nums1)):
            l1.append(nums1[i])
            i+=1
        while(j<len(nums2)):
            l1.append(nums2[j])
            j+=1
        if(len(l1)%2==1):
            med=l1[len(l1)/2]
        else:
            mid=len(l1)//2
            med=(l1[mid]+l1[mid-1])/2.0
        return med
        