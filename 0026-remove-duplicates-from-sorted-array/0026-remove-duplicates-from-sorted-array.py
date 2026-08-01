class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 1
        put = 0
        is_put = True

        i = 0

        while i < len(nums) - 1:

            last_val = nums[i]

            if nums[i] == nums[i+1]:
                if put and (nums[i] > nums[put-1]):
                    nums[put] = nums[i]
                    put += 1
                if is_put:
                    put = i + 1
                    is_put = False
                i += 2
            else:
                if put:
                    if nums[i] > nums[put-1]:
                        nums[put] = nums[i]
                        put += 1
                
                    if nums[i+1] > nums[put-1]:
                        nums[put] = nums[i+1]
                        put += 1
                i += 1
            
            if i < len(nums):
                if last_val != nums[i]:
                    k += 1
            else:
                return k

        if put and i == len(nums) - 1:
            if nums[i] != nums[i-1]:
                nums[put] = nums[i]

        return k

