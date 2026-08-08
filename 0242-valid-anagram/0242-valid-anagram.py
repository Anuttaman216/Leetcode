class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s)!=len(t)):
            return False
        else:
            d={}
            for i in s:
                    d[i]=d.get(i,0)+1
            for j in t:
                if j not in d:
                    return False
                d[j]-=1
                if(d[j]<0):
                    return False
            return True