class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        index = 0
        end = len(nums)

        while index < end:
            nums.append(nums[index])
            index += 1
        return nums