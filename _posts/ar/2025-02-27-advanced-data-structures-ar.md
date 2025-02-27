---
audio: false
lang: ar
layout: post
title: الهيكلات المتقدمة للبيانات في جاڤا
translated: true
---

الهيكلات البيانات هي الأساس للخوارزميات الفعالة. دعونا نستكشف أربعة هياكل قوية: قائمة التخطي، اتحاد-البحث، شجرة AVL، وشجرة الفهرسة الثنائية. هذه الهياكل تستخدم على نطاق واسع في السيناريوهات التي تتطلب بحث سريع، اتحاد، توازن، أو استعلام النطاق.

## 1. قائمة التخطي: بحث احتمالي
قائمة التخطي هي قائمة مرتبة مرتبة على طبقات تسمح بالبحث السريع، الإدراج، والحذف مع معقدية زمنية متوسطة O(log n)، وتقدم بديلاً لشجرة التوازن.

### تنفيذ Java
```java
import java.util.Random;

public class SkipList {
    static class Node {
        int value;
        Node[] next;
        Node(int value, int level) {
            this.value = value;
            this.next = new Node[level + 1];
        }
    }

    private Node head;
    private int maxLevel;
    private Random rand;
    private int level;

    SkipList() {
        maxLevel = 16;
        head = new Node(-1, maxLevel);
        rand = new Random();
        level = 0;
    }

    private int randomLevel() {
        int lvl = 0;
        while (rand.nextBoolean() && lvl < maxLevel) lvl++;
        return lvl;
    }

    void insert(int value) {
        Node[] update = new Node[maxLevel + 1];
        Node current = head;
        for (int i = level; i >= 0; i--) {
            while (current.next[i] != null && current.next[i].value < value) current = current.next[i];
            update[i] = current;
        }
        current = current.next[0];
        int newLevel = randomLevel();
        if (newLevel > level) {
            for (int i = level + 1; i <= newLevel; i++) update[i] = head;
            level = newLevel;
        }
        Node newNode = new Node(value, newLevel);
        for (int i = 0; i <= newLevel; i++) {
            newNode.next[i] = update[i].next[i];
            update[i].next[i] = newNode;
        }
    }

    boolean search(int value) {
        Node current = head;
        for (int i = level; i >= 0; i--) {
            while (current.next[i] != null && current.next[i].value < value) current = current.next[i];
        }
        current = current.next[0];
        return current != null && current.value == value;
    }

    public static void main(String[] args) {
        SkipList sl = new SkipList();
        sl.insert(3);
        sl.insert(6);
        sl.insert(7);
        System.out.println("Search 6: " + sl.search(6));
        System.out.println("Search 5: " + sl.search(5));
    }
}
```
**الخرج:**
```
Search 6: true
Search 5: false
```

