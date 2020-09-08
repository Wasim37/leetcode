# 我们只要保证窗口(队列)字符串含有t中字符的个数大于等于t里相应元素个数.如方法一
# 还有一种方法记录队列元素和t中元素的差值,直接看代码,很好理解!
class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        # python中defaultdict用法详解
        from collections import defaultdict
        lookup = defaultdict(int)
        for c in t:
            # 默认值为0.初始化为1，
            # 1，移动窗口不包含
            # 0，移动窗口包含
            lookup[c] += 1
        print(lookup)
        
        start = 0
        end = 0
        min_len = float("inf")
        # counter为0，代表窗口已经包含了全部元素
        counter = len(t)
        res = ""
        while end < len(s):
            # 右移窗口
            if lookup[s[end]] > 0:
                counter -= 1
            lookup[s[end]] -= 1
            end += 1
            
            # 每次右移窗口，判断左侧窗口是否要收缩
            while counter == 0:
                # 维护最小子串
                if min_len > end - start:
                    min_len = end - start
                    res = s[start:end]
                # ?不理解
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1
            print(lookup)
        return res

            
s = Solution()
s.minWindow('ADOBECODEBANC',"ABC")