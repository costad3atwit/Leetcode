#Problem num.217

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        individuals = set(nums)
        return len(individuals) != len(nums)
