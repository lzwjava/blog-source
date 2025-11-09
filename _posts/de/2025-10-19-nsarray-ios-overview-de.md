---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Übersicht von NSArray für iOS-Entwicklung
translated: true
type: note
---

### Was ist NSArray?

`NSArray` ist eine Klasse in Apples Foundation-Framework, das Teil des iOS SDK (und macOS, etc.) ist. Es repräsentiert eine unveränderliche, geordnete Sammlung von Objekten, ähnlich einem Array in anderen Sprachen. Das bedeutet, sobald Sie ein `NSArray` erstellt haben, können Sie keine Elemente hinzufügen, entfernen oder ersetzen – Sie können nur daraus lesen. Es wird häufig in Objective-C für die iOS-App-Entwicklung verwendet, um Listen von Daten zu speichern und zu verwalten, wie z.B. Benutzereinstellungen, Datenbankabfrageergebnisse oder UI-Elemente.

Wichtige Merkmale:
- **Unveränderlich**: Feste Größe und Inhalte nach der Erstellung (verwenden Sie `NSMutableArray` für veränderbare Versionen).
- **Typsicher für Objekte**: Speichert Zeiger auf Objective-C-Objekte (z.B. `NSString`, `NSNumber`, benutzerdefinierte Klassen). Es unterstützt keine Primitiven direkt – verpacken Sie diese in `NSNumber` oder ähnliches.
- **Indexbasierter Zugriff**: Auf Elemente wird über einen ganzzahligen Index (0-basiert) zugegriffen.
- **Thread-sicher**: Allgemein sicher für gleichzeitige Lesezugriffe, aber nicht für Schreibzugriffe (da es unveränderlich ist).
- **Integration**: Funktioniert nahtlos mit anderen Foundation-Klassen wie `NSDictionary`, `NSString` und Cocoa Touch UI-Komponenten.

In Swift wird `NSArray` zu `Array` gebrückt, aber wenn Sie in Objective-C arbeiten (üblich für Legacy-iOS-Code), verwenden Sie `NSArray` direkt.

### Wie man NSArray in iOS verwendet

So verwenden Sie `NSArray` in einem iOS-Projekt:
1. Importieren Sie das Foundation-Framework (es ist normalerweise standardmäßig in iOS-Apps enthalten).
   ```objc
   #import <Foundation/Foundation.h>
   ```

2. **Ein NSArray erstellen**:
   - Literale Syntax (iOS 6+): `@[object1, object2, ...]`
   - Init-Methode: `[[NSArray alloc] initWithObjects:object1, object2, nil]`
   - Aus einem C-Array: `initWithArray:copyItems:`

   Beispiel:
   ```objc
   NSArray *fruits = @[@"apple", @"banana", @"cherry"];
   // Oder:
   NSArray *numbers = [[NSArray alloc] initWithObjects:@1, @2, @3, nil];
   ```

3. **Auf Elemente zugreifen**:
   - `objectAtIndex:` um ein Element zu erhalten.
   - `count` für die Länge.
   - `firstObject` / `lastObject` für die Ränder.
   - `containsObject:` um die Existenz zu prüfen.

   Beispiel:
   ```objc
   NSString *firstFruit = [fruits objectAtIndex:0]; // "apple"
   NSUInteger count = [fruits count]; // 3
   BOOL hasOrange = [fruits containsObject:@"orange"]; // NO
   ```

4. **Iterieren**:
   - Schnelle Enumeration: `for (id obj in array) { ... }`
   - `enumerateObjectsUsingBlock:` für blockbasierte Iteration (iOS 4+).

   Beispiel:
   ```objc
   for (NSString *fruit in fruits) {
       NSLog(@"Fruit: %@", fruit);
   }
   ```

5. **Gängige Operationen**:
   - Sortieren: `sortedArrayUsingSelector:` oder `sortedArrayUsingComparator:`.
   - Filtern: `filteredArrayUsingPredicate:` (mit NSPredicate).
   - Verbinden: `componentsJoinedByString:` für Strings.
   - In Datei schreiben: `writeToFile:atomically:`.

   Beispiel (Filtern):
   ```objc
   NSPredicate *predicate = [NSPredicate predicateWithFormat:@"length > 5"];
   NSArray *longFruits = [fruits filteredArrayUsingPredicate:predicate];
   // Ergebnisse: @[@"banana", @"cherry"]
   ```

6. **In iOS-Kontexten**:
   - **Tabellenansichten**: Übergeben Sie ein `NSArray` an die Data-Source-Methoden von `UITableView` wie `tableView:numberOfRowsInSection:` (über `count`) und `tableView:cellForRowAtIndexPath:` (über `objectAtIndex:`).
   - **Benutzereinstellungen**: Speichern/Abrufen mit `NSUserDefaults`: `[defaults setObject:array forKey:@"savedItems"];`.
   - **JSON-Verarbeitung**: Konvertieren zu/from `NSData` mit `JSONObjectWithData:options:error:`.

Für veränderbare Bedürfnisse (z.B. dynamisches Hinzufügen von Elementen) wechseln Sie zu `NSMutableArray`:
```objc
NSMutableArray *mutableFruits = [NSMutableArray arrayWithArray:fruits];
[mutableFruits addObject:@"date"];
```

### Tipps
- Prüfen Sie immer auf `nil` oder Grenzen, um Abstürze zu vermeiden: Verwenden Sie `objectAtIndex:` mit Indexvalidierung.
- Leistung: O(1) für Zugriff, O(n) für Suchen.
- Modernes iOS: Ziehen Sie Swifts `Array` für neue Projekte in Betracht – es ist typsicherer.

[NSArray Dokumentation](https://developer.apple.com/documentation/foundation/nsarray)  
[NSMutableArray Dokumentation](https://developer.apple.com/documentation/foundation/nsmutablearray)