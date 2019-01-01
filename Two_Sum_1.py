class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            nums_copy = nums[::]
            nums_copy.remove(i)
            for j in nums_copy:
                if i + j == target:
                    return [nums.index(i), nums_copy.index(j)+1]