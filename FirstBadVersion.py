# Problem num.278
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while(left < right):
            version = (left + right)//2
            if isBadVersion(version):
                right = version #if it is bad then this could be the first bad version
            elif not isBadVersion(version):
                left = version+1 #if it is good then the first bad version must be after this
        return left
