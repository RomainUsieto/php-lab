# Révision 2 — questions autonomes et examen ciblé

122 questions révisées dans les quatre chapitres ; 260 questions au total (200 QCM et 60 exercices). Les 260 identifiants, réponses attendues, chapitres, thèmes, types et références de diapositives restent identiques. Aucun historique n’est effacé.

Les énoncés n’exigent plus la consultation d’un exemple du support. Les questions d’analyse montrent le code nécessaire ; les exercices précisent les propriétés, signatures et variables disponibles. Les questions sur les DAO décrivent la dépendance entre objets au lieu de supposer connus les numéros des stratégies. Les autres modes gardent accès aux quatre chapitres.

## Examen blanc

Uniquement chapitres 2 et 3, avec 10 QCM et 2 exercices chacun : 20 QCM + 4 exercices, total 24. La configuration ne peut pas réintroduire un autre chapitre. Le mélange, le chronomètre et le barème sont conservés. Un tirage exactement identique au précédent est toujours remplacé.

## Compatibilité de la progression

La clé de stockage reste php-lab-v1. Le validateur reconnaît l’ancienne composition de 5 QCM + 1 exercice sur chacun des quatre chapitres et la nouvelle composition de 10 + 2 sur chacun des chapitres 2 et 3. Les anciens examens actifs portent une mention explicite ; ils ne changent pas le périmètre des nouvelles copies.

## Vérifications automatisées

21 tests réussis : 500 examens 2–3, équilibre et absence de doublons, configuration contradictoire ignorée, banques insuffisantes refusées, import de l’ancienne formule sans perte des réponses/progrès/favoris, rejet des compositions incohérentes, contrôle des renvois à un document absent, vérification PHP de tous les extraits QCM et des 60 solutions de code, exécution des exemples autonomes Personne/Voiture.

## Contrôle de l’aperçu

Le serveur HTTP local répond 200 avec le fichier autonome, et le JavaScript assemblé passe node --check. Le navigateur intégré a rencontré un délai d’attente sur localhost ; le contrôle visuel de cette révision n’a pas pu être effectué. Les 21 vérifications automatisées passent. Aucun changement n’a été effectué sur le site GitHub distant : le fichier de remplacement est fourni pour une mise à jour manuelle.

## Questions révisées

| Identifiant | Chapitre | Notion conservée |
| --- | --- | --- |
| c1-q007 | 1 | Conditions |
| c1-q020 | 1 | Tableaux |
| c1-q023 | 1 | Tableaux |
| c1-q025 | 1 | Accumulation |
| c1-q028 | 1 | Fonctions |
| c1-q031 | 1 | Fonctions |
| c1-q035 | 1 | GET |
| c1-q043 | 1 | Validation |
| c1-q044 | 1 | Validation |
| c1-q047 | 1 | Sessions |
| c1-e009 | 1 | Boucles |
| c1-e010 | 1 | Accumulation |
| c2-q006 | 2 | Encapsulation |
| c2-q007 | 2 | Encapsulation |
| c2-q009 | 2 | Instance |
| c2-q012 | 2 | Constructeur |
| c2-q015 | 2 | Arguments |
| c2-q016 | 2 | Arguments |
| c2-q017 | 2 | Arguments |
| c2-q018 | 2 | Contrôle |
| c2-q019 | 2 | Contrôle |
| c2-q021 | 2 | Méthodes |
| c2-q022 | 2 | Constructeur |
| c2-q024 | 2 | Héritage |
| c2-q025 | 2 | Héritage |
| c2-q026 | 2 | Héritage |
| c2-q027 | 2 | Héritage |
| c2-q029 | 2 | Destructeur |
| c2-q032 | 2 | Statique |
| c2-q033 | 2 | Statique |
| c2-q034 | 2 | Statique |
| c2-q035 | 2 | Compteur |
| c2-q036 | 2 | Compteur |
| c2-q037 | 2 | Instance |
| c2-q040 | 2 | Méthodes |
| c2-q043 | 2 | Héritage |
| c2-q044 | 2 | Compteur |
| c2-q045 | 2 | Encapsulation |
| c2-q046 | 2 | Arguments |
| c2-q049 | 2 | Héritage |
| c2-e004 | 2 | Instance |
| c2-e008 | 2 | Méthodes |
| c2-e010 | 2 | Héritage |
| c2-e011 | 2 | Héritage |
| c3-q002 | 3 | Persistance |
| c3-q003 | 3 | Stockage |
| c3-q009 | 3 | Architecture |
| c3-q011 | 3 | DAO |
| c3-q014 | 3 | Métier |
| c3-q015 | 3 | DAO |
| c3-q016 | 3 | XML |
| c3-q017 | 3 | Conception |
| c3-q018 | 3 | PDO |
| c3-q020 | 3 | Connexion |
| c3-q022 | 3 | Singleton |
| c3-q023 | 3 | Singleton |
| c3-q024 | 3 | Singleton |
| c3-q025 | 3 | PDO |
| c3-q026 | 3 | Singleton |
| c3-q027 | 3 | Connexion |
| c3-q028 | 3 | DAO instance |
| c3-q029 | 3 | DAO instance |
| c3-q030 | 3 | DAO statique |
| c3-q034 | 3 | Create |
| c3-q036 | 3 | Read |
| c3-q037 | 3 | Finders |
| c3-q038 | 3 | Finders |
| c3-q042 | 3 | Delete |
| c3-q043 | 3 | Stratégie 1 |
| c3-q044 | 3 | Stratégie 1 |
| c3-q045 | 3 | Stratégie 2 |
| c3-q046 | 3 | Stratégie 2 |
| c3-q047 | 3 | Centralisation |
| c3-q048 | 3 | Syntaxe |
| c3-q050 | 3 | Connexion |
| c3-e001 | 3 | DAO instance |
| c3-e002 | 3 | Connexion |
| c3-e005 | 3 | Singleton |
| c3-e006 | 3 | Singleton |
| c3-e008 | 3 | Stratégie 2 |
| c3-e009 | 3 | Stratégie 1 |
| c3-e010 | 3 | Finders |
| c3-e011 | 3 | Create |
| c3-e013 | 3 | Update |
| c3-e015 | 3 | Correction |
| c4-q003 | 4 | Conception |
| c4-q004 | 4 | Modèle |
| c4-q012 | 4 | Contrôleur |
| c4-q013 | 4 | Cycle MVC |
| c4-q014 | 4 | Sous-vues |
| c4-q018 | 4 | Organisation |
| c4-q021 | 4 | Point d’entrée |
| c4-q022 | 4 | Routage |
| c4-q024 | 4 | Sous-contrôleurs |
| c4-q025 | 4 | Paramètres |
| c4-q027 | 4 | Actions |
| c4-q028 | 4 | Actions |
| c4-q030 | 4 | Cycle MVC |
| c4-q032 | 4 | Démarche |
| c4-q033 | 4 | Démarche |
| c4-q034 | 4 | Démarche |
| c4-q038 | 4 | Fichiers |
| c4-q039 | 4 | Fichiers |
| c4-q040 | 4 | Navigation |
| c4-q042 | 4 | Films |
| c4-q043 | 4 | Modèle films |
| c4-q044 | 4 | Modèle films |
| c4-q045 | 4 | Vues films |
| c4-q046 | 4 | Vues films |
| c4-q047 | 4 | Formulaire films |
| c4-q048 | 4 | Formulaire films |
| c4-q049 | 4 | Actions films |
| c4-q050 | 4 | Tests |
| c4-e002 | 4 | Chemin |
| c4-e004 | 4 | Contrôleur |
| c4-e006 | 4 | Vue |
| c4-e009 | 4 | Actions |
| c4-e010 | 4 | Modification |
| c4-e011 | 4 | Films |
| c4-e012 | 4 | Films |
| c4-e013 | 4 | Films |
| c4-e014 | 4 | Ajout films |
