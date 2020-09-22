方法1：递归
时间复杂度：\mathcal{O}(N)O(N)。执行了 N/2N/2 次的交换。
空间复杂度：\mathcal{O}(N)O(N)，递归过程中使用的堆栈空间。
class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)



方法2：双指针
时间复杂度：\mathcal{O}(N)O(N)。执行了 N/2N/2 次的交换。
空间复杂度：\mathcal{O}(1)O(1)，只使用了常数级空间。
class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
