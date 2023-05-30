class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        nums_len = len(nums)
        while i < nums_len:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                nums_len -= 1
            else:
                i += 1
        return nums


nums = [0,1,0,3,12]
print(Solution().moveZeroes(nums))
nums = [0]
print(Solution().moveZeroes(nums))