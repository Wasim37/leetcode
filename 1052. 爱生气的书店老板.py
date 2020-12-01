# 思路：考虑到对于老板不生气的时候，无论使用不使用技能，这些顾客都是满意的，
# 所以可以先进行操作，把不影响技能实施的部分提前记录下并去掉
# 如案例 customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
# customers更新之后变为[0,0,0,2,0,1,0,5]
# 所以我们只需找出当前数组 连续X个的总和 最大值就可以了

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        t = 0
        for i in range(len(grumpy)): 
            if grumpy[i] == 0:
                t += customers[i]
                customers[i] = 0
        # print(t)
        # print(customers)

        # 滑动窗口找连续X个的最大值
        n = sum(customers[:X])  
        m = n
        for i in range(1, len(customers) - X + 1):
            m = m + customers[i + X - 1] - customers[i - 1]
            n = max(m, n)
        return n + t
