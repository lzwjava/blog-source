---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Kauf- und Verkaufssignale fehlen auf Jahrescharts
translated: true
type: note
---

### Problem mit Kauf-/Verkaufssignalen im K-Line-Chart der Tiger Trade Global Mobile App

Es klingt, als ob Sie ein Anzeigeproblem haben, bei dem Kauf-/Verkaufssignale (z. B. technische Indikatoren für Handelssignale wie RSI-Kreuzungen oder MACD-Signale oder möglicherweise Markierungen aus dem Trade Feed für Kauf-/Verkaufsvolumen/-ausführungen) in wöchentlichen oder monatlichen K-Line-Charts erscheinen, in der Jahresansicht jedoch verschwinden. In der Tiger Trade App (Version 9.4.0.2, Stand September 2025) könnte dieses Verhalten auf Designeinschränkungen der App zurückzuführen sein – längere Zeiträume wie die Jahresansicht haben weniger Datenpunkte (z. B. aggregiert in monatlichen Candles), was dazu führen kann, dass Indikatoren nicht korrekt berechnet werden, überladen wirken oder ganz ausgeblendet werden, um Ungenauigkeiten zu vermeiden.

### Warum das passiert:
- **Daten-Granularität**: In Jahrescharts repräsentieren die K-Lines Monate oder Jahre, daher können technische Indikatoren (z. B. RSI, das ~14 Datenpunkte benötigt) aufgrund unzureichender Balken keine Signale auslösen. Kürzere Zeiträume (wöchentlich/monatlich) haben mehr Balken, was klare Signale ermöglicht.
- **App-Einstellungen**: In mobilen Versionen sind Kauf-/Verkaufssignale aus dem "Trade Feed" (Echtzeit-Kauf-/Verkaufsvolumen-Ticks oder Indikatoren) für kürzere Zeiträume in Kurs-/Seiten-Charts aktiviert, um eine Überlastung zu verhindern. Updates wie 9.2.4 haben Trade-Feed-Signale hinzugefügt, aber diese sind standardmäßig möglicherweise nur für Intraday-/Wochen-/Monatsansichten aktiviert [1].
- **Performance-/UI-Gründe**: Die Anzeige dichter Signale in Jahresansichten könnte die App verlangsamen oder Benutzer verwirren, daher werden sie bedingt ausgeblendet.

### Wie man das Problem löst oder umgeht:
1.  **Zeitrahmen wechseln, wie Sie es bereits getan haben**: Für zuverlässige Kauf-/Verkaufssignale bleiben Sie bei wöchentlichen oder monatlichen Ansichten im K-Line-Chart. Tippen Sie im Chart-Tab auf der Aktienseite auf den Zeitraum-Auswähler (z. B. "W" für Woche oder "M" für Monat), um umzuschalten – die Signale sollten wieder erscheinen.

2.  **Indikator-Einstellungen überprüfen**:
    - Öffnen Sie die Aktienseite > Chart/K-Line-Tab.
    - Tippen Sie auf das Bearbeiten/Einstellungen-Symbol (⚙️ oder Schraubenschlüssel) im Chart.
    - Stellen Sie sicher, dass Ihre Indikatoren (z. B. RSI, MACD) aktiviert sind. Wenn die Signale im Jahreszeitraum weiterhin ausgeblendet werden, schränkt die App diese möglicherweise ein – versuchen Sie, sie erneut hinzuzufügen oder den Cache unter Profil > Einstellungen > Cache leeren zu löschen.

3.  **Trade-Feed-Signale aktivieren (falls zutreffend)**:
    - In der neuesten Version 9.4.0.2 wird der Trade Feed (Kauf-/Verkaufsvolumen-Indikatoren, die auf den K-Lines überlagert sind) möglicherweise nicht im Jahreszeitraum angezeigt. Gehen Sie zu Profil > Einstellungen > Kurse oder Chart-Einstellungen, um "Trade Feed anzeigen" umzuschalten, falls verfügbar (neuere Updates betonen dies bei Zeitraum-Charts [1]).
    - Wenn es sich um Markierungen für ausgeführte Trades (Punkte/Linien im Chart) handelt, zeigt die Mobile App diese generell nicht in Charts an; überprüfen Sie stattdessen den Tab "Positionen" oder "Orders" für ausgeführte Käufe/Verkäufe.

4.  **App-Update und Tipps**:
    - Stellen Sie sicher, dass Sie Version 9.4.0.2 verwenden (prüfen Sie unter Profil > Über in der App). Ältere Versionen können Fehler haben; aktualisieren Sie über den App Store.
    - Wenn die Signale hartnäckig verschwinden, starten Sie die App neu oder melden Sie sich ab/an. Für die Desktop-Version von Tiger Trade können Sie die vollständige Anzeige von Markierungen über die Chart-Einstellungen aktivieren, aber in der Mobile App fehlt diese Option [2] [3].
    - Für benutzerdefinierte Indikatoren wie Kauf-/Verkaufspfeile besuchen Sie support.tiger.com für Mobile-FAQs – die Apps unterstützen auf Mobilgeräten keine selbstgeschriebenen Indikatoren.

Wenn das Problem bestehen bleibt oder Sie Signale speziell in Jahrescharts benötigen, kontaktieren Sie den Tiger Brokers Support über die App (Profil > Hilfe) oder die Foren, da es sich um einen Bug in der globalen Mobile-Version handeln könnte. Für detaillierte Anleitungen zu Indikatoren sehen Sie sich das Video "Adding Indicators to the K Chart" auf YouTube an [4].

Zitate:
[1] https://www.itiger.com/about/app/update
[2] https://support.tiger.com/english/frequently-asked-questions/questions-about-indicators
[3] https://support.tiger.com/english/windows/chart/chart-settings
[4] https://www.youtube.com/watch?v=5xgmRavEkFE