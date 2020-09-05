class Solution:
    def palindrome(self, s: str, left: str, right: str) -> str:
        # 使用双指针，从中间开始向两边扩散来判断回文串
        # print('old', left, right)
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1
#         print('new', left, right)
        return s[left+1:right]

    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(0, len(s)):
            s1 = self.palindrome(s, i, i)
            s2 = self.palindrome(s, i, i + 1)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
            # print('i:', i ,'s1:', s1, 's2:', s2, 'res', res)
        return res
