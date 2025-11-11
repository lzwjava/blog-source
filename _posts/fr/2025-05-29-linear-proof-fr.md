---
audio: false
generated: true
lang: fr
layout: post
title: Preuve d'indépendance linéaire
translated: true
type: note
---

23. Étant donné que les vecteurs \\( \alpha_1, \alpha_2, \alpha_3 \\) sont linéairement indépendants, et les vecteurs \\( \beta_1 = \alpha_1 + 2\alpha_2 \\), \\( \beta_2 = -\alpha_1 + \alpha_2 - 3\alpha_3 \\), \\( \beta_3 = 3\alpha_1 + 6\alpha_3 \\). Montrer que les vecteurs \\( \beta_1, \beta_2, \beta_3 \\) sont linéairement liés.

### Solution :
Pour montrer que les vecteurs \\( \beta_1, \beta_2, \beta_3 \\) sont linéairement liés, nous devons trouver des scalaires \\( c_1, c_2, c_3 \\) (non tous nuls) tels que :

\\[ c_1 \beta_1 + c_2 \beta_2 + c_3 \beta_3 = 0 \\]

Donné :
\\[ \beta_1 = \alpha_1 + 2\alpha_2 \\]
\\[ \beta_2 = -\alpha_1 + \alpha_2 - 3\alpha_3 \\]
\\[ \beta_3 = 3\alpha_1 + 6\alpha_3 \\]

Nous devons trouver des constantes \\( c_1, c_2, c_3 \\) telles que :

\\[ c_1 (\alpha_1 + 2\alpha_2) + c_2 (-\alpha_1 + \alpha_2 - 3\alpha_3) + c_3 (3\alpha_1 + 6\alpha_3) = 0 \\]

Ceci peut être réécrit comme :

\\[ (c_1 - c_2 + 3c_3)\alpha_1 + (2c_1 + c_2)\alpha_2 + (-3c_2 + 6c_3)\alpha_3 = 0 \\]

Puisque \\( \alpha_1, \alpha_2, \alpha_3 \\) sont linéairement indépendants, les coefficients de \\( \alpha_1, \alpha_2, \alpha_3 \\) doivent chacun être nuls :

1. \\( c_1 - c_2 + 3c_3 = 0 \\)
2. \\( 2c_1 + c_2 = 0 \\)
3. \\( -3c_2 + 6c_3 = 0 \\)

Résolvons ce système d'équations :

À partir de l'équation 2 :
\\[ 2c_1 + c_2 = 0 \implies c_2 = -2c_1 \\]

À partir de l'équation 3 :
\\[ -3c_2 + 6c_3 = 0 \implies -3(-2c_1) + 6c_3 = 0 \implies 6c_1 + 6c_3 = 0 \implies c_3 = -c_1 \\]

Substituons \\( c_2 = -2c_1 \\) et \\( c_3 = -c_1 \\) dans l'équation 1 :
\\[ c_1 - (-2c_1) + 3(-c_1) = 0 \implies c_1 + 2c_1 - 3c_1 = 0 \implies 0 = 0 \\]

Ceci est vrai pour tout \\( c_1 \\). Choisissons \\( c_1 = 1 \\) :

Alors :
\\[ c_2 = -2 \\]
\\[ c_3 = -1 \\]

Ainsi, nous avons trouvé des constantes \\( c_1 = 1, c_2 = -2, c_3 = -1 \\) telles que :

\\[ 1 \cdot \beta_1 - 2 \cdot \beta_2 - 1 \cdot \beta_3 = 0 \\]

Ceci prouve que les vecteurs \\( \beta_1, \beta_2, \beta_3 \\) sont linéairement liés.