class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        for i in range(n,101):
            dig=0
            prodig=1
            temp=i
            while(temp>0):
                dig=temp%10
                prodig*=dig
                temp=temp//10
            if(prodig%t==0):
                return i
