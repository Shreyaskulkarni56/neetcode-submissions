class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset =set()
        for num in nums:
            if num not in  hashset:
                return False
            hashset.append(num)
        return True 