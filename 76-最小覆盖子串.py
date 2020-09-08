class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        # python中defaultdict用法详解
        from collections import defaultdict
        lookup = defaultdict(int)
        for c in t:
            # 默认值为0.初始化为1，代表
            lookup[c] += 1
        # print(lookup)
        
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
            # 同时维护 counter 的值
            while counter == 0:
                if min_len > end - start:
                    min_len = end - start
                    res = s[start:end]
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1
        return res