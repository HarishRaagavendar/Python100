class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        nums[:]=[num for num in nums if num!=val]
        k=len(nums)
        return k
