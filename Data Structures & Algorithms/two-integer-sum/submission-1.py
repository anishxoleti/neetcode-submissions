class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)): 
            needed_value = target - nums[i]
            if needed_value in seen:
                    return [seen[needed_value], i]
            seen[nums[i]] = i 

            

        