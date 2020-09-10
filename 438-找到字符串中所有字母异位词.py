from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ''' 滑动窗口
        '''
        res = [] # 记录结果
        window = {}     # 记录窗口中各个字符数量的字典
        need = {}      # 记录目标字符串中各个字符数量的字典
        for c in p:
            need[c] = need.get(c, 0) + 1  # 统计目标字符串的信息

        left = right = 0
        valid = 0
        while right < len(s):
            c = s[right]
            right += 1
            
            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩
            while right - left >= len(p):
                # 当窗口符合条件时，把起始索引加入 res
                if valid == len(need):
                    res.append(left)
                d = s[left]
                left += 1
                # 进行窗口内数据的一系列更新
                # 注意：左部收缩和窗口右移时的逻辑对称
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] = window.get(d, 0) - 1
                # print(window)
        return res