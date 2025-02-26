---
audio: false
lang: fr
layout: post
title: Algorithmes de Recherche et de Simulation en Java
translated: true
---

Les algorithmes de recherche et de simulation abordent les problèmes de recherche de chemin et probabilistes. Explorons la recherche A* et la simulation de Monte Carlo.

## 1. Recherche A*: Recherche de chemin heuristique
A* est un algorithme de recherche informée qui utilise une heuristique pour trouver le chemin le plus court dans un graphe, combinant les forces de Dijkstra et de la recherche gloutonne. Il est largement utilisé dans les jeux et la navigation.

### Implémentation en Java
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
        return Math.abs(x1 - x2) + Math.abs(y1 - y2); // Distance de Manhattan
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
        System.out.println("Aucun chemin trouvé!");
    }

    static void printPath(Node node) {
        List<int[]> path = new ArrayList<>();
        while (node != null) {
            path.add(new int[]{node.x, node.y});
            node = node.parent;
        }
        Collections.reverse(path);
        System.out.println("Chemin:");
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
**Sortie:**
```
Chemin:
(0, 0)
(1, 0)
(2, 0)
(2, 1)
(2, 2)
(2, 3)
```

## 2. Simulation de Monte Carlo: Estimation probabiliste
Les méthodes de Monte Carlo utilisent l'échantillonnage aléatoire pour estimer les résultats, comme l'approximation de π en simulant des points dans un carré et un cercle.

### Implémentation en Java
```java
import java.util.Random;

public class MonteCarlo {
    static double estimatePi(int points) {
        Random rand = new Random();
        int insideCircle = 0;
        for (int i = 0; i < points; i++) {
            double x = rand.nextDouble();
            double y = rand.nextDouble();
            if (x * x + y * y <= 1) insideCircle++; // À l'intérieur du cercle unité
        }
        return 4.0 * insideCircle / points; // Rapport * 4 approxime π
    }

    public static void main(String[] args) {
        int points = 1000000;
        double pi = estimatePi(points);
        System.out.println("π estimé avec " + points + " points: " + pi);
        System.out.println("π réel: " + Math.PI);
    }
}
```
**Sortie (varie en raison de l'aléatoire):**
```
π estimé avec 1000000 points: 3.1418
π réel: 3.141592653589793
```