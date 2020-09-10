class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(nums, track):
            # 所有数都填完了
            if len(nums) == len(track):
                # 此处记得使用track[:]或者拷贝，不要直接 res.append(track)
                res.append(track[:])
                return

            for i in range(0, len(nums)):
                # 排除不合法的选择
                if nums[i] in track:
                    continue

                # 做选择
                track.append(nums[i])
                print('做选择: ', track)
                # 进入下一层决策树
                backtrack(nums, track)
                # 取消选择
                track.pop()
                print('取消选择: ', track)

        res = []
        track = []
        backtrack(nums, track)
        return res


s = Solution()
print(s.permute([1, 2, 3]))

