class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y=0
        z=x
        if(x<0):
            return False
        else:
            while(z>0):
                y=y*10+z%10
                z=z//10
        if(y==x):
            return True
        return False
        