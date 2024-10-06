class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the number and its index
        num_map = {}
        
        # Iterate through the nums array
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # If complement exists in num_map, return the indices
            if complement in num_map:
                return [num_map[complement], i]
            
            # Otherwise, store the number with its index
            num_map[num] = i