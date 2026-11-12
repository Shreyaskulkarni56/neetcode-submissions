class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        for i in range(n):
                if nums[i]== target:
                    return nums[i]
        return -1