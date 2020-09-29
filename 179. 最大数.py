# 重载比较运算符 lt(less than)
# 将数组中所有元素类型改为字符串
# 对数组排序，key 为重载后的 lt
# 将排序后的数组拼接起来输出
# 如果第一个元素就为 ‘0’，说明所有元素均为 ‘0’，则返回 ‘0’


class StrLt(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strn = [str(n) for n in nums]
        strn.sort(key=StrLt)
        return ''.join(strn) if strn[0] != '0' else '0'
