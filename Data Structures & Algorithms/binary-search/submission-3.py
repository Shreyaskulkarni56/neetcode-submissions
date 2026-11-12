class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] and nums[j]== target:
                    return nums[i]
        return -1