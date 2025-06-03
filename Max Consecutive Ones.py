class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        r,c = 0,0
        for i in nums:
            if i == 1:
                c = c + 1
            else:
                c = 0
            r = max(r,c)
        return r
