# Journal de validation

## Correctif du suivi des erreurs — 25 novembre 2026

`npm test` : **26 tests réussis, zéro échec**. Les cinq nouveaux tests vérifient :

- Une reprise juste retire immédiatement chaque question des erreurs, y compris après remise et restauration. La maîtrise conserve son seuil de trois succès.
- Un QCM multiple incomplet ou un code auto-évalué à 50 % reste à retravailler.
- Le retrait manuel conserve les compteurs, favoris et historique ; il persiste dans LocalStorage et dans une sauvegarde JSON.
- Le même essai n’est pas compté deux fois ; une nouvelle réponse incorrecte réactive une erreur retirée.
- Les anciennes sauvegardes reconnaissent les erreurs déjà réussies sans effacer leurs résultats.

Les JavaScript modulaire et autonome passent la vérification de syntaxe. La version autonome a été régénérée à partir des modules corrigés.


La révision 2 comporte **21 tests réussis**, des questions autonomes et des examens limités aux chapitres 2 et 3. Voir [le rapport de révision 2](REVISION-2.md) pour la portée actuelle et la limite du contrôle visuel.

## Validation initiale — avant la révision 2

## Contrôles automatisés

`npm test` : **15 tests réussis, zéro échec**.

- Structure : 260 identifiants et énoncés distincts ; 50 QCM et 15 exercices par chapitre ; métadonnées et références de diapositives présentes.
- Banque : 166 choix uniques, 19 questions multiples, 15 vrai/faux et 60 exercices ; 137 faciles, 99 intermédiaires et 24 difficiles, répartis dans les quatre chapitres.
- 500 examens : exactement 20 QCM et 4 codes ; exactement cinq QCM et un code dans chaque chapitre ; aucune répétition dans une copie.
- Cas de tirage identique : remplacement garanti d’un QCM si la sélection reproduit exactement la précédente copie remise.
- Mélange : source non mutée, éléments préservés, les quatre positions possibles pour une option.
- Réponses multiples : ordre libre ; omission, surplus et doublon refusés.
- Score : barème personnalisé, note provisoire, code à 50 %, puis note finale complète.
- Filtres : chapitre, niveau, type code et sélection vide.
- Maîtrise : trois succès consécutifs après une erreur ; aucun double comptage dans une session.
- Sauvegarde et import : réponses, texte du code, marquage, ordre des propositions, index et date de départ conservés ; données incohérentes refusées.
- Horloge : temps calculé sur une date absolue et expiration bornée.
- Historique : mises à jour sans doublon ; copies à auto-évaluation incomplète exclues de la moyenne.
- Code libre : pas de comparaison de chaînes pour juger une solution équivalente.
- Vrai PHP local : `php -l` sur les 60 corrections et leurs variantes, dans un contexte de classe/méthode adapté ; exécution de six exemples de prédiction.

La vérification de syntaxe ne prétend pas prouver sémantiquement toutes les solutions. Les méthodes dépendantes d’une base ou du modèle utilisent le contrat donné dans l’énoncé. La notation du code dans le site reste une auto-évaluation explicite.

## Parcours observés dans le navigateur

- Accueil initial : zéro résultat, aucun chiffre de réussite inventé ; navigation et accès aux modes.
- Examen 45 minutes : 24 questions parcourues, équilibre 6 par chapitre, quatre éditeurs de code ; réponse simple, réponse multiple, marquage et navigation.
- Actualisation pendant l’examen : même question, mêmes positions d’options, sélection multiple et quatre réponses de code restaurées ; compteur poursuivi.
- Remise : confirmation mentionnant les questions non répondues ; 24 corrections ; note 1/20 pour deux QCM justes et code en attente, puis 11/20 après les quatre auto-évaluations correctes au barème 1/5.
- QCM personnalisé : filtre réponses multiples, correction immédiate et explication de chaque proposition.
- QCM différé : sélection par raccourci 1, aucune correction ni bouton de validation immédiate avant la remise.
- Entraînement code : saisie libre, indice, affichage de la référence, explications et auto-évaluation ; syntaxe compacte conservée telle que saisie.
- Erreurs : correction consultable, liste des questions marquées et démarrage d’une sélection ciblée.
- Express : session de 12 questions, erreurs existantes prioritaires.
- Chapitre MVC : résumé, statistiques et thèmes ; fiche complète comportant huit sections.
- Impression : page réunissant exactement cinq fiches et 39 sections, avec styles d’impression dédiés. La boîte d’impression système et une imprimante physique n’ont pas été testées.
- Export réel JSON vers le navigateur, réinitialisation, import de ce même fichier avec confirmation et récupération des résultats (26 questions évaluées, examen à 11/20).
- Examen d’une minute : remise automatique, temps final 01:00 et copie sans réponse notée 0/20 ; comportement conservé à l’actualisation.
- Mobile 390 × 844 : accueil, éditeur, navigation latérale et fiches ; largeur de document 390 px, sans débordement horizontal global.
- Clair et sombre : affichages contrôlés, préférences restaurées.
- Console : aucune erreur ni alerte JavaScript relevée sur les parcours testés.
- Données de test réinitialisées après vérification.

## Version HTML autonome

`PHP-Lab-autonome.html` est généré à partir des mêmes modules et JSON, avec style, code et banque intégrés. Le script assemblé passe `node --check`. Test navigateur sur HTTP local : accueil chargé, examen de 24 questions lancé, aucune erreur JavaScript, puis données de test effacées.

L’outil navigateur refuse la navigation `file://`. L’ouverture directe par double-clic n’a donc pas été vérifiée ; aucun navigateur alternatif ni contournement du protocole n’a été utilisé. La version autonome ne comporte plus de chargement JSON ni d’import de module externe.

## Limites de vérification

Tests réalisés dans le navigateur intégré sur ordinateur et avec un viewport mobile, sans appareil mobile physique. Les fichiers utilisent uniquement des chemins relatifs et des routes à fragments compatibles GitHub Pages. Aucun dépôt GitHub n’a été créé ni publié : le README fournit la procédure. Le projet utilise un serveur HTTP de fichiers pour l’aperçu local ; aucun serveur PHP ni service distant n’est utilisé par l’application.
