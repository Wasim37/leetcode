# 方法1：““递增的x元子序列”通用解法”
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return 0

        dp = [1 for _ in range(0, len(nums))]
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] == 3:
                return True
        
        return False

# 方法2：trick, 详见：https://leetcode-cn.com/problems/increasing-triplet-subsequence/solution/c-xian-xing-shi-jian-fu-za-du-xiang-xi-jie-xi-da-b/
# 用两个变量 r1, r2 分别记录第一小和第二小的数。然后遍历 nums。只要碰到比 r1 小的数我们就替换掉 r1，碰到比 r1 大但比 r2 小的数就替换 r2。
# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         r1, r2 = sys.maxsize, sys.maxsize
#         for n in nums :
#             if n <= r1 : r1 = n
#             elif n <= r2 : r2 = n
#             else : return True
#         return False