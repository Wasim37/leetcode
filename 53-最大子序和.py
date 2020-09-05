# 要点：
# f(i)=max{f(i−1) + ai, ai}
# 正增益，pre_sum只要小于0，就丢弃
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        pre_sum = 0
        for i in range(0, len(nums)):
            if pre_sum > 0:
                pre_sum = pre_sum + nums[i]
            else:
                pre_sum = nums[i]
            sum = max(pre_sum, sum)
        return sum