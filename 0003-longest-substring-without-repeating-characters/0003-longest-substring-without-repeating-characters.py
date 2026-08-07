class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s)==0):
            return 0
        cur_long=1
        d_set=set()
        l=0
        r=0
        while(r<len(s)):
            if(s[r] not in d_set):
                d_set.add(s[r])
                r+=1
                if(r-l>cur_long):
                    cur_long=r-l
            else:
                while(s[r] in d_set):
                    d_set.discard(s[l])
                    l+=1
        return cur_long

