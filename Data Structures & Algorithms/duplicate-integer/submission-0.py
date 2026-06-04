class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_copy = set()
        for num in nums:
            if num in num_copy:
                return True
            num_copy.add(num)
        return False