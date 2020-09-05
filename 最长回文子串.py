class Solution:
    def palindrome(self, s: str, left: str, right: str) -> str:
        print('old', left, right)
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1
        print('new', left, right)
        sss = s[left+1:right]
        print('sss', sss)
        return sss

    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(0, len(s)):
            s1 = self.palindrome(s, i, i)
            s2 = self.palindrome(s, i, i + 1)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
            print(res)
        return res


s = Solution()
print(s.longestPalindrome('sabaabcba'))
