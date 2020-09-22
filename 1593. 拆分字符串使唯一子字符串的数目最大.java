class Solution {
    int res = 0;
    Set<String> set = new HashSet<>();

    public int maxUniqueSplit(String s) {
        backstracking(s, 0);
        return res;
    }

    private void backstracking(String s, int begin) {
        // ��֦������ǰ�Ѳ�ֽ������ʣ���ַ���С��֮ǰ�õ��Ĵ𰸣���û�б�Ҫ�ٽ�����ȥ
        if (set.size() + s.length() - begin <= res) {
            return;
        }
        
        // �������������������ַ���β����˵��������
        if (begin == s.length()) {
            if (set.size() > res) {
                res = set.size();
            }
            return;
        }
        
        // ������
        for (int i = begin; i < s.length(); ++i) {
            String substr = s.substring(begin, i + 1);
            // System.out.println(begin + "-" + (i+1) + "-" + set + "-" + substr + "-" + "-" + res);
            
            // �ų����Ϸ���ѡ��
            if (set.contains(substr)) {
                continue;
            }
            
            // ��ѡ��
            set.add(substr);
            // ������һ�������
            backstracking(s, i + 1);
            // ȡ��ѡ��
            set.remove(substr);
        }
    }
}