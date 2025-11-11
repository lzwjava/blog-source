---
audio: false
generated: true
lang: fr
layout: post
title: Inductances
translated: true
type: note
---

Au cœur d'innombrables circuits électroniques se trouve l'inductance (ou bobine), un composant passif en apparence simple mais doté d'une profonde capacité à influencer le flux du courant électrique. Contrairement aux résistances qui s'opposent directement au flux du courant ou aux condensateurs qui stockent l'énergie dans un champ électrique, les inductances stockent l'énergie dans un champ magnétique et, crucialement, s'opposent aux *changements* de courant. Cette caractéristique les rend indispensables dans des applications allant du filtrage et du stockage d'énergie à l'accord des circuits et la conversion de puissance.

Le fonctionnement d'une inductance est régi par les principes fondamentaux de l'électromagnétisme, principalement la Loi de l'induction de Faraday et la Loi de Lenz.

**Loi de l'induction de Faraday :** Cette loi stipule qu'un champ magnétique changeant à travers une bobine de fil induira une force électromotrice (fem), ou tension, aux bornes de la bobine. L'amplitude de cette fem induite est directement proportionnelle à la vitesse de variation du flux magnétique à travers la bobine. Mathématiquement, cela s'exprime par :

$E = -N \frac{d\Phi_B}{dt}$

Où :
* $E$ est la fem induite (tension)
* $N$ est le nombre de spires de la bobine
* $\frac{d\Phi_B}{dt}$ est la vitesse de variation du flux magnétique à travers chaque spire

**Loi de Lenz :** Cette loi complète la Loi de Faraday en définissant la direction du courant induit et, par conséquent, la polarité de la tension induite. Elle stipule que le courant induit circulera dans une direction qui crée un champ magnétique s'opposant à la *variation* du flux magnétique qui l'a produit. Cette opposition inhérente au changement est la caractéristique déterminante du comportement d'une inductance. Si le courant traversant une inductance augmente, la tension induite s'opposera à cette augmentation, essayant de maintenir le courant initial. Inversement, si le courant diminue, la tension induite tentera de s'opposer à cette diminution, essayant de maintenir le flux du courant.

**Construction physique et facteurs affectant l'inductance :**

Une inductance est typiquement construite comme une bobine de fil isolé enroulé autour d'un noyau. Les caractéristiques physiques de cette construction influencent directement son inductance (L), qui est une mesure de la capacité de l'inductance à stocker l'énergie dans un champ magnétique et à s'opposer aux changements de courant. L'inductance est principalement déterminée par :

* **Nombre de spires (N) :** L'inductance est proportionnelle au carré du nombre de spires de la bobine. Plus il y a de spires, plus le champ magnétique est fort pour un courant donné et donc plus l'inductance est élevée.
* **Section transversale de la bobine (A) :** Une plus grande section transversale permet à davantage de lignes de flux magnétique de traverser la bobine, augmentant l'inductance.
* **Longueur de la bobine (l) :** Pour un nombre de spires et une section donnés, une bobine plus courte résulte en un champ magnétique plus concentré et une inductance plus élevée.
* **Perméabilité du matériau du noyau (μ) :** Le matériau du noyau impacte significativement l'inductance. Les matériaux ferromagnétiques (comme le fer ou la ferrite) ont une haute perméabilité magnétique, ce qui signifie qu'ils peuvent supporter un champ magnétique bien plus fort que l'air pour la même intensité de champ magnétique. L'utilisation d'un noyau à haute perméabilité augmente considérablement l'inductance par rapport à une inductance à air. La relation est souvent exprimée comme :

$L \propto \frac{N^2 A \mu}{l}$

Les inductances peuvent avoir différents types de noyaux, notamment l'air, le fer, la ferrite et le fer pulvérisé, chacun offrant des caractéristiques différentes en termes de valeur d'inductance, de réponse en fréquence et de gestion de la puissance. La méthode d'enroulement (monocouche, multicouche) et l'espacement entre les spires jouent également un rôle dans la détermination de la valeur d'inductance finale et des effets parasites.

**Comportement dans les circuits continu et alternatif :**

Le comportement d'une inductance diffère significativement selon qu'elle se trouve dans un circuit continu (DC) ou alternatif (AC).

* **Circuits continu :** Dans un circuit continu avec une source de tension constante, lorsque le circuit est initialement fermé, le courant commence à circuler et à construire un champ magnétique dans l'inductance. L'inductance s'oppose à cette augmentation de courant en générant une force contre-électromotrice. Lorsque le courant approche un état stable (il ne change plus), la vitesse de variation du flux magnétique devient nulle, et la tension induite aux bornes de l'inductance idéale chute à zéro. Dans cette condition de régime permanent en continu, une inductance idéale se comporte comme un court-circuit, permettant au courant de circuler sans entrave (seulement limité par la résistance du circuit). Cependant, pendant la phase transitoire (lorsque le courant change), l'opposition de l'inductance au changement de courant est évidente, et le courant augmente exponentiellement vers sa valeur de régime permanent, dictée par la constante de temps du circuit ($\tau = L/R$). Lorsque la source continue est retirée, l'inductance s'oppose à la diminution du courant, et l'énergie stockée dans le champ magnétique est libérée, provoquant une décroissance exponentielle du courant.

* **Circuits alternatif :** Dans un circuit alternatif, le courant change constamment en magnitude et en direction. Ce changement continu du courant signifie que le champ magnétique dans l'inductance change également continuellement, induisant une tension à ses bornes selon la Loi de Faraday. Cette tension induite s'oppose toujours au changement de courant. Cette opposition au flux du courant alternatif est appelée **réactance inductive ($X_L$)**. La réactance inductive dépend de la fréquence et est donnée par :

$X_L = 2\pi f L$

Où :
* $X_L$ est la réactance inductive en ohms ($\Omega$)
* $f$ est la fréquence du courant alternatif en Hertz (Hz)
* $L$ est l'inductance en Henrys (H)

Lorsque la fréquence du signal alternatif augmente, la vitesse de variation du courant augmente, résultant en une tension induite plus grande et donc une réactance inductive plus élevée. Cela signifie que les inductances offrent plus d'opposition aux signaux alternatifs de haute fréquence et moins d'opposition aux signaux alternatifs de basse fréquence.

Dans une inductance idéale dans un circuit alternatif, le courant est en retard de phase de 90 degrés par rapport à la tension. Cela s'explique par le fait que la tension induite est proportionnelle à la *vitesse de variation* du courant. Le courant change le plus rapidement lorsqu'il traverse la ligne zéro, tandis que la tension induite est à son pic à ces points.

**Impédance (Z) :** Dans les circuits alternatifs contenant à la fois une résistance (R) et une réactance inductive ($X_L$), l'opposition totale au flux du courant est appelée impédance (Z). L'impédance est une quantité complexe qui prend en compte à la fois l'amplitude et la relation de phase de l'opposition. Pour un circuit RL série, l'impédance est donnée par :

$Z = R + jX_L$

Où $j$ est l'unité imaginaire. La magnitude de l'impédance est

\\[ 
    |Z| = \sqrt{R^2 + X_L^2}$
\\]

**Applications clés des inductances :**

Les propriétés uniques des inductances en font des composants essentiels dans une grande variété de circuits électroniques :

* **Filtres :** Les inductances sont utilisées en conjonction avec des condensateurs et des résistances pour créer des filtres qui laissent passer ou bloquent sélectivement certaines fréquences. Elles sont cruciales dans l'équipement audio, les alimentations (pour lisser l'ondulation résiduelle) et les systèmes de communication.
* **Stockage d'énergie :** Les inductances peuvent stocker de l'énergie électrique dans leurs champs magnétiques. Cette propriété est utilisée dans les alimentations à découpage (comme les convertisseurs boost et buck) pour augmenter ou réduire efficacement les tensions.
* **Circuits d'accord :** Dans les circuits résonants (circuits LC), les inductances et les condensateurs sont utilisés ensemble pour créer des circuits hautement sensibles à une fréquence spécifique. Ceci est fondamental pour le fonctionnement des radios, télévisions et autres dispositifs de communication pour sélectionner les canaux désirés.
* **Transformateurs :** Les transformateurs, essentiels pour la transmission de puissance et la conversion de tension, sont constitués de deux bobines ou plus (inductances) qui sont couplées magnétiquement. Un courant changeant dans une bobine induit une tension dans les autres bobines.
* **Bobines de blocage (Chokes) :** Les inductances sont utilisées comme bobines de blocage pour bloquer les signaux alternatifs tout en laissant passer les signaux continus. On les trouve couramment dans les alimentations et les circuits audio.
* **Capteurs :** Les capteurs inductifs fonctionnent en détectant les changements d'inductance causés par la proximité ou le mouvement d'objets métalliques.
* **Chargement sans fil :** Le couplage inductif entre des bobines est la base des systèmes de transfert d'énergie sans fil utilisés pour charger les smartphones, les véhicules électriques et autres appareils.

En résumé, les inductances sont des composants fondamentaux en électronique, tirant parti des principes de l'induction électromagnétique pour s'opposer aux changements de courant et stocker l'énergie dans un champ magnétique. Leur comportement dans les circuits continu et alternatif, caractérisé par leur inductance et leur réactance dépendante de la fréquence, les rend indispensables pour un large éventail d'applications qui façonnent la technologie moderne.