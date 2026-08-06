class Solution(object):
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        max_a=0
        min_h=0
        b=0
        i=0
        j=len(h)-1
        while(i<j):
            b=j-i
            min_h=min(h[i],h[j])
            if(min_h*b)>max_a:
                max_a=min_h*b
            if(h[i]<h[j]):
                i+=1
            else:
                j-=1
        return max_a