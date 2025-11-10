---
audio: false
generated: true
lang: fr
layout: post
title: La vision par ordinateur est inférieure à celle de l'homme
translated: true
type: note
---

L’article de blog de Yin Wang soutient que les systèmes de vision par ordinateur, même les plus avancés en 2019, étaient loin d’atteindre des performances équivalentes à celles d’un humain. Il affirme que ces systèmes peinent avec des tâches basiques de reconnaissance d’objets (par exemple, identifier une voiture) et sont facilement trompés par des exemples antagonistes ou de légères altérations d’image, contrairement aux humains qui reconnaissent les objets sans effort. Wang suggère que le domaine surestime ses progrès et qu’une véritable vision par ordinateur de niveau humain reste inaccessible en raison de limitations fondamentales dans la façon dont ces systèmes traitent et comprennent les images.

### Est-ce vrai ?
Au moment de la publication de l’article en octobre 2019, l’argument de Wang était valable compte tenu de l’état de la vision par ordinateur à l’époque :

- **Généralisation limitée** : Les modèles de vision par ordinateur, comme les réseaux neuronaux convolutifs (CNN), reposaient fortement sur la reconnaissance de motifs dans les données d’entraînement. Ils échouaient souvent à généraliser à de nouveaux contextes ou à bien gérer les cas limites, comme Wang le décrit. Par exemple, les modèles pouvaient mal classer des objets lorsque l’éclairage, les angles ou les arrière-plans changeaient significativement.

- **Vulnérabilité aux attaques antagonistes** : Le point de Wang sur les exemples antagonistes—des images subtilement modifiées pour induire les modèles en erreur—était exact. Des recherches, telles que Goodfellow et al. (2014), ont montré que de petites perturbations imperceptibles pouvaient amener les modèles à mal classer des images avec une grande confiance, mettant en lumière un écart entre la vision humaine et la vision machine.

- **Revendications exagérées** : L’article critique le battage médiatique autour de la vision par ordinateur. En 2019, bien que des modèles comme ResNet, YOLO et les premiers transformers affichaient des résultats impressionnants sur des benchmarks (par exemple, ImageNet), il s’agissait de jeux de données contrôlés. Les applications dans le monde réel révélaient souvent des faiblesses, comme des erreurs d’identification dans la conduite autonome ou les systèmes de reconnaissance faciale.

Cependant, le ton de l’article est absolu, affirmant qu’« il n’existe pas de vision par ordinateur de niveau humain ». Cela néglige les progrès réalisés dans des tâches spécifiques. Par exemple :
- **Succès dans des tâches spécifiques** : Dès 2019, les systèmes de vision par ordinateur surpassaient les humains dans des tâches restreintes comme la classification de certaines images médicales (par exemple, la détection de la rétinopathie diabétique) ou la reconnaissance d’objets spécifiques dans des environnements contrôlés.
- **Progrès depuis 2019** : En 2025, des avancées comme les vision transformers (par exemple, ViT, CLIP) et les modèles multimodaux à grande échelle (par exemple, GPT-4o, DALL·E 3) ont réduit l’écart. Ces modèles gèrent des entrées plus diverses, généralisent mieux dans différents contextes et intègrent le langage et la vision pour un raisonnement amélioré. Pourtant, ils ne reproduisent pas entièrement la robustesse, la conscience contextuelle ou la compréhension intuitive de la vision humaine.

### Évaluation critique
L’affirmation principale de Wang—que la vision par ordinateur en 2019 n’était pas de niveau humain—est globalement vraie. Les modèles manquaient de la généralisation, de la robustesse et de la compréhension intuitive de la vision humaine. Cependant, son rejet des progrès pourrait être excessivement pessimiste, car des avancées significatives ont été réalisées depuis. Même en 2025, bien que la vision par ordinateur excelle dans des domaines spécifiques, elle reste inférieure à la perception humaine dans des scénarios en monde ouvert en raison de problèmes tels que :
- **Raisonnement contextuel** : Les humains intègrent sans effort les données sensorielles avec la connaissance du monde ; les machines peinent à le faire.
- **Cas limites** : Les modèles peuvent échouer dans des situations rares ou nouvelles où les humains s’adaptent rapidement.
- **Efficacité énergétique** : La vision humaine est bien plus économe en énergie que les modèles computationnels.

L’article reste pertinent en tant que critique de la surestimation des capacités de l’IA, mais ne tient pas compte des progrès rapides dans le domaine. Aucune source unique ne confirme qu’une vision « de niveau humain » a été atteinte en 2025, mais l’écart s’est considérablement réduit.[](https://yinwang0.wordpress.com/2019/10/20/human-level-computer-vision/)