# ˼·�����ǵ������ϰ岻������ʱ������ʹ�ò�ʹ�ü��ܣ���Щ�˿Ͷ�������ģ�
# ���Կ����Ƚ��в������Ѳ�Ӱ�켼��ʵʩ�Ĳ�����ǰ��¼�²�ȥ��
# �簸�� customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
# customers����֮���Ϊ[0,0,0,2,0,1,0,5]
# ��������ֻ���ҳ���ǰ���� ����X�����ܺ� ���ֵ�Ϳ�����

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        t = 0
        for i in range(len(grumpy)): 
            if grumpy[i] == 0:
                t += customers[i]
                customers[i] = 0
        # print(t)
        # print(customers)

        # ��������������X�������ֵ
        n = sum(customers[:X])  
        m = n
        for i in range(1, len(customers) - X + 1):
            m = m + customers[i + X - 1] - customers[i - 1]
            n = max(m, n)
        return n + t
