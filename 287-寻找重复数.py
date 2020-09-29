from typing import List

# �ռ任ʱ�䣬��α���nums
# ͨ���������֪�����ַ�����������ȷ��һ���з�Χ������
# https://leetcode-cn.com/problems/find-the-duplicate-number/solution/er-fen-fa-si-lu-ji-dai-ma-python-by-liweiwei1419/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        left = 1
        right = size - 1

        while left < right:
            mid = left + (right - left) // 2

            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            # ���ݳ���ԭ��С�ڵ��� 4 �����ĸ�������ϸ���� 4 ����
            # ��ʱ�ظ�Ԫ��һ�������� [1, 4] ������

            if cnt > mid:
                # �ظ���Ԫ��һ�������� [left, mid] ������
                right = mid
            else:
                # if ������ȷ���Ժ�else ������������� if �ķ���
                # [mid + 1, right]
                left = mid + 1
        return left