---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Übersicht zur Pydantic-Datenvalidierung
translated: true
type: note
---

### Pydantic-Bibliothek
Pydantic ist eine beliebte Open-Source-Python-Bibliothek zur Datenvalidierung und -analyse. Sie nutzt die Typ-Hinweise von Python, um Eingabedaten (wie JSON oder Wörterbücher) automatisch anhand definierter Schemata zu validieren, Typen nach Möglichkeit zu konvertieren und klare Fehler bei Nichtübereinstimmungen zu melden. Beispielsweise stellt sie sicher, dass ein Ganzzahlfeld nicht als Zeichenkette übergeben wird, sofern nicht anders angegeben. Sie wird häufig in Web-Frameworks wie FastAPI für die Behandlung von API-Anfragen und -Antworten verwendet.

-   **Wichtige Merkmale**: Unterstützt komplexe Typen (z. B. Enums, Unions), benutzerdefinierte Validatoren sowie Serialisierung und Deserialisierung.
-   **Installation und Verwendung**: Installation via `pip install pydantic`. Einfaches Beispiel:
    ```python
    from pydantic import BaseModel

    class User(BaseModel):
        id: int
        name: str

    user = User(id='123', name='Alice')  # Wandelt '123' in int um
    print(user.dict())  # Ausgabe: {'id': 123, 'name': 'Alice'}
    ```

### Pydantic-Core
Pydantic-core ist die zugrunde liegende Hochleistungs-Engine von Pydantic. Es ist in Rust (über PyO3-Bindungen) geschrieben, um eine schnelle Datenvalidierung zu bieten, die viel schneller ist als reine Python-Implementierungen. Es ist nicht für die direkte Verwendung durch Benutzer gedacht – stattdessen wird es automatisch von Pydantic aufgerufen. Diese Trennung ermöglicht eine einfachere Wartung und Optimierungen, wie die Behandlung von Grenzfällen bei der Typumwandlung, ohne die Hauptbibliothek zu verlangsamen.

-   **Beziehung zu Pydantic**: Man kann sich Pydantic als die benutzerfreundliche API-Hülle um Pydantic-core vorstellen. Upgrades für Pydantic-core verbessern die Leistung, ohne öffentliche APIs zu ändern.
-   **Warum es wichtig ist**: Leistungstests zeigen, dass Pydantic-core die Validierung 10- bis 100-mal schneller macht als Alternativen wie Marshmallow oder Django Forms.

### Typisierung in Python
Das Modul `typing` ist Teil der Standardbibliothek von Python (hinzugefügt in Python 3.5+ via PEP 484) und bietet Werkzeuge zum Hinzufügen von Typ-Hinweisen zum Code. Diese Hinweise erzwingen zur Laufzeit keine Regeln, verbessern aber die Lesbarkeit des Codes, ermöglichen IDE-Unterstützung (z. B. Autovervollständigung, Fehlererkennung) und erlauben es statischen Typprüfern wie mypy, Fehler frühzeitig zu erkennen.

-   **Häufige Komponenten**: Enthält `List[str]` für Listen von Zeichenketten, `Union[int, str]` für mehrere Typen, `Optional[int]` für `int | None` und Generika wie `Dict[str, Any]`.
-   **Beziehung zu Pydantic**: Pydantic baut direkt auf `typing`-Annotationen auf. Ein Modell wie `class Model(BaseModel): x: int` verwendet `typing`, um Erwartungen zu definieren, und Pydantic validiert entsprechend. Ohne `typing` könnte Pydantic nicht funktionieren, da seine typgesteuerte Validierung auf diesen Hinweisen basiert.

### Wie sie zusammenhängen
Pydantic kombiniert die Hinweise von `typing` mit der Geschwindigkeit von Pydantic-core, um Daten deklarativ zu validieren. Beispielsweise könnte ein API-Endpunkt Pydantic-Modelle verwenden, die mit `typing`-Typen annotiert sind, und sich auf Pydantic-core für eine effiziente Validierung verlassen. Dieses Ökosystem unterstützt moderne Python-Muster wie Dataclasses und asynchrone Frameworks und macht es zu einem Grundpfeiler für typsichere Datenverarbeitung. Für weiterführende Details siehe die offizielle Pydantic-Dokumentation oder GitHub.