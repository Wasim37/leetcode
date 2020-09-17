class Solution:
    def isPalindrome(self, s: str) -> bool:
        # isalnum :检测字符串是否由字母和数字组成
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        # 翻转字符串有2种方案
        # return sgood == sgood[::-1]
        return sgood == ''.join(reversed(sgood))
