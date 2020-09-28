class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        index = 0
        cost = 0
        res = -1
        waiting = 0
        bc, rc = 0, 0
        times = 0
        for i, v in enumerate(customers):
            times = i + 1
            rc += runningCost  # 每次都必须转

            waiting += v
            inboard = min(4, waiting)
            bc += boardingCost * inboard
            waiting -= inboard

            if cost < bc - rc:
                cost = bc - rc
                res = times
            index = (index + 1) % 4

        while waiting > 0:  # 清空剩下的游客
            times += 1
            bc += boardingCost * min(4, waiting)
            rc += runningCost
            if cost < bc - rc:
                cost = bc - rc
                res = times
            waiting -= 4

        return res