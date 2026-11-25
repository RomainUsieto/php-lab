# Analyse des supports et traçabilité

Analyse des quatre fichiers fournis, sans modification des originaux. Extraction des 164 diapositives (textes, tableaux et formes), inspection des captures et schémas incorporés après déduplication des logos, et conversion des quatre présentations en PDF de travail. Les captures ont été lues visuellement ; la tentative OCR locale n’a pas abouti et n’a pas servi de base aux corrections.

Les 260 questions ont été rédigées autour des notions effectivement présentes. Le chapitre 3 privilégie les contrats CRUD, l’organisation et les appels DAO ; il ne transforme pas le cours en un chapitre sur des API SQL absentes des supports. Les exercices définissent explicitement les méthodes et variables disponibles.

## Référence ergonomique

[CCNA Lab](https://aloyslrtg.github.io/ccna-lab/) a été observé dans le navigateur : barre latérale, sélection de modules, cartes, hiérarchie typographique, tableau de bord sobre, composition de session, ordre mélangé et révision des erreurs. PHP Lab reprend cette organisation avec un accent indigo, un examen 20+4 et un éditeur spécifique. Aucun asset ni question réseau n’est repris.

## Coquilles prises en compte

- Chapitre 1 : guillemets typographiques, exemple de validation mal ponctué (diapo 43), contradiction > 0 / >= 0 entre 41 et 43.
- Chapitre 2 : underscores manquants de __construct et __destruct, getNom à la place de getNum (8), self::planete sans dollar (27), appel parent présenté comme obligatoirement premier alors qu’il s’agit d’une convention du cours (20), concaténation de $this sans conversion définie (24).
- Chapitre 3 : nom DAO traditionnellement « Data Access Object » (le support inverse deux mots), accolades et underscores manquants dans plusieurs squelettes, affectation locale de la connexion, notations point au lieu de ->, méthode liberer appartenant à GestionConnexion et non PDO (21).
- Chapitre 4 : noms views/vues et layot/layout à harmoniser, include appelé « redirection » alors qu’il charge un fichier côté serveur, file_exists testant l’existence et non l’autorisation.

Les références de diapositives indiquent le point du cours utilisé ; les exercices peuvent adapter les valeurs tout en conservant la notion. Les réponses sont corrigées en PHP valide, pas reproduites mécaniquement à partir des coquilles.

## Inventaire diapositive par diapositive

### Chapitre 1 — 48 diapositives

| Diapo | Notions / contenu inspecté | Questions associées |
| --- | --- | --- |
| 1 | Titre et objectifs du chapitre | Contexte, illustration ou prolongement traité dans la fiche |
| 2 | Objectifs et progression PHP / POO / DAO / MVC | Contexte, illustration ou prolongement traité dans la fiche |
| 3 | Syntaxe, commentaires, echo et exécution serveur | c1-q001, c1-q002, c1-q004, c1-q006, c1-e002 |
| 4 | Variables, types et affectation | c1-q003, c1-q005, c1-e001 |
| 5 | Condition if et majorité | c1-q007, c1-e003 |
| 6 | if / else | c1-q008, c1-e003 |
| 7 | if / elseif / else et note | c1-q009, c1-e004 |
| 8 | Tableau des opérateurs de comparaison | c1-q010, c1-q011 |
| 9 | Tableau des opérateurs logiques | c1-q012, c1-q013, c1-q014 |
| 10 | Exercice : classement d’une note | c1-e004 |
| 11 | Capture de la solution et sorties Admis / Très bien | Contexte, illustration ou prolongement traité dans la fiche |
| 12 | Boucle for et compteur | c1-q015, c1-q016, c1-q050, c1-e005 |
| 13 | Boucle while | c1-q017, c1-q018, c1-e006 |
| 14 | foreach sur tableau indexé | c1-q019 |
| 15 | foreach avec clé et valeur | c1-q020, c1-e009 |
| 16 | Comparaison des trois boucles | Contexte, illustration ou prolongement traité dans la fiche |
| 17 | Exercice : produits, total, compteur et livraison | c1-q025, c1-q026, c1-q048, c1-e010 |
| 18 | Deux captures : 60 € / 3 et 44 € / 2 | c1-q025, c1-q026 |
| 19 | Définition des tableaux | Contexte, illustration ou prolongement traité dans la fiche |
| 20 | Indices et remplacement d’un fruit | c1-q021, c1-q022, c1-e007 |
| 21 | Clés et valeurs d’un tableau associatif | c1-q023, c1-q024, c1-e008 |
| 22 | Comparaison indexé / associatif | Contexte, illustration ou prolongement traité dans la fiche |
| 23 | Exercice : gestion des produits | c1-q048, c1-e008, c1-e010 |
| 24 | Capture : modification clavier à 30 €, total 910 € | Contexte, illustration ou prolongement traité dans la fiche |
| 25 | Déclaration et appel d’une fonction | c1-q027 |
| 26 | Fonction avec paramètres | c1-q028 |
| 27 | return, somme et différence avec echo | c1-q029, c1-q030, c1-q049, c1-e011 |
| 28 | Exercice : calcul de moyenne | c1-q031, c1-e012 |
| 29 | Captures : moyenne 12 et moyenne 7 | c1-q031 |
| 30 | Captures : readline, (float), résultat 5,666… | c1-q032 |
| 31 | Définition de page dynamique | Contexte, illustration ou prolongement traité dans la fiche |
| 32 | Schéma utilisateur / serveur PHP / navigateur | Contexte, illustration ou prolongement traité dans la fiche |
| 33 | Formulaire : action, method, name, id | c1-q033, c1-q034 |
| 34 | Formulaire GET de recherche | c1-q035 |
| 35 | Captures formulaire et URL recherche.php?mot=PHP | c1-q035 |
| 36 | Lecture GET, isset et htmlspecialchars | c1-q036, c1-q040, c1-e013 |
| 37 | Formulaire POST, nom et email | Contexte, illustration ou prolongement traité dans la fiche |
| 38 | Lecture POST, échappement, HTTPS | c1-q037, c1-q038, c1-q039, c1-q040, c1-e015 |
| 39 | Schéma formulaire / POST / traitement / résultat | Contexte, illustration ou prolongement traité dans la fiche |
| 40 | Comparaison GET / POST | Contexte, illustration ou prolongement traité dans la fiche |
| 41 | Exercice : produit et validation | c1-q044 |
| 42 | trim et opérateur ?? | c1-q041, c1-q042, c1-e014 |
| 43 | Validation et contradiction sur le prix nul | c1-q043, c1-q044, c1-e014 |
| 44 | Capture : php -S localhost:8000 | Contexte, illustration ou prolongement traité dans la fiche |
| 45 | Tableau récapitulatif des instructions | c1-q045, c1-q046 |
| 46 | Capture du formulaire et récapitulatif | Contexte, illustration ou prolongement traité dans la fiche |
| 47 | Extension : plusieurs produits et $_SESSION | c1-q047 |
| 48 | Capture : produits conservés, tableau et total | Contexte, illustration ou prolongement traité dans la fiche |

### Chapitre 2 — 32 diapositives

| Diapo | Notions / contenu inspecté | Questions associées |
| --- | --- | --- |
| 1 | Titre du chapitre | Contexte, illustration ou prolongement traité dans la fiche |
| 2 | Introduction à la POO PHP | Contexte, illustration ou prolongement traité dans la fiche |
| 3 | Objet : données et actions | c2-q002 |
| 4 | Classe et instance | c2-q001 |
| 5 | Déclaration et tableau des visibilités | c2-q003, c2-q004, c2-q005, c2-q039, c2-e001 |
| 6 | Méthodes fonction / procédure | c2-q040 |
| 7 | Exemples de getter et setter | c2-q006, c2-q007, c2-q037, c2-q038, c2-e002, c2-e003 |
| 8 | Utilisation des accesseurs et $this | c2-q008, c2-q009, c2-q045, c2-e004 |
| 9 | Instanciation et rôle du constructeur | c2-q010 |
| 10 | Nom du constructeur moderne | c2-q011 |
| 11 | Initialisation des attributs | c2-q012, c2-q041, c2-e005 |
| 12 | Un constructeur, comptage et lecture des arguments | c2-q013, c2-q014 |
| 13 | Indices 0, 1, 2 des arguments | c2-q015, c2-q046, c2-e006 |
| 14 | switch de surcharge simulée | c2-q016, c2-q017, c2-q018, c2-q019, c2-e007 |
| 15 | Appels à deux ou trois arguments | c2-q017 |
| 16 | Exercice Voiture : attributs | c2-q020 |
| 17 | Exercice Voiture : encapsulation et constructeur | Contexte, illustration ou prolongement traité dans la fiche |
| 18 | Exercice Voiture : coût et deux formats | c2-q021, c2-q022, c2-q047, c2-e008 |
| 19 | Capture du résultat des deux voitures | Contexte, illustration ou prolongement traité dans la fiche |
| 20 | Constructeur de classe fille | c2-q023, c2-q026 |
| 21 | Code Personne / Etudiant | c2-q011, c2-q023, c2-q024, c2-q025, c2-q026, c2-e010 |
| 22 | extends et parent:: | c2-q042, c2-e009 |
| 23 | Code Utilisateur héritant de Personne | c2-q027 |
| 24 | Destructeur et références | c2-q028, c2-q030, c2-e012 |
| 25 | Code Voiture, constructeur et destructeur | c2-q028, c2-q029 |
| 26 | Capture : création / fin / destruction | c2-q029 |
| 27 | Propriété et méthode static | c2-q031, c2-q032, c2-q033, c2-q034, c2-q048, c2-q050, c2-e013 |
| 28 | Appel de méthode statique avec :: | c2-q032, c2-e014 |
| 29 | Exercice plateforme : classe mère Utilisateur | Contexte, illustration ou prolongement traité dans la fiche |
| 30 | Exercice : Formateur et Apprenant | c2-q043, c2-q049, c2-e011 |
| 31 | Compteur statique d’utilisateurs | c2-q035, c2-q036, c2-q044, c2-e015 |
| 32 | Capture de cinq utilisateurs et compteur 5 | c2-q036 |

### Chapitre 3 — 34 diapositives

| Diapo | Notions / contenu inspecté | Questions associées |
| --- | --- | --- |
| 1 | Titre du chapitre | Contexte, illustration ou prolongement traité dans la fiche |
| 2 | Objets métier / DAO / stockage | Contexte, illustration ou prolongement traité dans la fiche |
| 3 | Durée de vie mémoire et persistance | c3-q001 |
| 4 | Deux étapes et supports BDR / XML | c3-q002, c3-q003 |
| 5 | Table et passerelle Personne | c3-q004 |
| 6 | SQL dans le métier et couplage | c3-q005 |
| 7 | Motivation des DAO | c3-q006 |
| 8 | Exemples d’insertion et suppression | c3-q007 |
| 9 | Schéma n-tiers, couches et machines | c3-q008 |
| 10 | Parcours utilisateur vers la base | c3-q009 |
| 11 | Principes : DAO associé et partagé | c3-q010, c3-q011 |
| 12 | Avantages : isolation et factorisation | c3-q012, c3-q013 |
| 13 | Exemple métier Soiree | c3-q014 |
| 14 | Exemple SoireeDAO et SQL | c3-q015, c3-q049, c3-e011, c3-e015 |
| 15 | Variante XML et changement de support | c3-q016 |
| 16 | Granularité DAO par table | c3-q017 |
| 17 | API : JDBC, OLE DB et PDO | c3-q018, c3-q019 |
| 18 | GestionConnexion et Singleton | c3-q020, c3-q021 |
| 19 | Code du service de connexion | c3-q022, c3-q023, c3-q024, c3-q025, c3-q026, c3-q027, c3-q048, c3-q050, c3-e002, c3-e003, c3-e004, c3-e005, c3-e006, c3-e007 |
| 20 | Squelette d’instance DAO | c3-q028, c3-q029, c3-q031, c3-e001 |
| 21 | Squelette statique DAO | c3-q030, c3-q031, c3-q050, c3-e012 |
| 22 | Tableau des opérations CRUD | c3-q032, c3-q033 |
| 23 | Create avec paramètres ou objet | c3-q034, c3-e011 |
| 24 | Retours possibles de Create | c3-q035 |
| 25 | Trois types de lectures | c3-q036, c3-q039 |
| 26 | Finders findById et findAll | c3-q037, c3-q038, c3-e010 |
| 27 | Variantes Update | c3-q040, c3-q041, c3-e013 |
| 28 | Variantes Delete | c3-q042, c3-e014 |
| 29 | Présentation des deux stratégies | Contexte, illustration ou prolongement traité dans la fiche |
| 30 | Schéma stratégie 1 : métier lié au DAO | c3-q043 |
| 31 | Code stratégie 1 et coquilles de notation | c3-q044, c3-e009 |
| 32 | Schéma stratégie 2 : application liée aux DAO | c3-q045 |
| 33 | Code stratégie 2 et appel creer | c3-q046, c3-q049, c3-e008, c3-e015 |
| 34 | Génération de DAO et accès centralisé | c3-q047 |

### Chapitre 4 — 50 diapositives

| Diapo | Notions / contenu inspecté | Questions associées |
| --- | --- | --- |
| 1 | Titre du chapitre | Contexte, illustration ou prolongement traité dans la fiche |
| 2 | Plan MVC | Contexte, illustration ou prolongement traité dans la fiche |
| 3 | Patron de conception et capitalisation | Contexte, illustration ou prolongement traité dans la fiche |
| 4 | Problèmes d’organisation du code | c4-q003 |
| 5 | Définition d’un patron de conception | c4-q002 |
| 6 | Les trois responsabilités MVC | c4-q001 |
| 7 | Modèle : logique et SQL | c4-q004, c4-q005 |
| 8 | Code query et fetchAll | c4-q006, c4-e005 |
| 9 | Vue : présentation HTML | c4-q007 |
| 10 | Code de vue avec foreach alternatif | c4-q008, c4-q009, c4-e006 |
| 11 | Contrôleur : coordination | c4-q010 |
| 12 | Code appel modèle puis include de vue | c4-q011, c4-q012, c4-e004 |
| 13 | Synthèse des interactions | Contexte, illustration ou prolongement traité dans la fiche |
| 14 | Schéma du cycle HTTP / SQL / données / HTML | c4-q013 |
| 15 | Vue externe et sous-vues | c4-q014 |
| 16 | Tableau header / menu / contenu / footer | c4-q015 |
| 17 | Arborescence views et layout | c4-q016, c4-e007 |
| 18 | Sous-vues communes et liées à la demande | c4-q017, c4-q018 |
| 19 | Exercice vues étudiants et arborescence | c4-e007 |
| 20 | Exercice liste, ajout et navigation | c4-q019 |
| 21 | Capture de la page assemblée | Contexte, illustration ou prolongement traité dans la fiche |
| 22 | Contrôleur principal index.php | c4-q020, c4-q021 |
| 23 | Menu et paramètre controleur | c4-q022 |
| 24 | Sous-contrôleurs et leurs responsabilités | c4-q023 |
| 25 | Tableau des sous-contrôleurs | c4-q024 |
| 26 | $_REQUEST[controleur] | c4-q025 |
| 27 | Point d’entrée toujours appelé | Contexte, illustration ou prolongement traité dans la fiche |
| 28 | Paramètre action et cas d’utilisation | c4-q026, c4-e008 |
| 29 | Code switch modifierProduit / voirCategories | c4-q027, c4-q028, c4-q029, c4-e009, c4-e010 |
| 30 | Schéma complet de consultation étudiants | c4-q030 |
| 31 | Modèle : préparation et accès aux données | c4-q031 |
| 32 | Cinq étapes de démarche | c4-q032, c4-q033, c4-q034 |
| 33 | Étape 1 : cas d’utilisation | c4-q035 |
| 34 | Étape 2 : vues externes | c4-q033 |
| 35 | Étape 3 : arborescence de l’application | c4-q034 |
| 36 | Étape 4 : contrôleur principal | c4-q034 |
| 37 | Code de routage et file_exists | c4-q036, c4-q037, c4-q038, c4-q039, c4-e001, c4-e002, c4-e003 |
| 38 | Test par URL du point d’entrée | c4-q040 |
| 39 | Étape 5 : coder l’ajout | c4-q041 |
| 40 | Synthèse MVC et démarche | Contexte, illustration ou prolongement traité dans la fiche |
| 41 | Exercice catalogue de films | c4-q042 |
| 42 | Arborescence du catalogue | Contexte, illustration ou prolongement traité dans la fiche |
| 43 | Contrats des quatre méthodes Film | c4-q043, c4-q044, c4-e011, c4-e012, c4-e013 |
| 44 | Sous-vues communes du catalogue | c4-q045 |
| 45 | Vue de liste des films | c4-q046 |
| 46 | Vue de détail d’un film | c4-e012 |
| 47 | Formulaire d’ajout et catégories | c4-q047, c4-q048, c4-e014 |
| 48 | Actions liste / details / categorie / ajouter / enregistrer | c4-q049, c4-e011, c4-e012, c4-e013, c4-e014 |
| 49 | Point d’entrée du catalogue et défaut films | c4-q050, c4-e015 |
| 50 | Trois scénarios de test fonctionnel | c4-q050 |

