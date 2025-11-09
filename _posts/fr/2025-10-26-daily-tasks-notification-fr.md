---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Configuration des notifications quotidiennes pour les tâches Google
translated: true
type: note
---

### Configurer une notification quotidienne récurrente dans Google Tasks

Google Tasks prend en charge les tâches récurrentes avec des notifications liées à une date et une heure d'échéance. La bonne nouvelle est que la prochaine occurrence d'une tâche récurrente apparaîtra automatiquement à sa date prévue **peu importe que vous marquiez la tâche actuelle comme terminée ou non**. Cela signifie que vous n'avez *pas besoin* de la marquer comme faite pour que les rappels continuent de se répéter chaque jour — le cycle se poursuit de lui-même.

Cependant, si vous ne marquez pas la tâche comme terminée, l'instance du jour en cours restera dans votre liste de tâches comme "en retard" une fois l'heure d'échéance passée. Cela peut encombrer légèrement votre vue, mais la notification elle-même ne se déclenchera qu'une fois par jour à l'heure définie, et vous pouvez la rejeter (pour la faire disparaître) sans autre action. Si vous souhaitez que l'entrée de la tâche disparaisse également de la liste (pour une expérience plus épurée), vous devrez la marquer comme terminée — mais c'est optionnel car les rappels ne s'arrêteront pas.

Voici comment la configurer pour votre exemple "acheter de la nourriture sur JD.com" :

1.  Ouvrez l'application **Google Tasks** sur votre téléphone (ou accédez-y via Gmail/Calendar sur le web).
2.  Appuyez sur le **+** pour créer une nouvelle tâche.
3.  Saisissez le titre : **Acheter de la nourriture sur JD.com**.
4.  Appuyez sur **Ajouter date/heure** et définissez la première date/heure d'échéance (par exemple, demain à 8h00, quand vous voulez la notification quotidienne).
5.  À côté de "Date/heure", appuyez sur **Répéter**.
6.  Choisissez **Quotidien** (ou personnalisé si nécessaire).
7.  Sous "Se termine", sélectionnez **Jamais** (ou définissez une date de fin si vous le souhaitez temporaire).
8.  Appuyez sur **OK** > **Enregistrer**.

-   **Notifications** : Allez dans les paramètres système de votre téléphone > Applications > Google Tasks > Notifications, et assurez-vous qu'elles sont activées. L'application enverra une notification à l'heure d'échéance exacte chaque jour.
-   **Ce qui se passe quotidiennement** : Vous recevrez une alerte. Rejetez-la, et la notification disparaît. L'entrée de la tâche reste jusqu'à ce qu'elle soit complétée (si vous choisissez de le faire), mais une nouvelle instance apparaît automatiquement le lendemain pour un nouveau rappel.
-   **Voir/Modifier** : Dans l'application Tasks, les tâches en retard s'affichent par défaut en haut. Vous pouvez passer à la vue "Planifiées" pour vous concentrer sur les prochaines.

Si les tâches en retard persistantes vous dérangent, les marquer comme terminées est rapide (appuyez sur le cercle à côté de la tâche) et génère instantanément la prochaine instance propre — aucune étape supplémentaire n'est nécessaire. Mais si vous voulez vraiment zéro interaction au-delà du rejet de la notification, cette configuration vous satisfait à 90%, car la répétition principale ne dépend pas de l'achèvement.

Si cela ne convient pas tout à fait (par exemple, vous ne voulez *aucune* entrée de tâche visible), envisagez Google Assistant comme alternative : Dites "Ok Google, rappelle-moi tous les jours à 8h d'acheter de la nourriture sur JD.com." Cela crée une alerte récurrente similaire via la section Rappels de l'application Google, qui se synchronise avec Tasks mais se comporte plus comme une alarme pure (rejeter et oublier, sans accumulation visible de tâches). Elle notifie quotidiennement sans exiger de marquage.

Pour plus de détails sur les tâches récurrentes : [Gérer les tâches répétitives dans Google Tasks](https://support.google.com/tasks/answer/12132599)