class Solution:
    def isPalindrome(self, s: str) -> bool:
        # isalnum :����ַ����Ƿ�����ĸ���������
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        # ��ת�ַ�����2�ַ���
        # return sgood == sgood[::-1]
        return sgood == ''.join(reversed(sgood))
