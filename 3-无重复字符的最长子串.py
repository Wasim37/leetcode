class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        lookup = defaultdict(int)
        start = 0
        end = 0
        max_len = 0
        counter = 0
        while end < len(s):
            # 窗口右移
            if lookup[s[end]] > 0:
                counter += 1
            lookup[s[end]] += 1
            end += 1

            # 左边窗口收缩
            # 如果 counter 大于1，表示存在重复字符
            while counter > 0:
                if lookup[s[start]] > 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1

            # 维护最长子串长度
            max_len = max(max_len, end - start)
        return max_len