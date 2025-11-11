---
audio: false
generated: true
lang: de
layout: post
title: Programmieren in Assembler
translated: true
type: note
---

Hier folgt ein umfassendes Tutorial für **Teil 2: Programmierung in Assembler**, das die aufgeführten Themen abdeckt: *8086-Befehlssatz (Datenübertragungs-, Arithmetik-, Logik- und Steuerflussbefehle), Programmierung in Assembler (sequenzielle, Verzweigungs- und Schleifenstrukturen) und Interrupt-Service-Routinen*. Dieses Tutorial ist gründlich, zugänglich und praxisnah aufgebaut und setzt auf den Grundlagen von Mikrocomputern (z.B. 8086/8088-Architektur) auf. Es werden Grundkenntnisse über CPU-Register und Speicheradressierung vorausgesetzt.

---

## Teil 2: Programmierung in Assembler

Assembler ist eine Programmiersprache auf niedriger Ebene, die direkte Kontrolle über die Operationen eines Mikroprozessors bietet. Für den Intel 8086/8088 ermöglicht Assembler Programmierern, Anweisungen zu schreiben, die eng an den Maschinencode angelehnt sind und eine feingranulare Kontrolle über Hardware-Ressourcen wie Register, Speicher und E/A-Geräte bieten.

### 1. 8086-Befehlssatz

Der 8086-Befehlssatz ist eine Sammlung von Befehlen, die die CPU versteht, kategorisiert nach ihrer Funktion: **Datenübertragung**, **Arithmetik**, **Logik** und **Steuerfluss**. Jede Anweisung operiert auf Registern, Speicher oder Immediate-Werten unter Verwendung der Adressierungsmodi des 8086 (z.B. Register, direkt, indirekt).

#### a. Datenübertragungsbefehle
Diese Befehle bewegen Daten zwischen Registern, Speicher und Immediate-Werten.

- **MOV (Move)**:
  - Syntax: `MOV Ziel, Quelle`
  - Funktion: Kopiert Daten von der Quelle zum Ziel.
  - Beispiel: `MOV AX, BX` (kopiere BX nach AX); `MOV AX, [1234h]` (kopiere Daten von der Speicheradresse DS:1234h nach AX).
  - Hinweise: Beeinflusst keine Flags; Quelle und Ziel müssen die gleiche Größe haben (8-Bit oder 16-Bit).
- **XCHG (Exchange)**:
  - Syntax: `XCHG Ziel, Quelle`
  - Funktion: Tauscht die Inhalte von Quelle und Ziel.
  - Beispiel: `XCHG AX, BX` (tausche AX und BX).
- **PUSH (Push auf Stack)**:
  - Syntax: `PUSH Quelle`
  - Funktion: Schiebt 16-Bit-Daten auf den Stack, dekrementiert SP um 2.
  - Beispiel: `PUSH AX` (speichere AX auf dem Stack).
- **POP (Pop vom Stack)**:
  - Syntax: `POP Ziel`
  - Funktion: Holt 16-Bit-Daten vom Stack zum Ziel, inkrementiert SP um 2.
  - Beispiel: `POP BX` (stelle BX vom Stack wieder her).
- **LEA (Load Effective Address)**:
  - Syntax: `LEA Ziel, Quelle`
  - Funktion: Lädt die Adresse eines Speicher-Operanden in ein Register.
  - Beispiel: `LEA BX, [SI+4]` (lade Adresse von DS:SI+4 in BX).
- **IN/OUT**:
  - Syntax: `IN Ziel, Port`; `OUT Port, Quelle`
  - Funktion: Überträgt Daten zu/von E/A-Ports.
  - Beispiel: `IN AL, 60h` (Lese Tastatur-Port); `OUT 61h, AL` (Schreibe zum Lautsprecher-Port).

#### b. Arithmetische Befehle
Diese führen mathematische Operationen aus und aktualisieren Flags (z.B. ZF, CF, SF, OF) basierend auf den Ergebnissen.

- **ADD (Addieren)**:
  - Syntax: `ADD Ziel, Quelle`
  - Funktion: Addiert Quelle zu Ziel, speichert Ergebnis in Ziel.
  - Beispiel: `ADD AX, BX` (AX = AX + BX).
- **SUB (Subtrahieren)**:
  - Syntax: `SUB Ziel, Quelle`
  - Funktion: Subtrahiert Quelle von Ziel.
  - Beispiel: `SUB CX, 10` (CX = CX - 10).
- **INC (Inkrementieren)**:
  - Syntax: `INC Ziel`
  - Funktion: Erhöht Ziel um 1.
  - Beispiel: `INC BX` (BX = BX + 1).
- **DEC (Dekrementieren)**:
  - Syntax: `DEC Ziel`
  - Funktion: Verringert Ziel um 1.
  - Beispiel: `DEC CX` (CX = CX - 1).
- **MUL (Multiplizieren, Unsigned)**:
  - Syntax: `MUL Quelle`
  - Funktion: Multipliziert AL (8-Bit) oder AX (16-Bit) mit Quelle, speichert Ergebnis in AX oder DX:AX.
  - Beispiel: `MUL BX` (DX:AX = AX * BX).
- **DIV (Dividieren, Unsigned)**:
  - Syntax: `DIV Quelle`
  - Funktion: Dividiert AX (8-Bit) oder DX:AX (16-Bit) durch Quelle, speichert Quotient in AL/AX, Rest in AH/DX.
  - Beispiel: `DIV BX` (AX = DX:AX / BX, DX = Rest).
- **ADC (Add with Carry)** und **SBB (Subtract with Borrow)**:
  - Funktion: Behandeln Multi-Word-Arithmetik unter Verwendung des Carry-Flags.
  - Beispiel: `ADC AX, BX` (AX = AX + BX + CF).

#### c. Logische Befehle
Diese führen bitweise Operationen aus und manipulieren Binärdaten.

- **AND (Bitweises UND)**:
  - Syntax: `AND Ziel, Quelle`
  - Funktion: Führt bitweises UND aus, speichert Ergebnis in Ziel.
  - Beispiel: `AND AX, 0FFh` (lösche oberes Byte von AX).
- **OR (Bitweises ODER)**:
  - Syntax: `OR Ziel, Quelle`
  - Funktion: Führt bitweises ODER aus.
  - Beispiel: `OR BX, 1000h` (setze Bit 12 in BX).
- **XOR (Bitweises XOR)**:
  - Syntax: `XOR Ziel, Quelle`
  - Funktion: Führt bitweises XOR aus.
  - Beispiel: `XOR AX, AX` (setze AX auf 0).
- **NOT (Bitweises NICHT)**:
  - Syntax: `NOT Ziel`
  - Funktion: Invertiert alle Bits im Ziel.
  - Beispiel: `NOT BX` (BX = ~BX).
- **SHL/SHR (Shift Left/Right)**:
  - Syntax: `SHL Ziel, Anzahl`; `SHR Ziel, Anzahl`
  - Funktion: Schiebt Bits links/rechts, füllt mit 0 (SHR) oder Sign-Bit (SAL/SAR).
  - Beispiel: `SHL AX, 1` (AX = AX * 2).
- **ROL/ROR (Rotate Left/Right)**:
  - Funktion: Rotiert Bits, wobei sie durch das Carry-Flag wandern.
  - Beispiel: `ROL BX, 1` (rotiere BX links um 1 Bit).

#### d. Steuerflussbefehle
Diese ändern die Ausführungsreihenfolge des Programms und ermöglichen Sprünge, Schleifen und Unterprogramme.

- **JMP (Jump)**:
  - Syntax: `JMP Label`
  - Funktion: Springt bedingungslos zu einem Label.
  - Beispiel: `JMP start` (gehe zu Label `start`).
  - Varianten:
    - Kurzer Sprung (±127 Bytes).
    - Naher Sprung (innerhalb des Segments).
    - Ferner Sprung (anderes Segment).
- **Bedingte Sprünge**:
  - Syntax: `Jcc Label` (z.B. JZ, JNZ, JC, JNC)
  - Funktion: Springt basierend auf Flag-Zuständen.
  - Beispiele:
    - `JZ schleife_ende` (springe wenn Zero-Flag gesetzt).
    - `JC fehler` (springe wenn Carry-Flag gesetzt).
    - Häufige Bedingungen: JZ (zero), JNZ (not zero), JS (sign), JO (overflow).
- **LOOP (Schleife)**:
  - Syntax: `LOOP Label`
  - Funktion: Dekrementiert CX, springt zum Label wenn CX ≠ 0.
  - Beispiel: `LOOP verarbeite` (wiederhole bis CX = 0).
  - Varianten:
    - `LOOPE/LOOPZ`: Schleife wenn CX ≠ 0 und ZF = 1.
    - `LOOPNE/LOOPNZ`: Schleife wenn CX ≠ 0 und ZF = 0.
- **CALL (Unterprogrammaufruf)**:
  - Syntax: `CALL Label`
  - Funktion: Schiebt Rückgabeadresse auf den Stack, springt zum Unterprogramm.
  - Beispiel: `CALL berechne_summe` (rufe Unterprogramm auf).
- **RET (Return)**:
  - Syntax: `RET`
  - Funktion: Holt Rückgabeadresse vom Stack, setzt Ausführung fort.
  - Beispiel: `RET` (kehre vom Unterprogramm zurück).
- **INT (Interrupt)**:
  - Syntax: `INT Nummer`
  - Funktion: Löst einen Software-Interrupt aus, ruft eine Interrupt-Service-Routine (ISR) auf.
  - Beispiel: `INT 21h` (DOS-Systemaufruf).
- **IRET (Interrupt Return)**:
  - Funktion: Kehrt von einer ISR zurück, stellt Flags und Rückgabeadresse wieder her.

---

### 2. Programmierung in Assembler

Assemblerprogramme werden als menschenlesbare Anweisungen geschrieben, die in Maschinencode assembliert werden. Der 8086 verwendet ein **segmentiertes Speichermodell**, wobei Code-, Daten- und Stack-Segmente explizit definiert werden.

#### a. Programmstruktur
Ein typisches 8086-Assemblerprogramm enthält:
- **Direktiven**: Anweisungen für den Assembler (z.B. NASM, MASM).
  - `SEGMENT`: Definiert Code-, Daten- oder Stack-Segmente.
  - `ORG`: Setzt Ursprungsadresse.
  - `DB/DW`: Definiert Byte/Word-Daten.
- **Anweisungen**: CPU-Operationen (z.B. MOV, ADD).
- **Labels**: Markieren Positionen für Sprünge oder Daten.
- **Kommentare**: Erklären den Code (z.B. `; Kommentar`).

**Beispielprogrammstruktur (MASM-Syntax)**:
```asm
.model small
.stack 100h
.data
    message db 'Hello, World!$'
.code
main proc
    mov ax, @data    ; Initialisiere DS
    mov ds, ax
    mov dx, offset message ; Lade Nachrichtenadresse
    mov ah, 09h      ; DOS-Funktion: String ausgeben
    int 21h          ; DOS-Interrupt aufrufen
    mov ah, 4Ch      ; Programm beenden
    int 21h
main endp
end main
```

#### b. Sequenzielle Strukturen
Sequenzieller Code führt Anweisungen der Reihe nach aus, ohne Sprünge oder Schleifen.

**Beispiel: Zwei Zahlen addieren**
```asm
mov ax, 5        ; AX = 5
mov bx, 10       ; BX = 10
add ax, bx       ; AX = AX + BX (15)
mov [ergebnis], ax ; Speichere Ergebnis im Speicher
```
- Anweisungen werden nacheinander ausgeführt.
- Üblich für einfache Berechnungen oder Dateninitialisierung.

#### c. Verzweigungsstrukturen
Verzweigungen verwenden bedingte/unbedingte Sprünge, um den Programmfluss basierend auf Bedingungen zu ändern.

**Beispiel: Vergleichen und verzweigen**
```asm
mov ax, 10       ; AX = 10
cmp ax, 15       ; Vergleiche AX mit 15
je gleich        ; Springe wenn AX == 15
mov bx, 1        ; Sonst, BX = 1
jmp fertig
gleich:
    mov bx, 0    ; BX = 0 wenn gleich
fertig:
    ; Programm fortsetzen
```
- **CMP**: Setzt Flags basierend auf Subtraktion (AX - 15).
- **JE**: Springt wenn ZF = 1 (gleich).
- Nützlich für if-then-else-Logik.

#### d. Schleifenstrukturen
Schleifen wiederholen Anweisungen, bis eine Bedingung erfüllt ist, oft unter Verwendung von `LOOP` oder bedingten Sprüngen.

**Beispiel: Summiere Zahlen 1 bis 10**
```asm
mov cx, 10       ; Schleifenzähler = 10
mov ax, 0        ; Summe = 0
summen_schleife:
    add ax, cx   ; Addiere CX zur Summe
    loop summen_schleife ; Dekrementiere CX, schleife wenn CX ≠ 0
    ; AX = 55 (1 + 2 + ... + 10)
```
- `LOOP` vereinfacht zählerbasierte Iteration.
- Alternative: Verwende `CMP` und `JNZ` für benutzerdefinierte Bedingungen.

**Beispiel mit bedingter Schleife**
```asm
mov ax, 0        ; Zähler
mov bx, 100      ; Limit
hochzaehlen:
    inc ax       ; AX++
    cmp ax, bx   ; Vergleiche mit 100
    jle hochzaehlen ; Springe wenn AX <= 100
```
- Flexibel für nicht-zählerbasierte Schleifen.

#### e. Unterprogramme
Unterprogramme modularisieren Code, ermöglichen Wiederverwendung via `CALL` und `RET`.

**Beispiel: Quadriere eine Zahl**
```asm
main:
    mov ax, 4    ; Eingabe
    call quadrat ; Rufe Unterprogramm auf
    ; AX = 16
    jmp ende
quadrat:
    push bx      ; Speichere BX
    mov bx, ax   ; Kopiere AX
    mul bx       ; AX = AX * BX
    pop bx       ; Stelle BX wieder her
    ret          ; Return
ende:
    ; Programm beenden
```
- **PUSH/POP**: Register speichern/wiederherstellen, um Seiteneffekte zu vermeiden.
- Der Stack verwaltet Rückgabeadressen automatisch.

---

### 3. Interrupt-Service-Routinen (ISRs)

Interrupts ermöglichen es der CPU, auf externe oder interne Ereignisse (z.B. Tastatureingabe, Timer-Ticks) zu reagieren, indem das aktuelle Programm pausiert und eine ISR ausgeführt wird.

#### Interrupt-Mechanismus
- **Interrupt-Vektor-Tabelle (IVT)**:
  - Befindet sich im Speicher 0000:0000h–0000:03FFh.
  - Speichert Adressen von ISRs für 256 Interrupt-Typen (0–255).
  - Jeder Eintrag: Segment:Offset (4 Bytes).
- **Typen**:
  - **Hardware-Interrupts**: Ausgelöst durch Geräte (z.B. IRQ).
  - **Software-Interrupts**: Ausgelöst durch `INT`-Befehl (z.B. INT 21h für DOS).
  - **Exceptions**: CPU-Fehler (z.B. Division durch Null).
- **Prozess**:
  1. Interrupt tritt auf.
  2. CPU speichert Flags, CS und IP auf dem Stack.
  3. Springt zur ISR via IVT.
  4. ISR führt aus, endet mit `IRET` zum Wiederherstellen des Zustands.

#### Schreiben einer ISR
ISRs müssen:
- Register erhalten (PUSH/POP).
- Den Interrupt schnell behandeln.
- Mit `IRET` enden.

**Beispiel: Benutzerdefinierte Timer-ISR**
```asm
.data
old_vec dw 2 dup(0) ; Speichere alten Interrupt-Vektor
.code
install_isr:
    cli             ; Deaktiviere Interrupts
    mov ax, 0
    mov es, ax      ; ES = 0 (IVT-Segment)
    mov bx, 1Ch*4   ; Timer-Interrupt (1Ch)
    mov ax, es:[bx] ; Speichere alten Vektor
    mov old_vec, ax
    mov ax, es:[bx+2]
    mov old_vec+2, ax
    mov ax, offset my_isr ; Setze neuen Vektor
    mov es:[bx], ax
    mov ax, cs
    mov es:[bx+2], ax
    sti             ; Aktiviere Interrupts
    ret
my_isr:
    push ax
    inc word ptr [zaehler] ; Inkrementiere Zähler
    pop ax
    iret            ; Return from interrupt
```
- Hängt sich in den Timer-Interrupt (1Ch, ~18.2 Hz).
- Inkrementiert eine Zählvariable.
- Erhält Register und verwendet `IRET`.

**Beispiel: DOS-Interrupt (INT 21h)**
```asm
mov ah, 09h      ; Funktion: String ausgeben
mov dx, offset msg ; Adresse des '$'-terminierten Strings
int 21h          ; DOS aufrufen
```
- INT 21h bietet Betriebssystemdienste (z.B. E/A, Dateibehandlung).
- AH spezifiziert den Funktionscode.

#### Praktische Hinweise
- **Zustand speichern**: ISRs müssen alle Register erhalten, um das Hauptprogramm nicht zu beschädigen.
- **Priorität**: Hardware-Interrupts können andere unterbrechen (verwaltet durch PIC).
- **Debugging**: Verwende Tools wie DEBUG.COM oder moderne Emulatoren (z.B. DOSBox, Bochs).

---

### Beispielprogramm: Fakultätsberechnung
Dieses Programm berechnet die Fakultät einer Zahl (z.B. 5! = 120) unter Verwendung einer Schleife und eines Unterprogramms.

```asm
.model small
.stack 100h
.data
    num dw 5        ; Eingabezahl
    result dw ?     ; Speichere Ergebnis
.code
main proc
    mov ax, @data
    mov ds, ax      ; Initialisiere DS
    mov ax, num     ; Lade Zahl
    call factorial  ; Berechne Fakultät
    mov result, ax  ; Speichere Ergebnis
    mov ah, 4Ch     ; Beenden
    int 21h
main endp
factorial proc
    push bx
    mov bx, ax      ; BX = n
    mov ax, 1       ; AX = Ergebnis
fak_schleife:
    cmp bx, 1
    jle fertig      ; Wenn BX <= 1, beenden
    mul bx          ; AX = AX * BX
    dec bx          ; BX--
    jmp fak_schleife
fertig:
    pop bx
    ret
factorial endp
end main
```
- **Logik**:
  - Eingabe: num = 5.
  - Schleife: AX = AX * BX, BX-- bis BX = 1.
  - Ergebnis: AX = 5 * 4 * 3 * 2 * 1 = 120.
- **Merkmale**:
  - Unterprogramm für Modularität.
  - Stack für Registersicherung.
  - Sequenzielle und Schleifenstrukturen.

---

### Best Practices
1. **Kommentiere Code**: Assembler ist kryptisch; erkläre jeden Schritt.
2. **Minimiere Registerverwendung**: Vermeide unnötiges Überschreiben.
3. **Teste inkrementell**: Verwende Debugger zum Verfolgen der Ausführung.
4. **Behandle Randfälle**: Prüfe auf Overflow, Null oder negative Eingaben.
5. **Optimiere**: Reduziere Anweisungen (z.B. verwende XOR AX, AX statt MOV AX, 0).

---

### Zusammenfassung
- **8086-Befehlssatz**:
  - **Datenübertragung**: MOV, PUSH, POP zum Bewegen von Daten.
  - **Arithmetik**: ADD, SUB, MUL für Berechnungen.
  - **Logik**: AND, OR, XOR für Bitmanipulation.
  - **Steuerfluss**: JMP, LOOP, CALL für Programmfluss.
- **Programmierstrukturen**:
  - **Sequenziell**: Lineare Ausführung für einfache Aufgaben.
  - **Verzweigung**: Bedingte Sprünge für Entscheidungen.
  - **Schleife**: LOOP oder Jcc für Wiederholung.
  - **Unterprogramme**: CALL/RET für modularen Code.
- **Interrupts**:
  - ISRs behandeln Ereignisse via IVT.
  - Zustand erhalten, Ende mit IRET.
  - Verwendet für Hardware (z.B. Timer) und Software (z.B. DOS) Interrupts.

---

### Übungsfragen
1. Schreibe ein Programm, das einen String im Speicher umkehrt.
2. Implementiere ein Unterprogramm, das prüft, ob eine Zahl eine Primzahl ist.
3. Erstelle eine ISR für den Tastatur-Interrupt (INT 09h), um Tastendrücke zu zählen.
4. Erkläre den Unterschied zwischen `JMP` und `CALL`.
5. Optimiere diesen Code: `MOV AX, 0; MOV BX, AX; ADD BX, 5`.

---

Dieses Tutorial behandelt die Grundlagen der 8086-Assemblerprogrammierung, mit Beispielen und Erklärungen zum Aufbau praktischer Fähigkeiten. Wenn du bestimmte Befehle, fortgeschrittene Techniken (z.B. String-Operationen) oder Emulationstools näher erkunden möchtest, lass es mich wissen!