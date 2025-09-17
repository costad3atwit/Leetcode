#Track total of "current" subarray
#If total is ever greater than ret, update ret to total (so we are always storing the maximum subarray sum so far)
#If total is ever negative when checking next item, set total to 0 to represent starting a new subarray.
#   Because if current total of the subarray is negative then we either find something better starting at the next item
#   or the best was already found and stored in ret


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curTotal = 0
        ret = nums[0]
        for num in nums:
            if curTotal < 0:
                curTotal = 0
            curTotal += num
            if curTotal > ret:
                ret = curTotal
        return ret
