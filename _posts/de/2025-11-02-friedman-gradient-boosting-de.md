---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Jerome Friedman und Gradient Boosting
translated: true
type: note
---

### Einführung in Jerome H. Friedman

Jerome Harold Friedman, geboren am 29. Dezember 1939 in der kleinen Stadt Yreka, Kalifornien (in der Nähe der Grenze zu Oregon), ist ein bahnbrechender amerikanischer Statistiker und eine der einflussreichsten Persönlichkeiten in der Entwicklung des modernen Machine Learning und Data Mining. Mit einem Hintergrund in der Physik überführte er computergestützte Methoden aus der Hochenergie-Teilchenphysik in die Statistik und schuf so praktische Algorithmen, die große, komplexe Datensätze verarbeiten können. Seine Arbeit legt den Schwerpunkt auf interpretierbare, robuste Modelle für Vorhersagen und die Entdeckung von Mustern, die Felder von Suchmaschinen bis hin zur Bioinformatik beeinflussen. Friedman hat über 70 Publikationen verfasst, wegweisende Bücher wie *Classification and Regression Trees* (CART, 1984) und *The Elements of Statistical Learning* (2001) mitverfasst und prestigeträchtige Ehrungen erhalten, darunter die Wahl in die National Academy of Sciences (2010), die American Academy of Arts and Sciences (2005) und mehrere Auszeichnungen für Innovationen im Bereich Data Mining und statistische Methoden.

### Das Originalpapier zu Gradient Boosting (Friedman, 2001)

Friedmans bahnbrechendes Papier *"Greedy Function Approximation: A Gradient Boosting Machine"*, veröffentlicht im August 2001 in den *Annals of Statistics*, formalisierte Gradient Boosting als eine vielseitige Ensemble-Methode für Regression und Klassifikation. Aufbauend auf früheren Boosting-Ideen von Informatikern wie Yoav Freund und Robert Schapire (die sich auf Klassifikationsfehler konzentrierten), erweiterte Friedman diese auf beliebige Verlustfunktionen unter Verwendung eines "funktionalen Gradientenabstiegs"-Rahmens. Die Kernidee: Iteratives Hinzufügen von schwachen Lernern (oft einfache Entscheidungsbäume), die den negativen Gradienten des Verlusts an den aktuellen Residuen anpassen, wodurch Fehler schrittweise minimiert werden, ähnlich wie stochastischer Gradientenabstieg im Funktionsraum.

Wichtige Innovationen umfassten:
- **Schrumpfung (Lernrate)**: Ein Regularisierungsparameter, um Overfitting zu verhindern, indem jeder neue Baum skaliert wird, was die Varianz reduziert, ohne die Verzerrung zu erhöhen.
- **Flexibilität**: Anwendbar auf jede differenzierbare Verlustfunktion (z.B. quadratischer Fehler für Regression, Log-Loss für Klassifikation), was es zu einem Allzweckwerkzeug macht.
- **Statistische Interpretation**: In Zusammenarbeit mit Trevor Hastie und Robert Tibshirani zeigte er, dass Boosting die Korrelation zwischen schwachen Lernern reduziert und so die Ensemble-Leistung verbessert.

Dieses Papier (vorgetragen als seine Rietz Lecture im Jahr 1999) löste eine breite Akzeptanz aus – Implementierungen wie XGBoost und LightGBM dominieren heute Kaggle-Wettbewerbe und die Industrie. Es hat über 20.000 Zitationen und verwandelte Ensemble-Learning von einer Heuristik in eine statistisch fundierte Kraft.

### Seine Geschichte: Vom Bastler aus der Kleinstadt zum Pionier des Machine Learning

Friedmans Werdegang liest sich wie eine klassische Geschichte von neugiergetriebener Neuerfindung. Aufgewachsen in einer Familie ukrainischer Einwanderer – seine Großeltern gründeten in den 1930er Jahren eine Wäscherei, die von seinem Vater und Onkel geführt wurde – war er in der High School ein selbsternannter "dramatischer Underachiever". Uninteressiert an Büchern, aber besessen von Elektronik, baute er Amateurfunkgeräte, Kristallradios und Hochspannungssender und unterhielt sich mit Kurzwellenoperatoren auf der ganzen Welt. Der Vater eines funkbegeisterten Freundes mentorierte ihn, aber sein Schulleiter warnte ihn, er würde im College durchfallen. Unbeirrt immatrikulierte er sich für zwei Jahre Party und Grundlagenwissenschaften am Humboldt State (heute Cal Poly Humboldt) und wechselte 1959 nach Verhandlungen mit seinem Vater an die UC Berkeley. Dort fesselte ihn ein hervorragender Physikprofessor; er schloss 1962 mit einem A.B. in Physik ab (Durchschnitt B+/A-, keine kleine Leistung vor der Noteninflation) und jobbte nebenher als Feuerwehrmann und im Radio.

Seine Promotion in Hochenergie-Teilchenphysik folgte 1967, mit Schwerpunkt auf Mesonen-Reaktionen in Blasenkammern unter Luis Alvarez' legendärer Gruppe am Lawrence Berkeley Lab. Während des Vietnamkriegs entzog er sich der Einberufung durch Studentenaufschub und stürzte sich in die Computerarbeit – er programmierte Streudiagramme auf alten IBM-Maschinen in Maschinensprache und Fortran. Dies löste eine Wende aus: Manuelle Mustererkennung auf Filmen führte zu Software wie Kiowa (explorative Datenanalyse) und Sage (Monte-Carlo-Simulationen), die Physik mit Statistik verband. Nach der Promotion blieb er als Postdoc (1968–1972), aber eine Laborumstrukturierung erzwang einen Wechsel.

1972 landete er als Leiter der Computation Research Group am Stanford Linear Accelerator Center (SLAC) und pendelte von Berkeley aus mit seiner Frau und seiner kleinen Tochter. An der Spitze von ~10 Programmierern befasste er sich mit Grafik, Algorithmen und Werkzeugen für Physiker auf modernster Hardware. Sabbaticals – wie am CERN (1976–1977), wo er adaptiven Monte-Carlo-Code schrieb – erweiterten seinen Horizont, aber die Intensität am SLAC entsprach seinem Stil. Auf Interface-Konferenzen lernte er Statistik-Größen kennen: John Tukey (Projection Pursuit, 1974), Leo Breiman (CART-Kollaboration, ab 1977) und Werner Stuetzle (Regressionsextensionen).

Bis 1982 war er halbtags im Statistikk Department der Stanford University tätig (ab 1984 voller Professor; Vorsitzender 1988–1991; Emeritus 2007) und balancierte die SLAC-Leitung bis 2003. Seine "Random Walk"-Forschung – das Lösen kniffliger Probleme durch Code und Empirie – brachte Durchbrüche hervor:
- **1970er**: k-d-Bäume für schnelle nächste Nachbarn (1977) und Projection Pursuit, um "Klumpen" in hohen Dimensionen zu erkennen.
- **1980er**: CART (Bäume für Klassifikation/Regression) und ACE (nichtparametrische Transformationen, 1985).
- **1990er**: MARS (spline-basierte adaptive Regression, 1991); Kritik an PLS; Bump Hunting (PRIM, 1999).
- **2000er**: Gradient Boosting (2001); RuleFit (interpretierbare Regeln aus Ensembles); glmnet (schnelles LASSO/elastic net).

Als produktiver Berater (z.B. Google 2011–2014, Yahoo 2004–2005) kommerzialisierte er Tools wie CART-Software und beeinflusste damit Suchmaschinen und mehr. Beeinflusst von Tukeys operationalem Fokus ("erzähl mir die Schritte") und Breimans Pragmatismus, mied Friedman schwere Theorie zugunsten eleganter, testbarer Algorithmen. Er lernte Statistik im laufenden Betrieb – ohne formale Kurse – und betrachtete sich selbst als "Opportunisten", der sich mit dem Chaos des Data Mining auseinandersetzte. Kollaborationen mit "brillanten" Studenten und Kollegen befeuerten ihn; er zog sich 2006 von der SLAC-Leitung zurück, beriet aber weiterhin und schrieb.

### Wo ist er jetzt?

Stand 2025, im Alter von 85 Jahren, ist Friedman weiterhin als Professor Emeritus mit der Stanford University verbunden und beeinflusst das Feld durch sein Vermächtnis und gelegentliche Arbeit. Sein Stanford-Profil listet ihn als aktiven Forscher im Bereich Machine Learning, und aktuelle Updates (z.B. American Academy of Arts and Sciences, September 2025) heben seine anhaltende Anerkennung hervor. Es gibt keine Anzeichen für einen vollständigen Ruhestand – angesichts seiner Geschichte ist er wahrscheinlich sporadisch beratend oder mentorisch tätig. Er lebt in der Bay Area, ganz seinen kalifornischen Wurzeln treu.

**Referenzen**
- [Jerome H. Friedman - Wikipedia](https://en.wikipedia.org/wiki/Jerome_H._Friedman)
- [Jerome H. Friedman | Department of Statistics, Stanford](https://statistics.stanford.edu/people/jerome-h-friedman)
- [A Conversation with Jerry Friedman (arXiv PDF)](https://arxiv.org/pdf/1507.08502)
- [Vita - Jerome H. Friedman (PDF)](https://jerryfriedman.su.domains/ftp/vita.pdf)
- [Jerome H. Friedman | American Academy of Arts and Sciences](https://www.amacad.org/person/jerome-h-friedman)