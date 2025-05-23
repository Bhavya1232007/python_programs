class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = set(nums)
        max = 0
        n = len(nums)
        for a in s:
            if max < nums.count(a):
                max = nums.count(a)
                max_ele = a
                if max > n/2:
                    break
                   
        return max_ele

            
        
    
    


