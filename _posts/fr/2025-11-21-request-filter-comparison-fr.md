---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4.1-fast
title: 'Comparaison des filtres de requête : WebSphere contre Spring Boot'
translated: true
type: note
---

### Aperçu
IBM WebSphere Application Server (WAS, traditionnel ou Liberty) et Spring Boot prennent tous deux en charge le concept de **chaîne de traitement des requêtes** basée sur le `javax.servlet.Filter` et le `FilterChain` de l'API Servlet Java standard. C'est là que les requêtes HTTP entrantes passent par une série de filtres avant d'atteindre les servlets (ou contrôleurs/gestionnaires), et où les réponses peuvent être modifiées sur le chemin du retour.

- Les filtres permettent le pré-traitement (par exemple, authentification, journalisation, compression) et le post-traitement des requêtes/réponses.
- Le mécanisme central — implémenter `Filter`, appeler `chain.doFilter(request, response)` pour continuer — est **identique** car les deux s'exécutent dans un conteneur Servlet (WAS a son propre conteneur web Java EE complet ; Spring Boot intègre par défaut Tomcat/Jetty/Undertow).

Il n'y a pas de différence fondamentale dans le fonctionnement d'un "filtre de chaîne de requêtes" de base. Cependant, la manière dont vous configurez, ordonnez et intégrez les filtres diffère considérablement en raison de l'architecture de chaque plateforme.

### Comparaison Clé

| Aspect                   | IBM WebSphere Application Server (Traditionnel/Liberty) | Spring Boot |
|--------------------------|----------------------------------------------------------|-------------|
| **Mécanisme Sous-jacent** | Filtres Servlet standard (`javax.servlet.Filter`). WAS possède également des extensions propriétaires comme `ChainedRequest`/`ChainedResponse` pour le transfert/chaînage interne des requêtes dans certains scénarios (par exemple, portail ou API IBM personnalisées). | Filtres Servlet standard. Spring Boot enregistre automatiquement tout bean Filter `@Component` ou vous l'enregistrez explicitement via `FilterRegistrationBean`. |
| **Configuration**        | Principalement via `web.xml` (déclaratif) ou enregistrement programmatique. Pour les filtres globaux (sur toutes les applications) : complexe — nécessite des bibliothèques partagées, des écouteurs personnalisés ou des extensions spécifiques à IBM (pas de web.xml simple à l'échelle du serveur comme Tomcat). | Convention plutôt que configuration : Annotez avec `@Component` + `@Order` pour un enregistrement automatique, ou utilisez `FilterRegistrationBean` pour un contrôle fin (modèles d'URL, types de répartiteur). Très convivial pour le développeur. |
| **Ordonnancement**       | Défini par l'ordre dans `web.xml` ou via `@Order` si programmatique. L'ordonnancement global est délicat. | Facile avec `@Order(n)` (plus bas = plus tôt) ou l'interface `Ordered`. Spring Boot gère la chaîne automatiquement. |
| **Chaîne de Filtres de Sécurité** | Utilise des filtres Servlet standard ou la sécurité spécifique à IBM (par exemple, TAI, rôles JEE). Pas de chaîne de sécurité intégrée comme Spring Security. | Spring Security fournit une puissante `SecurityFilterChain` (via `FilterChainProxy`) avec plus de 15 filtres ordonnés (CSRF, authentification, gestion de session, etc.). Hautement personnalisable avec plusieurs chaînes par chemin. |
| **Facilité d'Ajout de Filtres Personnalisés** | Plus verbeux, surtout pour les filtres globaux/inter-applications. Nécessite souvent des ajustements via la console d'administration ou des bibliothèques partagées. | Extrêmement simple — juste un bean `@Component` ou une classe de configuration. Auto-intégré dans le conteneur embarqué. |
| **Modèle de Déploiement** | Serveur Java EE complet traditionnel. Applications déployées en WAR/EAR. Prend en charge des fonctionnalités d'entreprise avancées (clustering, transactions, JMS). | Conteneur embarqué (JAR exécutable autonome par défaut). Peut être déployé en WAR sur des serveurs externes (y compris WAS). Orienté léger/microservices. |
| **Performance/Overhead** | Surcharge plus élevée (serveur d'applications complet). Les chaînes de transport, les canaux du conteneur web ajoutent des couches. | Surcharge plus faible (conteneur léger embarqué). Démarrage plus rapide, utilisation des ressources réduite. |
| **Quand les Filtres S'exécutent** | Dans la chaîne entrante du conteneur web WAS. Peut avoir des filtres de transport au niveau du serveur (par exemple, filtrage IP sur les canaux TCP). | Dans la chaîne de filtres du conteneur embarqué. Spring Boot ajoute ses propres filtres (gestion des erreurs, encodage des caractères, etc.). |
| **Cas d'Utilisation Courants** | Monolithes d'entreprise, portails, applications Java EE héritées nécessitant une sécurité/journalisation globale. | Microservices modernes, API REST, développement rapide avec Spring Security. |

### Exemples Pratiques

**Filtre Personnalisé Standard (le même code fonctionne dans les deux) :**
```java
@Component  // Spring Boot uniquement ; dans WAS, déclarez-le dans web.xml
@Order(1)
public class LoggingFilter implements Filter {
    public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)
            throws IOException, ServletException {
        System.out.println("Requête : " + ((HttpServletRequest) req).getRequestURI());
        chain.doFilter(req, res);  // Critique : passe au filtre/servlet suivant
    }
    // init/destroy...
}
```

**Dans Spring Boot (enregistré automatiquement) :**
Juste la classe ci-dessus + `@Component`.

**Dans WAS :**
Ajoutez dans `web.xml` :
```xml
<filter>
    <filter-name>LoggingFilter</filter-name>
    <filter-class>com.example.LoggingFilter</filter-class>
</filter>
<filter-mapping>
    <filter-name>LoggingFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

### Quand Choisir Quelle Solution
- **Utilisez les filtres WAS** si vous êtes dans un environnement IBM hérité, avez besoin des fonctionnalités complètes de Java EE, ou devez appliquer des filtres globalement sur de nombreuses applications sans modifier le code.
- **Utilisez les filtres Spring Boot** (surtout avec Spring Security) pour les nouveaux projets/projets greenfield, les microservices, les itérations rapides, ou lorsque vous voulez plusieurs chaînes de sécurité et un ordonnancement facile.

En résumé, le **concept de filtre de chaîne de requêtes est le même** (spécification Servlet), mais **Spring Boot le rend beaucoup plus simple et plus puissant** pour la plupart des cas d'utilisation modernes, tandis que WAS est plus lourd, orienté entreprise et nécessite plus de configuration.

[Documentation IBM WAS sur le Filtrage Servlet](https://www.ibm.com/docs/en/was/9.0.5?topic=extensions-servlet-filtering)  
[Filtres Personnalisés Spring Boot](https://www.baeldung.com/spring-boot-add-filter)  
[Chaîne de Filtres Spring Security](https://docs.spring.io/spring-security/reference/servlet/architecture.html)