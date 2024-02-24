class Solution:
    def findGCD(self, nums: List[int]) -> int:
        m= max(nums)
        s=min(nums)
        for i in range(m,0,-1):
            if m%i==0 and s %i==0:
                return i