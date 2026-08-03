class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        put = 0

        for i in range(len(nums)):

            if nums[i] != val:
                nums[put] = nums[i]
                put += 1

        return put