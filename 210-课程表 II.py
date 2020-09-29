class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # �洢����ͼ
        edges = collections.defaultdict(list)
        # ���ÿ���ڵ��״̬��0=δ������1=�����У�2=�����
        visited = [0] * numCourses
        # ��������ģ��ջ���±� 0 Ϊջ�ף�n-1 Ϊջ��
        result = list()
        # �ж�����ͼ���Ƿ��л�
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])
        
        def dfs(u: int):
            nonlocal valid
            # ���ڵ���Ϊ�������С�
            visited[u] = 1
            # ���������ڽڵ�
            # ֻҪ�����л�������ֹͣ����
            for v in edges[u]:
                # �����δ��������ô�������ڽڵ�
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                # ����������С�˵���ҵ��˻�
                elif visited[v] == 1:
                    valid = False
                    return
            # ���ڵ���Ϊ������ɡ�
            visited[u] = 2
            # ���ڵ���ջ
            result.append(u)
        
        # ÿ����ѡһ����δ�������Ľڵ㣬��ʼ���������������
        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        
        if not valid:
            return list()
        
        # ���û�л�����ô������������
        # ע���±� 0 Ϊջ�ף������Ҫ�����鷴�����
        return result[::-1]
