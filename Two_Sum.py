class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list_dict = {}
        for i, element in enumerate(nums):
            answer = target - element
            if answer in list_dict:
                return [list_dict[answer], i]
            else:
                list_dict[element] = i