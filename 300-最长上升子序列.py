# 使用一维dp解题
# dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度。
# 我们已经知道了 dp[0...4] 的所有结果，我们如何通过这些已知结果推出 dp[5] 呢？
# 根据刚才我们对 dp 数组的定义，现在想求 dp[5] 值，也就是想求以 nums[5] 为结尾的最长递增子序列。
# nums[5] = 3，既然是递增子序列，我们只要找到前面那些结尾比 3 小的子序列，
# 然后把 3 接到最后，就可以形成一个新的递增子序列，而且这个新的子序列长度加一。
# 参考：https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247484498&amp;idx=1&amp;sn=df58ef249c457dd50ea632f7c2e6e761&source=41#wechat_redirect

class Solution:
    def lengthOfLIS(self, nums) -> int:
        if len(nums) == 0:
            return 0

        dp = [1 for _ in range(0, len(nums))]
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)