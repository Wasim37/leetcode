# ����1������������xԪ�����С�ͨ�ýⷨ��
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

# ����2��trick, �����https://leetcode-cn.com/problems/increasing-triplet-subsequence/solution/c-xian-xing-shi-jian-fu-za-du-xiang-xi-jie-xi-da-b/
# ���������� r1, r2 �ֱ��¼��һС�͵ڶ�С������Ȼ����� nums��ֻҪ������ r1 С�������Ǿ��滻�� r1�������� r1 �󵫱� r2 С�������滻 r2��
# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         r1, r2 = sys.maxsize, sys.maxsize
#         for n in nums :
#             if n <= r1 : r1 = n
#             elif n <= r2 : r2 = n
#             else : return True
#         return False