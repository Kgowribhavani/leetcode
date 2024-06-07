class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right=0, x
        res=0
        while left<=right:
            m=left+ ((right-left)//2)
            
            if m**2>x:
                right=m-1
                
            elif m**2<x :
                left=m+1
                res=m
                
            else:
                return m
        
        return res
