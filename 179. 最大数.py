# ���رȽ������ lt(less than)
# ������������Ԫ�����͸�Ϊ�ַ���
# ����������key Ϊ���غ�� lt
# ������������ƴ���������
# �����һ��Ԫ�ؾ�Ϊ ��0����˵������Ԫ�ؾ�Ϊ ��0�����򷵻� ��0��


class StrLt(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strn = [str(n) for n in nums]
        strn.sort(key=StrLt)
        return ''.join(strn) if strn[0] != '0' else '0'
