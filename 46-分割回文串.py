# result = []# def backtrack(路径, 选择列表):#     if 满足结束条件:#         result.add(路径)#         return#     for 选择 in 选择列表:#         做选择#         backtrack(路径, 选择列表)#         撤销选择class Solution:    def partition(self, s: str) -> List[List[str]]:        def backtrack(tmp, j):            if j == len(s) :                res.append(tmp)                        for i in range(j,n):                # 排除不合法的选择                if s[j:i+1] != s[j:i+1][::-1]:                    continue                                backtrack(tmp+[s[j:i+1]],i+1)                res = []        backtrack([], 0)        return res