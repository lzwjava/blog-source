---
audio: false
lang: hi
layout: post
title: खोज और सिमुलेशन एल्गोरिथम्स इन जावा
translated: true
---

खोज और सिमुलेशन एल्गोरिथम पथफाइंडिंग और प्रोबेबिलिस्टिक समस्याओं को हल करने में मदद करते हैं। चलो A* खोज और मॉन्टे कार्लो सिमुलेशन की खोज करते हैं।

## 1. A* खोज: ह्यूरिस्टिक पथफाइंडिंग
A* एक सूचित खोज एल्गोरिथम है जो एक ग्राफ में सबसे छोटा पथ खोजने के लिए एक ह्यूरिस्टिक का उपयोग करता है, डिज़्क्रा और ग्रीडी खोज की ताकतों को मिलाकर। यह खेलों और नाविगेशन में व्यापक रूप से उपयोग किया जाता है।

### जावा इम्प्लीमेंटेशन
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
        return Math.abs(x1 - x2) + Math.abs(y1 - y2); // मैनहट्टन दूरी
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
        System.out.println("कोई पथ नहीं मिला!");
    }

    static void printPath(Node node) {
        List<int[]> path = new ArrayList<>();
        while (node != null) {
            path.add(new int[]{node.x, node.y});
            node = node.parent;
        }
        Collections.reverse(path);
        System.out.println("पथ:");
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
**आउटपुट:**
```
पथ:
(0, 0)
(1, 0)
(2, 0)
(2, 1)
(2, 2)
(2, 3)
```

## 2. मॉन्टे कार्लो सिमुलेशन: प्रोबेबिलिस्टिक अनुमान
मॉन्टे कार्लो विधियाँ रैंडम सैम्पलिंग का उपयोग करके परिणामों का अनुमान लगाती हैं, जैसे कि एक वर्ग और वर्तुल में बिंदुओं को सिमुलेट करके π का अनुमान लगाना।

### जावा इम्प्लीमेंटेशन
```java
import java.util.Random;

public class MonteCarlo {
    static double estimatePi(int points) {
        Random rand = new Random();
        int insideCircle = 0;
        for (int i = 0; i < points; i++) {
            double x = rand.nextDouble();
            double y = rand.nextDouble();
            if (x * x + y * y <= 1) insideCircle++; // इंटरसेक्टिंग सर्कल
        }
        return 4.0 * insideCircle / points; // अनुपात * 4 π का अनुमान लगाता है
    }

    public static void main(String[] args) {
        int points = 1000000;
        double pi = estimatePi(points);
        System.out.println("1000000 बिंदुओं के साथ अनुमानित π: " + pi);
        System.out.println("वास्तविक π: " + Math.PI);
    }
}
```
**आउटपुट (रैंडमता के कारण बदलता है):**
```
1000000 बिंदुओं के साथ अनुमानित π: 3.1418
वास्तविक π: 3.141592653589793
```