class Solution {
    int res = 0;
    Set<String> set = new HashSet<>();

    public int maxUniqueSplit(String s) {
        backstracking(s, 0);
        return res;
    }

    private void backstracking(String s, int begin) {
        // 剪枝：若当前已拆分结果加上剩余字符数小于之前得到的答案，则没有必要再进行下去
        if (set.size() + s.length() - begin <= res) {
            return;
        }
        
        // 触发结束条件：到达字符串尾部，说明拆分完毕
        if (begin == s.length()) {
            if (set.size() > res) {
                res = set.size();
            }
            return;
        }
        
        // 回溯体
        for (int i = begin; i < s.length(); ++i) {
            String substr = s.substring(begin, i + 1);
            // System.out.println(begin + "-" + (i+1) + "-" + set + "-" + substr + "-" + "-" + res);
            
            // 排除不合法的选择
            if (set.contains(substr)) {
                continue;
            }
            
            // 做选择
            set.add(substr);
            // 进入下一层决策树
            backstracking(s, i + 1);
            // 取消选择
            set.remove(substr);
        }
    }
}