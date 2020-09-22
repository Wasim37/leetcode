class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # zip() —πÀı £¨zip(*) Ω‚—π
        cols = list(zip(*mat))
        res = 0
        for rows in mat:
            if sum(rows) == 1:
                j = rows.index(1)
                if sum(cols[j]) == 1:
                    res += 1
        return res