---
audio: false
lang: hant
layout: post
title: 搜尋與模擬演算法
translated: true
---

搜尋和模擬算法處理路徑查找和概率問題。讓我們探索 A* 搜尋和蒙特卡羅模擬。

## 1. A* 搜尋：啟發式路徑查找
A* 是一種啟發式搜尋算法，使用啟發式來找到圖中的最短路徑，結合了 Dijkstra 和貪婪搜尋的優點。它在遊戲和導航中廣泛使用。

### Java 實現
```java
import java.util.*;

public class AStar {
    static class Node implements Comparable<Node> {
        int x, y, g, h, f;
        Node parent;
        Node(int x, int y) {
            this.x = x;
            this.y = y;
            this.g = 0;
            this.h = 0;
            this.f = 0;
        }
        public int compareTo(Node other) { return this.f - other.f; }
    }

    static int heuristic(int x1, int y1, int x2, int y2) {
        return Math.abs(x1 - x2) + Math.abs(y1 - y2); // 曼哈頓距離
    }

    static void aStarSearch(int[][] grid, int[] start, int[] goal) {
        int rows = grid.length, cols = grid[0].length;
        PriorityQueue<Node> open = new PriorityQueue<>();
        boolean[][] closed = new boolean[rows][cols];
        Node startNode = new Node(start[0], start[1]);
        Node goalNode = new Node(goal[0], goal[1]);
        startNode.h = heuristic(start[0], start[1], goal[0], goal[1]);
        startNode.f = startNode.h;
        open.add(startNode);

        int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!open.isEmpty()) {
            Node current = open.poll();
            if (current.x == goal[0] && current.y == goal[1]) {
                printPath(current);
                return;
            }
            closed[current.x][current.y] = true;
            for (int[] dir : dirs) {
                int newX = current.x + dir[0], newY = current.y + dir[1];
                if (newX >= 0 && newX < rows && newY >= 0 && newY < cols && grid[newX][newY] != 1 && !closed[newX][newY]) {
                    Node neighbor = new Node(newX, newY);
                    neighbor.g = current.g + 1;
                    neighbor.h = heuristic(newX, newY, goal[0], goal[1]);
                    neighbor.f = neighbor.g + neighbor.h;
                    neighbor.parent = current;
                    open.add(neighbor);
                }
            }
        }
        System.out.println("沒有找到路徑！");
    }

    static void printPath(Node node) {
        List<int[]> path = new ArrayList<>();
        while (node != null) {
            path.add(new int[]{node.x, node.y});
            node = node.parent;
        }
        Collections.reverse(path);
        System.out.println("路徑：");
        for (int[] p : path) System.out.println("(" + p[0] + ", " + p[1] + ")");
    }

    public static void main(String[] args) {
        int[][] grid = {
            {0, 0, 0, 0},
            {0, 1, 1, 0},
            {0, 0, 0, 0}
        };
        int[] start = {0, 0}, goal = {2, 3};
        aStarSearch(grid, start, goal);
    }
}
```
**輸出：**
```
路徑：
(0, 0)
(1, 0)
(2, 0)
(2, 1)
(2, 2)
(2, 3)
```

## 2. 蒙特卡羅模擬：概率估計
蒙特卡羅方法使用隨機抽樣來估計結果，例如通過模擬正方形和圓內的點來近似 π。

### Java 實現
```java
import java.util.Random;

public class MonteCarlo {
    static double estimatePi(int points) {
        Random rand = new Random();
        int insideCircle = 0;
        for (int i = 0; i < points; i++) {
            double x = rand.nextDouble();
            double y = rand.nextDouble();
            if (x * x + y * y <= 1) insideCircle++; // 在單位圓內
        }
        return 4.0 * insideCircle / points; // 比例 * 4 近似 π
    }

    public static void main(String[] args) {
        int points = 1000000;
        double pi = estimatePi(points);
        System.out.println("使用 " + points + " 個點估計的 π: " + pi);
        System.out.println("實際 π: " + Math.PI);
    }
}
```
**輸出（因隨機性而變動）：**
```
使用 1000000 個點估計的 π: 3.1418
實際 π: 3.141592653589793
```