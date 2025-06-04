class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        st = set(nums)
        n = len(nums)
        lst = []
        for i in range(1,n+1):
            if i not in st :
                lst.append(i)
        return lst
