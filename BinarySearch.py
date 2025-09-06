#Problem num.704
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        index = (right+left)//2
        while left<=right:
            if nums[index] == target:
                return index
            elif target > nums[index]:
                left = index + 1
                index = (right+left)//2
            else:
                right = index -1
                index = (right+left)//2
        return -1
