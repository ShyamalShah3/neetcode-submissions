class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for i,num in enumerate(nums):
            x = target - num
            if x in seen:
                return [seen[x],i]
            seen[num] = i