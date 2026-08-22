class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        piv_swap = 0
        piv = 0

        i = len(nums) - 1
        
        while i - 1 >= 0:

            if nums[i-1] >= nums[i]:
                i -= 1
            else:
                piv = nums[i-1]
                piv_swap = nums[i]
                piv_swap_idx = i

                for j in range(i, len(nums)):
                    if  piv < nums[j] <= piv_swap:
                        piv_swap = nums[j]
                        piv_swap_idx = j
                
                nums[piv_swap_idx] = piv
                nums[i-1] = piv_swap

                break

        left = i
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
                
        