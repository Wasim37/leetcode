# result = []
# def backtrack(路径, 选择列表):
#     if 满足结束条件:
#         result.add(路径)
#         return

#     for 选择 in 选择列表:
#         做选择
#         backtrack(路径, 选择列表)
#         撤销选择

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, track):
            # 所有数都填完了
            if len(nums) == len(track):
                # 此处记得使用track[:]或者 track.copy()，不要直接 res.append(track) 
                # append()和pop()操作是在原列表上进行的，所以在res.append()的时候，加入的是track.copy()
                # 否则后续pop()操作会影响到res中的结果，最后返回一个空的二维列表
                res.append(track.copy())
                return

            for i in range(0, len(nums)):
                # 排除不合法的选择
                if nums[i] in track:
                    continue
                
                # 做选择
                track.append(nums[i])
                # print('做选择: ', track)
                # 进入下一层决策树
                backtrack(nums, track)
                # 取消选择
                track.pop()
                # print('取消选择: ', track)
        
        res = []
        track = []
        backtrack(nums, track)
        return res