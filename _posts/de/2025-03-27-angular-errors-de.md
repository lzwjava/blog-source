---
audio: false
generated: true
lang: de
layout: post
title: Angular-Fehler
translated: true
type: note
---

Bei der Arbeit mit Angular stoßen Entwickler häufig auf bestimmte Ausnahmen und Fehler. Nachfolgend finden Sie eine kategorisierte Liste häufiger Probleme, ihrer Ursachen und Lösungen:

---

### **Template & Data Binding Fehler**
1. **`ExpressionChangedAfterItHasBeenCheckedError`**  
   - **Ursache**: Ändern von Komponentendaten nach dem Change Detection-Zyklus von Angular (z.B. in `ngAfterViewInit` oder `ngOnChanges`).  
   - **Lösung**: Verwenden Sie `ChangeDetectorRef.detectChanges()` oder stellen Sie sicher, dass Datenänderungen vor Abschluss der Change Detection erfolgen.

2. **`Cannot read property 'X' of undefined`**  
   - **Ursache**: Zugriff auf nicht initialisierte Objekteigenschaften in Templates (z.B. `{{ user.name }}` wenn `user` `null` ist).  
   - **Lösung**: Verwenden Sie den Safe-Navigation-Operator (`{{ user?.name }}`) oder initialisieren Sie Objekte ordnungsgemäß.

3. **`Can't bind to 'X' since it isn't a known property of 'Y'`**  
   - **Ursache**: Fehlende Komponenten-/Direktivendeklaration oder Tippfehler im Eigenschaftsnamen.  
   - **Lösung**: Importieren Sie die Direktive/Komponente in das Modul oder überprüfen Sie die Schreibweise.

---

### **Dependency Injection (DI) Fehler**
4. **`NullInjectorError: No provider for XService`**  
   - **Ursache**: Service nicht im Modul/Komponente bereitgestellt oder zirkuläre Abhängigkeit.  
   - **Lösung**: Fügen Sie den Service zum `providers`-Array des Moduls/der Komponente hinzu.

5. **`No value accessor for form control`**  
   - **Ursache**: Benutzerdefinierte Form-Control ohne `ControlValueAccessor`-Implementierung oder falsche `formControlName`-Bindung.  
   - **Lösung**: Implementieren Sie `ControlValueAccessor` für benutzerdefinierte Controls oder überprüfen Sie die Formular-Bindungen.

---

### **TypeScript & Build Fehler**
6. **`Type 'X' is not assignable to type 'Y'`**  
   - **Ursache**: Typinkongruenzen (z.B. falscher Datentyp wird an eine Komponente übergeben).  
   - **Lösung**: Stellen Sie sicher, dass die Typen übereinstimmen oder verwenden Sie Type Assertions (falls beabsichtigt).

7. **`ERROR in Cannot find module 'X'`**  
   - **Ursache**: Fehlendes npm-Paket oder falscher Import-Pfad.  
   - **Lösung**: Installieren Sie das Paket (`npm install X`) oder korrigieren Sie den Import-Pfad.

---

### **Komponenten & Modul Fehler**
8. **`Component is not part of any NgModule`**  
   - **Ursache**: Komponente ist nicht in einem Modul deklariert oder Modul nicht importiert.  
   - **Lösung**: Fügen Sie die Komponente zu `declarations` in ihrem Modul hinzu oder importieren Sie das Modul.

9. **`ViewDestroyedError: Attempt to use a destroyed view`**  
   - **Ursache**: Subscriptions oder asynchrone Operationen, die nach der Zerstörung der Komponente ausgeführt werden.  
   - **Lösung**: Kündigen Sie Subscriptions in `ngOnDestroy` oder verwenden Sie den `async` Pipe.

---

### **HTTP & API Fehler**
10. **`HttpClient provider not found`**  
    - **Ursache**: Fehlender `HttpClientModule`-Import im Modul.  
    - **Lösung**: Importieren Sie `HttpClientModule` in `AppModule`.

11. **CORS Probleme**  
    - **Ursache**: Backend erlaubt keine Anfragen von der Frontend-Origin.  
    - **Lösung**: Konfigurieren Sie CORS auf dem Server oder verwenden Sie einen Proxy in Angular (`proxy.conf.json`).

---

### **Routing Fehler**
12. **`Route not found`**  
    - **Ursache**: Falsche Routendefinition oder fehlendes Lazy-Loaded-Modul.  
    - **Lösung**: Überprüfen Sie die Routen-Pfade und die Lazy-Load-Syntax (`loadChildren: () => import(...)`).

---

### **Formular Fehler**
13. **`FormControl not found`**  
    - **Ursache**: Verwendung von `formControlName` ohne Einbettung in eine `[formGroup]`.  
    - **Lösung**: Stellen Sie sicher, dass die übergeordnete FormGroup initialisiert und gebunden ist.

---

### **Verschiedenes**
14. **`Maximum call stack size exceeded`**  
    - **Ursache**: Rekursive Funktionen oder zirkuläre Abhängigkeiten.  
    - **Lösung**: Refaktorisieren Sie den Code, um Rekursionen/zirkuläre Referenzen zu eliminieren.

15. **`Zone.js Promise rejection`**  
    - **Ursache**: Nicht behandelte Promise-Rejections.  
    - **Lösung**: Fügen Sie `.catch()` hinzu oder verwenden Sie `try/catch` mit `async/await`.

16. **AOT Kompilierungsfehler**  
    - **Ursache**: Template-Syntax nicht kompatibel mit Ahead-of-Time-Kompilierung.  
    - **Lösung**: Vermeiden Sie komplexe Ausdrücke in Templates oder verwenden Sie eine Angular-kompatible Syntax.

---

### **Best Practices zur Fehlervermeidung**
- Verwenden Sie den `async` Pipe für Observables, um automatisch zu kündigen.
- Aktivieren Sie strikte TypeScript-Prüfungen (`strict: true` in `tsconfig.json`).
- Führen Sie `ng lint` aus, um Code-Qualitätsprobleme zu erkennen.
- Testen Sie mit dem `--prod` Flag, um AOT-Builds zu simulieren.

Indem Sie diese häufigen Probleme methodisch angehen, können Sie die Angular-Entwicklung optimieren und die Debugging-Zeit reduzieren.