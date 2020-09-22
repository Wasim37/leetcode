����1���ݹ�
ʱ�临�Ӷȣ�\mathcal{O}(N)O(N)��ִ���� N/2N/2 �εĽ�����
�ռ临�Ӷȣ�\mathcal{O}(N)O(N)���ݹ������ʹ�õĶ�ջ�ռ䡣
class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)



����2��˫ָ��
ʱ�临�Ӷȣ�\mathcal{O}(N)O(N)��ִ���� N/2N/2 �εĽ�����
�ռ临�Ӷȣ�\mathcal{O}(1)O(1)��ֻʹ���˳������ռ䡣
class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
