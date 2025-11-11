---
audio: false
generated: true
lang: fr
layout: post
title: Configuration des filtres dans les servlets Java
translated: true
type: note
---

### Comment fonctionne `javax.servlet.FilterConfig` ?

Dans les applications web Java construites à l'aide de l'API Servlet, l'interface `javax.servlet.FilterConfig` joue un rôle clé dans la configuration des filtres. Les filtres sont des composants qui interceptent et traitent les requêtes et réponses HTTP avant qu'elles n'atteignent une servlet ou après qu'elles l'aient quittée. `FilterConfig` fournit un moyen standardisé de transmettre des informations de configuration à un filtre lors de son initialisation par le conteneur web (par exemple, Tomcat, Jetty). Ci-dessous, j'expliquerai comment `FilterConfig` fonctionne, son objectif et comment il est utilisé.

---

#### **Qu'est-ce que `FilterConfig` ?**
`FilterConfig` est une interface du package `javax.servlet`. Elle est utilisée par le conteneur web pour fournir à un filtre des données de configuration pendant sa phase d'initialisation. Lorsqu'un filtre est défini dans une application web (via `web.xml` ou des annotations), le conteneur crée une instance du filtre et passe un objet `FilterConfig` à sa méthode `init`. Cet objet permet au filtre d'accéder à :
- Ses propres paramètres d'initialisation.
- Le `ServletContext` de l'application web.
- Son propre nom tel que défini dans la configuration.

 Les filtres implémentent l'interface `javax.servlet.Filter`, qui comprend trois méthodes : `init`, `doFilter` et `destroy`. L'objet `FilterConfig` est spécifiquement utilisé dans la méthode `init` pour configurer le filtre avant qu'il ne commence à traiter les requêtes.

---

#### **Cycle de vie d'un filtre et `FilterConfig`**
Pour comprendre comment `FilterConfig` fonctionne, examinons son rôle dans le cycle de vie du filtre :
1. **Démarrage du conteneur** : Lorsque l'application web démarre, le conteneur lit les définitions des filtres (depuis `web.xml` ou les annotations `@WebFilter`) et crée une instance de chaque filtre.
2. **Initialisation du filtre** : Pour chaque filtre, le conteneur appelle la méthode `init`, en passant un objet `FilterConfig` comme paramètre. C'est une opération unique par instance de filtre.
3. **Traitement de la requête** : Après l'initialisation, la méthode `doFilter` du filtre est appelée pour chaque requête correspondante. Bien que `FilterConfig` ne soit pas passé à `doFilter`, le filtre peut stocker les données de configuration de `FilterConfig` dans des variables d'instance pendant `init` pour une utilisation ultérieure.
4. **Arrêt du filtre** : Lorsque l'application s'arrête, la méthode `destroy` est appelée, mais `FilterConfig` n'intervient pas ici.

L'objet `FilterConfig` est essentiel pendant la phase d'initialisation, permettant au filtre de se préparer au traitement des requêtes.

---

#### **Méthodes clés de `FilterConfig`**
L'interface `FilterConfig` définit quatre méthodes qui donnent accès aux informations de configuration :

1. **`String getFilterName()`**
   - Retourne le nom du filtre tel que spécifié dans le fichier `web.xml` (sous `<filter-name>`) ou dans l'annotation `@WebFilter`.
   - C'est utile pour la journalisation, le débogage ou l'identification du filtre dans une chaîne de filtres.

2. **`ServletContext getServletContext()`**
   - Retourne l'objet `ServletContext`, qui représente l'ensemble de l'application web.
   - Le `ServletContext` permet au filtre d'accéder aux ressources de l'application entière, telles que les attributs de contexte, les fonctions de journalisation ou un `RequestDispatcher` pour transférer des requêtes.

3. **`String getInitParameter(String name)`**
   - Récupère la valeur d'un paramètre d'initialisation spécifique par son nom.
   - Les paramètres d'initialisation sont des paires clé-valeur définies pour le filtre dans `web.xml` (sous `<init-param>`) ou dans l'attribut `initParams` de l'annotation `@WebFilter`.
   - Retourne `null` si le paramètre n'existe pas.

4. **`Enumeration<String> getInitParameterNames()`**
   - Retourne une `Enumeration` de tous les noms de paramètres d'initialisation définis pour le filtre.
   - Cela permet au filtre de parcourir tous ses paramètres et de récupérer leurs valeurs en utilisant `getInitParameter`.

Ces méthodes sont implémentées par une classe concrète fournie par le conteneur web (par exemple, `FilterConfigImpl` interne à Tomcat). En tant que développeur, vous interagissez avec `FilterConfig` uniquement via cette interface.

---

#### **Comment `FilterConfig` est configuré**
Les filtres et leur configuration peuvent être définis de deux manières :
1. **En utilisant `web.xml` (Descripteur de déploiement)** :
   ```xml
   <filter>
       <filter-name>MyFilter</filter-name>
       <filter-class>com.example.MyFilter</filter-class>
       <init-param>
           <param-name>excludeURLs</param-name>
           <param-value>/login,/signup</param-value>
       </init-param>
   </filter>
   <filter-mapping>
       <filter-name>MyFilter</filter-name>
       <url-pattern>/*</url-pattern>
   </filter-mapping>
   ```
   - `<filter-name>` définit le nom du filtre.
   - `<init-param>` spécifie les paramètres d'initialisation sous forme de paires clé-valeur.

2. **En utilisant des annotations (Servlet 3.0 et ultérieur)** :
   ```java
   import javax.servlet.annotation.WebFilter;
   import javax.servlet.annotation.WebInitParam;

   @WebFilter(
       filterName = "MyFilter",
       urlPatterns = "/*",
       initParams = @WebInitParam(name = "excludeURLs", value = "/login,/signup")
   )
   public class MyFilter implements Filter {
       // Implémentation
   }
   ```
   - L'annotation `@WebFilter` définit le nom du filtre, les modèles d'URL et les paramètres d'initialisation.

Dans les deux cas, le conteneur utilise cette configuration pour créer un objet `FilterConfig` et le passer à la méthode `init` du filtre.

---

#### **Exemple pratique**
Voici comment un filtre pourrait utiliser `FilterConfig` en pratique :

```java
import javax.servlet.*;
import java.io.IOException;

public class MyFilter implements Filter {
    private String excludeURLs; // Variable d'instance pour stocker les données de configuration

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // Obtenir le nom du filtre
        String filterName = filterConfig.getFilterName();
        System.out.println("Initializing filter: " + filterName);

        // Obtenir un paramètre d'initialisation
        excludeURLs = filterConfig.getInitParameter("excludeURLs");
        if (excludeURLs != null) {
            System.out.println("Exclude URLs: " + excludeURLs);
        }

        // Stocker optionnellement ServletContext pour une utilisation ultérieure
        ServletContext context = filterConfig.getServletContext();
        context.log("Filter " + filterName + " initialized");
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        // Utiliser excludeURLs pour décider de filtrer ou non la requête
        chain.doFilter(request, response); // Poursuivre vers le filtre suivant ou la servlet
    }

    @Override
    public void destroy() {
        // Code de nettoyage
    }
}
```

- **Dans `init`** : Le filtre récupère son nom, un paramètre d'initialisation (`excludeURLs`) et le `ServletContext`. Il stocke `excludeURLs` dans une variable d'instance pour l'utiliser dans `doFilter`.
- **Dans `doFilter`** : Le filtre peut utiliser la configuration stockée (par exemple, `excludeURLs`) pour traiter les requêtes.

---

#### **Points clés concernant `FilterConfig`**
- **Portée spécifique au filtre** : Les paramètres d'initialisation dans `FilterConfig` sont spécifiques à l'instance du filtre. Différents filtres peuvent avoir des paramètres avec le même nom mais des valeurs différentes.
- **Contraste avec `ServletContext`** : Le `ServletContext` (accessible via `getServletContext()`) fournit des paramètres d'initialisation et des ressources à l'échelle de l'application, distincts des paramètres spécifiques au filtre dans `FilterConfig`.
- **Utilisation unique dans le cycle de vie** : `FilterConfig` n'est passé qu'à `init`. Si le filtre a besoin de ses données plus tard (par exemple, dans `doFilter`), il doit stocker les données dans des variables d'instance.
- **Fourni par le conteneur** : `FilterConfig` est une interface, et le conteneur web fournit l'implémentation concrète.

---

#### **Résumé**
`javax.servlet.FilterConfig` fonctionne en fournissant à un filtre des informations de configuration pendant son initialisation. Le conteneur web passe un objet `FilterConfig` à la méthode `init` du filtre, permettant au filtre de :
- Accéder à son nom (`getFilterName`).
- Récupérer ses paramètres d'initialisation (`getInitParameter`, `getInitParameterNames`).
- Interagir avec l'application web via le `ServletContext` (`getServletContext`).

Cela permet aux filtres d'être configurés de manière flexible—via `web.xml` ou des annotations—et les prépare à traiter efficacement les requêtes et réponses HTTP. Que vous excluiez certaines URL, définissiez des délais d'attente ou journalisiez des messages, `FilterConfig` est le pont entre la configuration du filtre et son comportement à l'exécution.