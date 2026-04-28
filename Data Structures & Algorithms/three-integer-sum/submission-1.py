class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n= len(nums)
        res=set()

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    sum = nums[i]+nums[j]+nums[k]
                    if sum == 0:
                        triple=tuple(sorted([nums[i],nums[j],nums[k]]))
                        res.add(triple)
        return  list(res)