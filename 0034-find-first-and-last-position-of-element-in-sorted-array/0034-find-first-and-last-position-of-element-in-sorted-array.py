class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        sol = [-1, -1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return sol

        left = 0
        right = len(nums) - 1

        # finding leftmost copy of a target

        while left <= right:

            mid = (left + right) // 2

            if left <= mid <= right:

                if nums[mid] == target:
                    sol[0] = mid
                    right = mid - 1
                
                elif nums[mid] < target:
                    left = mid + 1
                
                else:
                    right = mid - 1
            
            else:
                break

        if sol[0] >= 0:
            left = mid + 1
            right = len(nums) - 1
            sol[1] = sol[0]
        else:
            return sol
        
        # finding rightmost copy of a target

        while left <= right:

            mid = (left + right) // 2

            if nums[left] <= target <= nums[right]:

                if nums[mid] == target:
                    sol[1] = mid
                    left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1
                
                else:
                    right = mid - 1
            
            else:
                break

        return sol


        
            

        