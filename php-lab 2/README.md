# PHP Lab

Application de révision statique, en français, à partir des quatre PowerPoint fournis : **164 diapositives analysées, 200 QCM et 60 exercices courts**. Chaque chapitre contient 50 QCM et 15 exercices. Aucune dépendance à installer pour utiliser le site ; aucun compte, service payant, CDN ou serveur PHP.

## Mise à jour du site déjà publié

La révision 2 corrige les renvois à des exemples absents et limite les nouveaux examens blancs aux chapitres 2 et 3. La banque des quatre chapitres reste disponible dans les autres modes. Les identifiants et réponses attendues sont conservés ; les anciens résultats et examens sauvegardés restent lisibles. Une copie commencée avec l’ancienne formule est identifiée comme « Ancien examen · 4 chapitres ».

Pour remplacer un seul fichier sur GitHub, utiliser l’`index.html` autonome fourni dans `php-lab-mise-a-jour`. Dans le dépôt actuel, ouvrir le dossier **php-lab 2**, puis **Add file → Upload files**, envoyer cet `index.html` et valider **Commit changes**. Il contient tout le code et toutes les questions : les anciens dossiers ne sont plus utilisés par cette page. L’adresse publique reste la même et la clé LocalStorage est conservée.

Pour travailler sur la version modulaire, remplacer les fichiers du projet complet, puis régénérer `PHP-Lab-autonome.html` après toute modification. Le fichier de déploiement autonome est généré à partir des mêmes sources, sans banque différente.

## Ouvrir sans installation

Ouvrir **`PHP-Lab-autonome.html`** dans un navigateur : ce fichier contient le style, le JavaScript et les 260 questions. Il ne charge aucun JSON externe et ne nécessite aucun serveur ni connexion Internet. Les statistiques restent propres à ce fichier et au navigateur ; utiliser l’export/import pour les transférer.

Cette version a été contrôlée sur HTTP local (chargement et examen de 24 questions). Le navigateur de test intégré bloque le protocole `file://` : l’ouverture directe par double-clic n’a pas pu y être vérifiée. Si un navigateur interdit le LocalStorage sur un fichier local, utiliser le lancement HTTP ci-dessous pour la sauvegarde persistante.

Pour reconstruire ce fichier après une modification des sources : `python3 scripts/build-standalone.py`.

## Lancer la version modulaire en local

Dans un terminal ouvert dans ce dossier :

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

Ouvrir [PHP Lab en local](http://localhost:8080). Garder le terminal ouvert ; `Ctrl+C` arrête le serveur. Sur macOS, le fichier `lancer.command` lance le même serveur ; si le port est déjà occupé, exécuter `./lancer.command 8081` et ouvrir `http://localhost:8081`.

Pour `index.html`, le serveur sert uniquement les fichiers statiques. Il n’exécute pas le PHP saisi. Contrairement au fichier autonome, l’ouverture de `index.html` par double-clic (`file://`) bloque généralement le chargement des JSON : utiliser l’adresse HTTP ci-dessus. Python 3 est nécessaire uniquement pour cet aperçu local ; GitHub Pages n’en a pas besoin.

## Les six modes

- **Examen blanc** : exactement 20 QCM et 4 exercices, sur les chapitres 2 et 3 uniquement : dix QCM et deux exercices de code par chapitre. Ordre des questions et propositions mélangé, sans répétition dans la copie. Durée et poids QCM/code configurables. Réponses modifiables, marquage, navigation, confirmation de remise, correction complète.
- **Par chapitre** : résumé, fiche détaillée, 10 ou 50 QCM, 15 exercices, couverture, taux de réussite et thèmes à retravailler.
- **QCM personnalisé** : chapitres, nombre, difficulté, choix unique/multiples/vrai-faux, correction immédiate ou différée, minuterie facultative. Si le filtre fournit moins de questions, la taille réelle est annoncée et limitée au disponible.
- **Code** : éditeur avec coloration, numéros de ligne, Tab et indentation à la ligne suivante, indice, référence, variantes, explications et grille de vérification.
- **Erreurs** : questions ratées et questions marquées difficiles, reprises ciblées, corrections, regroupement des erreurs récurrentes par thème. Une erreur quitte la liste après trois bonnes réponses consécutives sur la question.
- **Express** : douze questions équilibrées (deux QCM et un code par chapitre), erreurs prioritaires puis notions essentielles.

Les quatre fiches et la fiche globale « L’essentiel à connaître avant l’examen » sont consultables et imprimables. « Imprimer les 5 fiches » ouvre une page réunissant les fiches ; utiliser ensuite le bouton d’impression pour enregistrer en PDF.

## Évaluation : règles explicites

Les QCM multiples sont justes si l’ensemble sélectionné correspond exactement aux bonnes réponses, indépendamment de l’ordre. Pas de points partiels ni de pénalité négative pour les QCM.

**Aucun moteur PHP n’est embarqué.** Le site n’exécute ni ne prétend analyser sémantiquement le code saisi. Comparer le comportement à la correction et aux trois critères, puis choisir 0 %, 50 % ou 100 %. Une syntaxe équivalente (espaces, indentation, guillemets compatibles, autre solution correcte) ne doit pas être pénalisée. Les paramètres et propriétés mentionnés dans le contexte sont supposés déjà définis ; certains exercices demandent une méthode à placer dans une classe.

En examen, aucune correction ni indice n’apparaît avant la remise. Après remise, la note est **provisoire** tant qu’un exercice saisi reste à auto-évaluer. Une absence de réponse vaut zéro. La note finale est :

```text
20 × points obtenus / points possibles
points possibles = (nombre QCM × poids QCM) + (nombre code × poids code)
```

Par défaut : QCM = 1, code = 5, donc 40 points possibles en examen. Une auto-évaluation à 50 % reste un essai à retravailler pour les statistiques de maîtrise. La moyenne et le meilleur score d’examens ignorent les copies dont l’auto-évaluation est inachevée.

La préparation affichée vaut `couverture × (0,5 + 0,5 × taux de réussite)`, avec des taux de 0 à 1. C’est un repère de révision sans garantie de réussite. « Questions réalisées » compte les questions uniques évaluées ; le taux global compte tous les essais évalués.

## Sauvegarde et données

La clé LocalStorage est `php-lab-v1`. Les réponses, l’ordre des choix, le temps de départ, l’index courant, les marquages et les résultats sont sauvegardés. L’horloge utilise la date absolue : elle continue pendant une fermeture ou une navigation vers une autre page. Une session expirée est remise automatiquement à la réouverture.

Dans **Préférences et données**, exporter/importer un JSON ou réinitialiser avec confirmation. L’import vérifie le format, les identifiants et la cohérence de la session avant remplacement. Une session en cours remplacée est perdue après confirmation ; les essais déjà évalués restent comptés. L’historique garde les 100 dernières sessions, les statistiques par question restent cumulatives.

Les sauvegardes sont propres à l’adresse du site et au navigateur : `localhost`, `127.0.0.1`, un autre port et GitHub Pages sont des origines différentes. Exporter puis importer pour transférer sa progression. Éviter la navigation privée pour conserver les données. Les données restent locales ; pas de télémétrie.

## Publier sur GitHub Pages

1. Créer un dépôt GitHub, puis y déposer **le contenu de ce dossier** (avec `index.html` à la racine, ainsi que `css`, `js`, `data`, `assets` et `.nojekyll`). Les PowerPoint originaux et le dossier d’analyse temporaire ne sont pas nécessaires.
2. Dans le dépôt, ouvrir **Settings → Pages**.
3. Choisir **Deploy from a branch**, branche `main`, dossier `/(root)`, puis enregistrer.
4. Attendre la publication puis ouvrir l’adresse affichée par GitHub Pages.

Si le dépôt contient ce projet dans un sous-dossier `php-lab`, le site sera accessible à `https://UTILISATEUR.github.io/DEPOT/php-lab/`, à condition d’avoir publié la racine du dépôt. Tous les liens d’assets et de données sont relatifs, et la navigation utilise les fragments `#/…` : aucun routage serveur ni build n’est nécessaire. GitHub Pages héberge les fichiers sans exécuter PHP. L’hébergement effectif n’est pas réalisé par ce livrable local.

## Architecture et extension

```text
index.html
css/style.css
js/app.js           Navigation et interfaces
js/quiz.js          Sélection, mélange, session et score
js/exam.js          Composition équilibrée des examens
js/code-editor.js   Éditeur et coloration locale
js/statistics.js    Couverture, maîtrise et résultats
js/storage.js       Sauvegarde et validation des imports
data/chapitre-1.json … chapitre-4.json
data/chapters.json  Fiches et résumés
data/build_bank.py  Source éditoriale reproductible
data/editorial.py   Relecture des distracteurs
data/self_contained.py  Énoncés autonomes et contrats explicites
tests/core.test.js
docs/ANALYSE.md
docs/VALIDATION.md
lancer.command
```

Chaque question a `id`, `chapter`, `slides`, `theme`, `difficulty`, `type`, `prompt`, `answer`, `explanation` et `essential`. Les énoncés sont autonomes : données, contrats et code nécessaires sont fournis sur la question. Les QCM contiennent des options à identifiants stables et une explication par proposition ; `answer` contient leurs identifiants, jamais leur position affichée. Le code contient `context`, `hint`, `lineExplanation`, `commonErrors`, `rubric`, `alternatives` et `validation: "self"`.

Pour modifier la banque, éditer les sources Python puis exécuter `python3 data/build_bank.py`, ou modifier directement les JSON sans les régénérer ensuite. Pour augmenter les effectifs à partir des sources Python, adapter les assertions 50/15 du générateur et les contrôles de taille/import. Le fichier `data/chapters.json` contient les cinq fiches (la globale est assemblée dans l’interface).

## Vérifications

Pour le développement, Node.js et PHP CLI sont nécessaires aux tests (ils ne sont pas nécessaires à l’utilisation du site) :

```sh
npm test
```

Le test PHP vérifie la syntaxe des 60 corrections et variantes dans leur contexte. D’autres contrôles exécutent des exemples de prédiction. Les tests JavaScript couvrent notamment 500 examens, mélange, réponses multiples, score pondéré, auto-évaluation, filtres, maîtrise, import/export et horloge. Voir `docs/VALIDATION.md` pour les parcours contrôlés dans le navigateur.

## Sources pédagogiques

- Chapitre 1 : *Rappels PHP & pages Web dynamiques*, 48 diapositives.
- Chapitre 2 : *Création de classes métiers en PHP*, 32 diapositives.
- Chapitre 3 : *Création des classes DAO*, 34 diapositives.
- Chapitre 4 : *Architecture MVC*, 50 diapositives.

La numérotation suit l’ordre des diapositives. Les coquilles des supports sont signalées dans les fiches ; les corrections emploient une syntaxe PHP valide. Le titre et la structure s’inspirent de [CCNA Lab](https://aloyslrtg.github.io/ccna-lab/), sans reprendre sa banque de questions. Le site ne prédit pas le sujet de l’examen.
