class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
       i = j = 0
       while j<len(nums):
        if nums[j] != 0:
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            i+=1
        j+=1
