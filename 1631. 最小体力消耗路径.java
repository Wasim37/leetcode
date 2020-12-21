package com.spark.teaching.lecture.service;

import java.util.ArrayList;
import java.util.List;

class Solution {

    class Edge {
        int x;
        int y;
        int val;

        public Edge(int x, int y, int val) {
            this.x = x;
            this.y = y;
            this.val = val;
        }
    }

    public int minimumEffortPath(int[][] heights) {
        List<Edge> edges = new ArrayList<>();
        int m = heights.length;
        int n = heights[0].length;

        // 将每两个相邻的格子之间连接一条边，长度为这两个格子本身权值的差的绝对值；
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int idx = i * n + j;
                if (i > 0) {
                    edges.add(new Edge(idx - n, idx, Math.abs(heights[i][j] - heights[i - 1][j])));
                }
                if (j > 0) {
                    edges.add(new Edge(idx - 1, idx, Math.abs(heights[i][j] - heights[i][j - 1])));
                }
            }
        }
        // 排序，按边的值从小到大排序
        edges.sort((o1, o2) -> o1.val - o2.val);

        UnionFind uf = new UnionFind(m * n);
        for (Edge edge : edges) {
            uf.unoin(edge.x, edge.y);// 合并
            if (uf.connect(0, m * n - 1))
                return edge.val; // 判断
        }
        return 0;
    }

    class UnionFind {
        int[] parents;
        int[] ranks;

        public UnionFind(int n) {
            parents = new int[n];
            ranks = new int[n];
            for (int i = 0; i < n; i++)
                parents[i] = i;
        }

        public int find(int x) {
            if (x != parents[x]) {
                parents[x] = find(parents[x]);
            }
            return parents[x];
        }

        public boolean unoin(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX == rootY) {
                return false;
            }
            if (ranks[rootX] > ranks[rootY]) {
                parents[rootY] = rootX;
            }
            if (ranks[rootX] < ranks[rootY]) {
                parents[rootX] = rootY;
            }
            if (ranks[rootX] == ranks[rootY]) {
                parents[rootY] = rootX;
                ranks[rootY]++;
            }
            return true;
        }

        public boolean connect(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            return rootX == rootY;
        }
    }
    
    public static void main(String[] args) {
        Solution solution = new Solution();
        int [][] a = {{1,2,3},{3,8,4},{5,3,5}};
        int result = solution.minimumEffortPath(a);
        System.out.println(result);
    }

}