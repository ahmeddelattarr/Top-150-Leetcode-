class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_elements=set(nums)
        n=len(nums)-len(unique_elements)
        return n>=1
        