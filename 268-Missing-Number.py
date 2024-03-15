class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if not nums :
            return 0
        if len(nums) == 1 and nums[0] != 0:
            return 0

        for i in range (len(nums)):
            if i !=nums[i]:
                return i
           
        return len(nums)