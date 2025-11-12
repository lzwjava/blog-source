---
audio: false
generated: true
lang: de
layout: post
title: LinkedHashMap vs. TreeMap
translated: true
type: note
---

Gute Frage! Sowohl `LinkedHashMap` als auch `TreeMap` sind Implementierungen der `Map`-Schnittstelle in Java, aber sie haben **unterschiedliche Ordnungsstrategien** und verwenden **unterschiedliche zugrundeliegende Datenstrukturen**.

### 🌳 `TreeMap`
- **Ordnung**: Sortiert nach der **natürlichen Ordnung** der Schlüssel (oder durch einen benutzerdefinierten `Comparator`, falls bereitgestellt).
- **Datenstruktur**: Basiert auf einem **Red-Black Tree** (eine Art selbstbalancierender binärer Suchbaum).
- **Performance**:
  - `O(log n)` für get/put/remove
  - Sortierte Reihenfolge wird ständig beibehalten
- **Anwendungsfall**: Wenn du **sortierte Schlüssel** benötigst.

### 🔗 `LinkedHashMap`
- **Ordnung**: Behält die **Einfügereihenfolge** bei (oder optional die Zugriffsreihenfolge, falls entsprechend konfiguriert).
- **Datenstruktur**: Basiert auf einer **Hash-Tabelle + verknüpften Liste**.
- **Performance**:
  - `O(1)` für get/put/remove (wie `HashMap`)
  - Leicht erhöhter Speicherverbrauch aufgrund der verknüpften Liste
- **Anwendungsfall**: Wenn dir **die Reihenfolge, in der Einträge hinzugefügt wurden**, wichtig ist.

---

### ✅ Iterator-Reihenfolge
Ja, ihre **Iterator-Reihenfolge wird unterschiedlich** sein:

| Map-Typ        | Iterator-Reihenfolge               |
|----------------|------------------------------------|
| `TreeMap`      | Nach Schlüsseln sortiert           |
| `LinkedHashMap`| Einfügereihenfolge (oder Zugriffsreihenfolge) |

---

### 🔍 Beispiel

```java
Map<String, Integer> treeMap = new TreeMap<>();
Map<String, Integer> linkedMap = new LinkedHashMap<>();

treeMap.put("banana", 2);
treeMap.put("apple", 3);
treeMap.put("cherry", 1);

linkedMap.put("banana", 2);
linkedMap.put("apple", 3);
linkedMap.put("cherry", 1);

System.out.println("TreeMap:");
for (String key : treeMap.keySet()) {
    System.out.println(key);
}

System.out.println("LinkedHashMap:");
for (String key : linkedMap.keySet()) {
    System.out.println(key);
}
```

**Ausgabe:**
```
TreeMap:
apple
banana
cherry

LinkedHashMap:
banana
apple
cherry
```

Lass mich wissen, wenn du eine detailliertere Aufschlüsselung von Performance oder Speichernutzung möchtest.