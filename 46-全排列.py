# result = []
# def backtrack(·��, ѡ���б�):
#     if �����������:
#         result.add(·��)
#         return

#     for ѡ�� in ѡ���б�:
#         ��ѡ��
#         backtrack(·��, ѡ���б�)
#         ����ѡ��

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, track):
            # ��������������
            if len(nums) == len(track):
                # �˴��ǵ�ʹ��track[:]���� track.copy()����Ҫֱ�� res.append(track) 
                # append()��pop()��������ԭ�б��Ͻ��еģ�������res.append()��ʱ�򣬼������track.copy()
                # �������pop()������Ӱ�쵽res�еĽ������󷵻�һ���յĶ�ά�б�
                res.append(track.copy())
                return

            for i in range(0, len(nums)):
                # �ų����Ϸ���ѡ��
                if nums[i] in track:
                    continue
                
                # ��ѡ��
                track.append(nums[i])
                # print('��ѡ��: ', track)
                # ������һ�������
                backtrack(nums, track)
                # ȡ��ѡ��
                track.pop()
                # print('ȡ��ѡ��: ', track)
        
        res = []
        track = []
        backtrack(nums, track)
        return res