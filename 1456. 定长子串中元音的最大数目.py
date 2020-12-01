class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_character = ['a', 'e', 'i', 'o', 'u']

        left = 0
        total_sum = 0
        max_sum = float("-inf") # 负无穷大
        
        # 初始化max_sum
        for right in range(0, k):
            if s[right] in vowel_character:
                total_sum = total_sum + 1
        max_sum = total_sum

        # 提前返回
        if total_sum == k:
            return k
        
        # 双指针
        for right in range(k, len(s)):
            if s[right] in vowel_character:
                total_sum = total_sum + 1
            if s[left] in vowel_character:
                total_sum = total_sum - 1
            left += 1
            if total_sum >= max_sum:
                max_sum = total_sum
            
            # 提前返回
            if max_sum == k:
                return k
        
        return max_sum