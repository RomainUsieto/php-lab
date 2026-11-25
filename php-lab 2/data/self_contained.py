"""Révision pédagogique : chaque question fournit ses hypothèses et son extrait.
Les références de diapositives restent des métadonnées, jamais un prérequis de lecture.
"""
def apply(banks):
    questions = {q['id']: q for items in banks.values() for q in items}
    def edit(id, **changes):
        questions[id].update(changes)
    def option(id, position, text=None, explanation=None):
        o = questions[id]['options'][position]
        if text is not None: o['text'] = text
        if explanation is not None: o['explanation'] = explanation

    edit('c1-q007', prompt='Quelle condition accepte tous les âges supérieurs ou égaux à 18 ans, en incluant 18 ans ?')
    # Fondamentaux : les valeurs et les champs utiles sont visibles dans la question.
    edit('c1-q020', code='$etudiant = ["nom" => "Anna", "age" => 20];\nforeach ($etudiant as $cle => $valeur) {\n    echo $cle . " : " . $valeur;\n}')
    edit('c1-q023', code='$etudiant = ["nom" => "Alex", "age" => 20, "ville" => "Anglet"];')
    edit('c1-q025', explanation='En additionnant les cinq prix indiqués : 12 + 8 + 15 + 20 + 5 = 60 €.')
    option('c1-q025', 3, explanation='44 € n’est pas la somme des cinq prix donnés dans cet énoncé.')
    edit('c1-q028', code='function saluer($nom) {\n    echo "Bonjour " . $nom;\n}\nsaluer("Alex");')
    edit('c1-q031', explanation='La moyenne arithmétique vaut (12 + 15 + 9) / 3 = 12. Elle est supérieure ou égale à 10.')
    edit('c1-q035', prompt='Ce formulaire est envoyé avec le texte « PHP » dans le champ mot. Quelle URL est obtenue ?',
         code='<form action="recherche.php" method="get">\n    <input type="text" name="mot" value="PHP">\n    <button type="submit">Rechercher</button>\n</form>')
    edit('c1-q043', prompt='Quelle fonction teste si $prix contient une valeur numérique ?')
    edit('c1-q044', prompt='On impose un prix strictement positif. Après avoir vérifié is_numeric($prix), quelle condition rejette les nombres invalides ?',
         explanation='Un prix strictement positif vérifie $prix > 0. Il faut donc rejeter $prix <= 0, ce qui exclut aussi zéro.')
    edit('c1-q047', prompt='Une page ajoute des produits lors de plusieurs soumissions de formulaire. Pourquoi conserver la liste dans $_SESSION ?')
    edit('c1-e009', context='$produits est déjà défini, par exemple ["Clavier" => 25, "Souris" => 15]. La boucle doit fonctionner aussi avec d’autres produits.')
    edit('c1-e010', context='$produits est déjà défini, par exemple ["Clavier" => 25, "Souris" => 15]. Calcule un total pour toutes ses valeurs, pas seulement pour cet exemple.')

    # Classes : aucun accesseur, constructeur ou comportement n’est à deviner.
    edit('c2-q006', prompt='Quel est le rôle de cette méthode setNum($nvNum) ?',
         code='class Personne {\n    private $num;\n    public function setNum($nvNum) {\n        $this->num = $nvNum;\n    }\n}')
    edit('c2-q007', prompt='Personne possède une propriété privée $num. Quel corps de méthode permet à getNum() de renvoyer sa valeur ?',
         context='La réponse doit renvoyer l’attribut de l’objet courant, sans l’afficher ni le modifier.')
    edit('c2-q009', prompt='$personne est un objet dont la méthode publique non statique getNum() renvoie son numéro. Comment appeler cette méthode ?')
    edit('c2-q012', prompt='Dans le constructeur d’un objet, le paramètre $leNom doit initialiser la propriété nom. Quelle affectation convient ?')
    edit('c2-q015', prompt='Dans le constructeur appelé par new Personne(12, "Dupont", "TechNova"), quelle valeur fournit func_get_arg(1) ?',
         context='Le constructeur reçoit les trois arguments dans l’ordre indiqué : numéro, nom, société.')
    edit('c2-q016', prompt='Un constructeur utilise switch (func_num_args()) pour distinguer le nombre d’arguments reçus. Quelle étiquette case traite un appel à deux arguments ?',
         explanation='func_num_args() renvoie le nombre reçu : pour deux arguments, le switch sélectionne case 2. Les indices individuels commencent à 0, mais le nombre vaut bien 2.')
    edit('c2-q017', prompt='Quelle valeur de societe est affectée lors de cet appel à deux arguments ?',
         code='class Personne {\n    private $num;\n    private $nom;\n    public $societe;\n    public function __construct() {\n        $this->num = func_get_arg(0);\n        $this->nom = func_get_arg(1);\n        if (func_num_args() == 3) {\n            $this->societe = func_get_arg(2);\n        } else {\n            $this->societe = "inconnu";\n        }\n    }\n}\n$p = new Personne(13, "Martin");',
         explanation='L’appel fournit deux arguments. Le test == 3 est donc faux et la branche else affecte la chaîne "inconnu" à societe.')
    option('c2-q017', 1, explanation='TechNova ne figure pas dans l’appel : deux arguments ne fournissent aucune société.')
    option('c2-q017', 3, explanation='Le code affecte explicitement "inconnu", et non null.')
    edit('c2-q018', prompt='Un constructeur contient un switch avec plusieurs case. Quel est le rôle de break à la fin d’un case ?')
    edit('c2-q019', prompt='Un constructeur teste le nombre d’arguments avec switch (func_num_args()). Que fait la branche default: exit(1); si aucun case ne correspond ?',
         explanation='La branche default est choisie pour un nombre non traité par les case. exit(1) arrête alors le programme avec le statut de sortie 1.')
    option('c2-q019', 0, explanation='Les case acceptent certains nombres d’arguments ; le défaut arrête l’exécution pour les autres.')
    option('c2-q019', 2, explanation='default ne sélectionne pas case 1 ; exit arrête le programme.')
    edit('c2-q021', prompt='Voiture possède la propriété prixJournalier. Quelle expression doit renvoyer calculerPrixLocation($nbJours) pour calculer le coût total de la location ?',
         context='Le coût total correspond au tarif d’un jour multiplié par le nombre de jours. La propriété n’est pas statique.')
    edit('c2-q022', prompt='Ce constructeur est appelé avec les quatre arguments indiqués. Quelle valeur reçoit disponible ?',
         code='class Voiture {\n    private $disponible;\n    public function __construct() {\n        if (func_num_args() == 4) {\n            $this->disponible = true;\n        } else {\n            $this->disponible = func_get_arg(4);\n        }\n    }\n}\n$v = new Voiture("AB-123-CD", "Peugeot", "208", 50);',
         explanation='L’appel contient quatre arguments. Le test == 4 est vrai, donc disponible est initialisé à true.')
    option('c2-q022', 1, explanation='La branche à quatre arguments affecte true, pas false.')
    option('c2-q022', 2, explanation='Le quatrième argument 50 est le tarif ; la branche choisie ne le lit pas comme disponibilité.')
    option('c2-q022', 3, explanation='La branche if initialise bien la propriété.')
    edit('c2-q024', prompt='Etudiant hérite de Personne, dont le constructeur public reçoit $nom. Depuis le constructeur d’Etudiant, quelle instruction appelle celui de Personne ?')
    edit('c2-q025', prompt='Dans ces déclarations, quel attribut est ajouté uniquement par la classe fille Etudiant ?',
         code='class Personne {\n    protected $nom;\n    public $societe;\n}\nclass Etudiant extends Personne {\n    private $formation;\n}')
    option('c2-q025', 1, explanation='nom est déclaré dans la classe mère Personne.')
    option('c2-q025', 2, explanation='societe est aussi déclaré dans la mère, pas ajouté dans la fille.')
    option('c2-q025', 3, explanation='Un constructeur est une méthode ; aucun attribut de ce nom n’est déclaré ici.')
    edit('c2-q026', prompt='Une classe fille redéfinit __construct. PHP appelle-t-il en plus automatiquement le constructeur de la mère ?',
         explanation='Non. Si la fille définit son propre constructeur, elle doit appeler explicitement parent::__construct(...) quand l’initialisation de la mère est nécessaire.')
    option('c2-q026', 0, 'Non, la fille doit appeler explicitement parent::__construct(...)', 'La redéfinition du constructeur ne déclenche pas un appel supplémentaire implicite à celui de la mère.')
    edit('c2-q027', prompt='Utilisateur hérite de Personne. Personne déclare num private et getNum() public. Comment une méthode d’Utilisateur peut-elle obtenir ce numéro ?')
    edit('c2-q029', prompt='Dans quel ordre ces trois messages sont-ils affichés, jusqu’à la fin du script ?',
         code='class Voiture {\n    public function __construct() { echo "Création"; }\n    public function __destruct() { echo "Destruction"; }\n}\n$voiture = new Voiture();\necho "Fin du programme";',
         explanation='new appelle le constructeur et affiche Création. Le echo suivant affiche Fin du programme. La variable conserve l’objet jusqu’à la fin du script, puis son destructeur affiche Destruction.')
    edit('c2-q032', prompt='Personne déclare public static function donnePlanete(). Quelle expression appelle cette méthode ?')
    edit('c2-q033', prompt='Personne contient private static $planete = "Terre". Depuis une méthode de Personne, quelle expression lit cette propriété statique ?',
         explanation='Une propriété statique s’écrit self::$planete depuis sa classe : le dollar reste nécessaire après ::.')
    edit('c2-q034', prompt='La propriété private static $planete = "Terre" existe dans Personne. Quelle méthode publique statique la renvoie correctement ?')
    edit('c2-q035', prompt='Utilisateur possède un compteur statique initialisé à zéro. Pour compter une fois chaque création d’utilisateur, où faut-il incrémenter ce compteur ?',
         context='Formateur et Apprenant héritent d’Utilisateur et appellent chacun une fois le constructeur parent lors de leur construction.')
    edit('c2-q036', prompt='Un compteur statique commence à 0 et est incrémenté une fois par appel au constructeur Utilisateur. Deux Formateur et trois Apprenant appellent chacun ce constructeur une fois. Quel total obtient-on ?',
         explanation='Cinq constructions provoquent chacune une incrémentation : 0 + 2 + 3 = 5.')
    edit('c2-q037', prompt='Les numéros sont des propriétés d’instance dans cette classe. Qu’affiche le programme ?',
         code='class Personne {\n    private $num;\n    public function setNum($nvNum) { $this->num = $nvNum; }\n    public function getNum() { return $this->num; }\n}\n$a = new Personne();\n$b = new Personne();\n$a->setNum(12);\n$b->setNum(13);\necho $a->getNum();')
    edit('c2-q040', prompt='Une méthode utilisée comme une procédure, sans valeur de retour explicite…',
         explanation='Le terme procédure décrit ici une action sans retour explicite. La méthode se déclare néanmoins avec function et peut recevoir des paramètres.')
    edit('c2-q043', prompt='Utilisateur possède afficherInfos() public, qui affiche les données communes. Formateur la redéfinit pour ajouter sa spécialité. Comment réutiliser l’affichage commun ?')
    edit('c2-q044', prompt='Utilisateur possède private static $nombreUtilisateurs = 0. Quel corps convient à son getter public statique getNombreUtilisateurs() ?')
    edit('c2-q049', prompt='Formateur et Apprenant ont chacun id, nom et email. Seul Formateur possède specialite, et seul Apprenant possède formation. Quelles données regrouper dans leur classe mère Utilisateur ?')
    edit('c2-e008', context='Fragment à placer dans Voiture. Sa propriété privée non statique $prixJournalier existe déjà et contient un tarif numérique.')
    edit('c2-e010', context='Etudiant extends Personne. Personne possède public function __construct($nom), qui initialise nom. Etudiant déclare déjà private $formation. Écris uniquement le constructeur de la fille.')
    edit('c2-e011', context='Formateur extends Utilisateur. Utilisateur possède afficherInfos() public qui affiche les données communes ; Formateur possède private $specialite. Écris uniquement la méthode de Formateur.')

    edit('c2-q045', prompt='Personne possède num private, setNum($valeur) public et getNum() public. $p est une instance de Personne. Quelles opérations respectent cette encapsulation ?')
    edit('c2-q046', prompt='À l’intérieur d’un constructeur appelé avec numéro, nom puis société, quelle expression fournit le troisième argument ?')
    edit('c2-e004', context='Personne est instanciable sans argument. setNum($valeur) est une méthode publique qui modifie son attribut num ; getNum() est une méthode publique qui renvoie cet attribut.')
    # DAO : les contrats sont fournis et les stratégies décrites sans numéros à mémoriser.
    edit('c3-q002', prompt='Pour conserver puis retrouver les informations d’objets après la fin du programme, quels éléments faut-il mettre en place ?')
    edit('c3-q003', prompt='Quel couple contient deux supports permettant de conserver des données après l’arrêt d’un programme PHP ?')
    edit('c3-q009', prompt='Dans une application séparant présentation, métier et persistance par des DAO, quel parcours des couches respecte leurs responsabilités ?')
    edit('c3-q011', prompt='On veut séparer les données d’une personne des opérations qui l’enregistrent dans une base. Quelle organisation est cohérente ?')
    edit('c3-q014', prompt='Soiree est une classe métier contenant la date, la nature et le nombre de places d’une soirée. Quel membre correspond à son rôle métier ?')
    edit('c3-q015', prompt='Une méthode DAO creer($objLaSoiree) reçoit une soirée à enregistrer. Pourquoi lit-elle les attributs via les getters publics de cet objet ?')
    edit('c3-q016', prompt='La méthode creer de SoireeDAO conserve le même contrat public mais enregistre désormais en XML au lieu d’une base relationnelle. Que montre cette modification ?')
    edit('c3-q017', prompt='Pour une base comportant de nombreuses tables, quelle organisation des DAO permet de regrouper les opérations relatives à chaque table ?')
    edit('c3-q018', prompt='Parmi ces propositions, quelle API PHP sert à accéder à des bases de données relationnelles ?')
    edit('c3-q020', prompt='Une classe technique GestionConnexion centralise l’ouverture et le partage d’une connexion PDO. Quel rôle remplit-elle vis-à-vis des DAO ?')
    edit('c3-q022', prompt='On construit un Singleton de connexion : GestionConnexion expose getConnexion() public statique et son constructeur est private. Pourquoi choisir cette visibilité pour le constructeur ?')
    edit('c3-q023', prompt='GestionConnexion expose public static function getConnexion() qui renvoie PDO et possède un constructeur privé. Quel appel permet d’obtenir la connexion ?')
    edit('c3-q024', prompt='Une méthode statique getConnexion() crée une instance de GestionConnexion seulement si is_null(self::$_instance) est vrai. Que permet ce test ?')
    edit('c3-q025', prompt='Quels éléments de configuration sont transmis dans cet appel PDO ?',
         code='$pdo = new PDO(\n    "mysql:host=localhost;dbname=nomBase",\n    "login",\n    "mdp"\n);',
         explanation='Le premier argument est le DSN qui précise le pilote, l’hôte et la base ; les deux suivants sont l’identifiant et le mot de passe.')
    edit('c3-q026', prompt='GestionConnexion conserve l’objet de gestion dans $_instance et l’objet PDO dans $laConnexion, tous deux statiques. Quelle expression sa méthode getConnexion() doit-elle renvoyer aux DAO ?',
         explanation='Les DAO ont besoin de PDO, conservé dans self::$laConnexion. self::$_instance désigne l’objet GestionConnexion utilisé pour contrôler sa création.')
    edit('c3-q027', prompt='Que fait cette méthode liberer(), placée dans GestionConnexion ?',
         code='public static function liberer() {\n    self::$_instance = null;\n    self::$laConnexion = null;\n}',
         context='Les deux propriétés sont statiques. D’autres objets peuvent encore conserver une référence à la même connexion PDO.',
         explanation='La méthode retire les références détenues par ces deux propriétés. Elle ne supprime aucune donnée persistante et ne garantit pas la destruction de PDO si une autre référence existe.')
    edit('c3-q028', prompt='On veut qu’un objet DAO réutilise, dans plusieurs méthodes, la connexion reçue à sa construction. Où la conserver dans la forme d’instance ?')
    edit('c3-q029', prompt='Un DAO déclare private $laConnexion. Quel constructeur initialise cet attribut pour que ses autres méthodes puissent utiliser PDO ?',
         context='GestionConnexion::getConnexion() est une méthode publique statique qui renvoie la connexion.')
    edit('c3-q030', prompt='On souhaite appeler les opérations du DAO directement avec NomTableDAO::methode(), sans créer d’objet DAO. Comment déclarer ces méthodes publiques ?')
    edit('c3-q034', prompt='Une soirée contient une date, une nature et un nombre de places. Quelles signatures permettent de transmettre ces informations à une méthode DAO de création ?',
         context='$objetSoiree est un objet métier dont les getters publics donnent accès à ces trois informations.')
    edit('c3-q036', prompt='Quel groupe décrit trois formes possibles de résultat d’une opération de lecture Read dans un DAO ?')
    edit('c3-q037', prompt='Dans un DAO, une méthode de recherche s’appelle findById($id). Quel est le contrat habituel correspondant à ce nom ?')
    edit('c3-q038', prompt='Un DAO utilise les noms findById, findAll, creer et detruire pour ses opérations. Quelle méthode choisir pour lire tous les enregistrements ?')
    edit('c3-q042', prompt='Quelles informations peut-on transmettre à une méthode Delete pour désigner un enregistrement précis à supprimer ?')
    edit('c3-q043', prompt='Un objet métier possède une référence vers un DAO et lui délègue lui-même sa sauvegarde. Dans cette organisation, qui connaît directement le DAO ?')
    edit('c3-q044', prompt='Soiree possède sauvegardeToi(), qui appelle son propre DAO pour s’enregistrer. Quel appel permet au programme de demander une sauvegarde sans manipuler le DAO lui-même ?',
         context='$uneSoiree est une instance de Soiree. sauvegardeToi() est une méthode publique d’instance.')
    edit('c3-q045', prompt='Le programme appelle un DAO avec un objet métier ; cet objet ne possède aucune référence au DAO. Quel avantage apporte cette organisation ?',
         explanation='L’objet métier reste indépendant de la passerelle de persistance. Le programme coordonne les appels au DAO, ce qui isole mieux les responsabilités.')
    option('c3-q045', 1, explanation='Le programme connaît et appelle bien le DAO ; c’est l’objet métier qui n’en garde pas de référence.')
    option('c3-q045', 3, explanation='Créer une soirée ne l’enregistre pas automatiquement : le programme doit appeler le DAO.')
    edit('c3-q046', prompt='On veut garder Soiree indépendante de tout DAO et confier la sauvegarde au programme principal. Quelle séquence correspond à ce choix ?',
         explanation='Le programme crée les deux objets puis transmet la soirée à $dao->creer($soiree). La classe Soiree n’a pas besoin de conserver le DAO.')
    option('c3-q046', 1, explanation='Si Soiree appelle son propre DAO, elle connaît la passerelle, contrairement au choix annoncé.')
    edit('c3-q048', prompt='Dans une méthode statique de GestionConnexion, quelle expression lit la propriété statique $laConnexion de cette classe ?')
    edit('c3-q050', prompt='GestionConnexion définit public static function liberer(). Quelle instruction appelle correctement cette méthode ?')
    edit('c3-e001', context='GestionConnexion existe et sa méthode publique statique getConnexion() renvoie PDO. Écris la classe DAO complète, sans implémenter d’opération CRUD.')
    edit('c3-e002', context='GestionConnexion existe. Elle propose public static function getConnexion(), qui renvoie la connexion PDO partagée. Écris uniquement l’appel et son affectation.')
    edit('c3-e005', context='Fragment du corps de getConnexion(), méthode statique de GestionConnexion. La classe possède private static $_instance = null et son constructeur privé initialise la connexion.')
    edit('c3-e006', context='Dans GestionConnexion : private static $_instance = null conserve l’objet de gestion ; private static $laConnexion conserve PDO. Le constructeur privé __construct() initialise $laConnexion. Écris uniquement la méthode publique statique getConnexion().')
    edit('c3-e008', context='Soiree possède public function __construct($date, $nature, $places). SoireeDAO est instanciable sans argument et possède public function creer($soiree). Écris uniquement les trois instructions du programme appelant.')
    edit('c3-e009', context='Fragment à placer dans Soiree. Sa propriété privée $objSoireeDAO est déjà initialisée avec un DAO. Ce DAO possède la méthode publique d’instance creer($soiree), qui reçoit la soirée à enregistrer et renvoie un résultat.')
    edit('c3-e010', context='$dao est un objet DAO déjà initialisé. Sa méthode publique findById($id) renvoie une personne ; findAll() renvoie la collection de toutes les personnes.')
    edit('c3-e011', prompt='Dans SoireeDAO, écris creer($soiree) qui extrait la date dans $date, la nature dans $nature et le nombre de places dans $places. Écris uniquement cette préparation, sans SQL.',
         context='$soiree propose les getters publics getLaDateSoiree(), getLaNature() et getLeNbPlaces(). Écris une méthode publique d’instance creer($soiree) à placer dans SoireeDAO.')
    edit('c3-e013', context='$dao est un objet DAO déjà initialisé. Sa méthode publique modifier($id, $nom) modifie la personne indiquée et renvoie un booléen de réussite.')
    edit('c3-e015', context='Dans le constructeur de SoireeDAO, la propriété private $_db doit conserver PDO. GestionConnexion expose public static function getConnexion(), qui renvoie cette connexion.')

    # MVC : les cas concrets sont décrits, sans demander de mémoriser un TP absent.
    edit('c4-q003', prompt='Quelles questions portent sur la conception et l’organisation d’une application ?')
    edit('c4-q004', prompt='Dans une architecture MVC séparant données, affichage et coordination, où placer les requêtes SQL ?')
    edit('c4-q012', prompt='Le contrôleur doit afficher une liste d’étudiants. Pourquoi préparer $etudiants avant l’inclusion de la vue ?',
         code='$etudiants = obtenirLesEtudiants($pdo);\ninclude("vues/liste_etudiants.php");',
         context='obtenirLesEtudiants($pdo) est une fonction du modèle qui renvoie la collection ; la vue parcourt $etudiants pour produire le HTML.')
    edit('c4-q013', prompt='Dans le cycle d’une page PHP utilisant MVC, quel contenu le serveur envoie-t-il finalement au navigateur ?')
    edit('c4-q014', prompt='Dans une interface composée d’un en-tête, d’un menu, d’un contenu central et d’un pied de page, que désigne la vue externe complète ?')
    edit('c4-q018', prompt='On sépare les fichiers entre controleurs/, modeles/ et vues/. Dans quel dossier ranger les fichiers PHP/HTML responsables de l’affichage ?')
    edit('c4-q021', prompt='index.php est le point d’entrée d’une application MVC et délègue le traitement à des sous-contrôleurs. Quelles tâches lui correspondent ?')
    edit('c4-q022', prompt='Une application utilise index.php?controleur=films&action=liste. Par convention, controleur choisit un groupe de traitements et action sa fonctionnalité. Que sélectionne controleur ?')
    edit('c4-q024', prompt='Une application sépare les traitements des étudiants, de l’authentification et des formations. Quel regroupement de sous-contrôleurs respecte ces domaines ?')
    edit('c4-q025', prompt='Quelle expression PHP lit le paramètre controleur dans la superglobale $_REQUEST ?')
    categories_code='switch ($action) {\n    case "voirCategories":\n        $lesCategories = $laConnexion->getLesCategories();\n        include("vues/v_categories.php");\n        break;\n}'
    edit('c4-q027', prompt='Quel enchaînement est réalisé lorsque $action vaut "voirCategories" ?', code=categories_code,
         context='$laConnexion est ici un objet du modèle ; getLesCategories() renvoie les données à afficher.')
    edit('c4-q028', prompt='D’après cet extrait du contrôleur, quelles données sont préparées pour la vue de modification ?',
         code='$idProduit = $_REQUEST["produit"];\n$leProduit = $laConnexion->getLeProduit($idProduit);\n$lesCategories = $laConnexion->getLesCategories();\ninclude("vues/v_modif_produit.php");',
         context='Le paramètre produit existe. Les méthodes du modèle renvoient respectivement le produit identifié et la collection des catégories.')
    edit('c4-q030', prompt='index.php appelle controleurs/etudiant.php. Celui-ci demande les étudiants au modèle puis inclut la vue de liste. Quel composant appelle ici le modèle avant la vue ?')
    edit('c4-q032', prompt='Avant de dessiner les écrans et d’organiser les fichiers d’une application, quelle première étape permet d’identifier les fonctionnalités attendues ?')
    edit('c4-q033', prompt='Les cas d’utilisation sont définis. Quelle étape permet maintenant de déterminer les pages que l’utilisateur devra voir ?')
    edit('c4-q034', prompt='Les besoins et les écrans sont définis. Quel ordre est cohérent pour organiser les fichiers, créer le point d’entrée puis implémenter les traitements ?')
    edit('c4-q038', context='$fichier contient un chemin choisi dans l’application. Le test d’existence ne remplace pas le contrôle des chemins autorisés.')
    edit('c4-q039', prompt='Que réalise include($fichier) lorsqu’il charge un sous-contrôleur PHP existant ?',
         context='$fichier contient le chemin autorisé de ce sous-contrôleur.')
    edit('c4-q040', prompt='index.php est le point d’entrée qui charge la connexion puis choisit un sous-contrôleur. Quelle URL respecte ce passage par le point d’entrée ?')
    edit('c4-q042', prompt='Un catalogue est limité à la consultation des fiches de films, au filtrage par catégorie et à l’ajout de films. Quelles opérations respectent ce périmètre ?')
    edit('c4-q043', prompt='Un modèle propose les quatre méthodes ci-dessous. D’après leurs noms et paramètres, laquelle permet de lire un seul film identifié ?',
         context='Contrats proposés : obtenirLesFilms() lit tous les films ; obtenirUnFilm($id) lit un film ; obtenirFilmsParCategorie($idCategorie) filtre la collection ; ajouterFilm($donnees) insère un film.')
    edit('c4-q044', prompt='Quel appel du modèle sélectionne les films appartenant à la catégorie $idCategorie ?',
         context='obtenirUnFilm($id) recherche un film par son identifiant ; obtenirLesFilms() lit tout ; obtenirFilmsParCategorie($idCategorie) applique un filtre de catégorie ; ajouterFilm($donnees) ajoute un film.')
    edit('c4-q045', prompt='Une page est composée de header.php, menu.php, d’un contenu spécifique et de footer.php. Dans quelle sous-vue placer le titre commun « Catalogue de films » ?')
    edit('c4-q046', prompt='La vue parcourt ces données. Quel ensemble d’informations peut-elle afficher pour chaque ligne de la liste ?',
         code='$films = [\n    ["titre" => "Les Lumières", "realisateur" => "A. Martin", "annee" => 2024]\n];',
         explanation='Chaque entrée contient exactement les clés titre, realisateur et annee : la vue peut donc afficher ces trois informations.')
    option('c4-q046', 1, explanation='Aucune clé description n’est fournie dans les données affichées.')
    option('c4-q046', 2, explanation='Ces données constituent une liste synthétique, pas toutes les informations d’une fiche complète.')
    option('c4-q046', 3, explanation='Il n’y a aucune clé catégorie dans cet extrait ; des informations de film sont bien présentes.')
    edit('c4-q047', prompt='Un formulaire d’ajout doit proposer les catégories existantes en base. Comment fournir les choix à la liste déroulante dans une architecture MVC ?')
    edit('c4-q048', prompt='Dans une application MVC à point d’entrée index.php, à quel composant un formulaire doit-il transmettre sa soumission pour coordonner son traitement ?')
    edit('c4-q049', prompt='On distingue une action ajouter pour ouvrir un formulaire et une action enregistrer pour traiter sa soumission. Quel traitement correspond à chaque action ?')
    edit('c4-q050', prompt='Un catalogue permet liste, détail, filtrage par catégorie et ajout de films. Quels parcours de test vérifient réellement ces fonctionnalités ?')
    edit('c4-e002', context='$controleur est une chaîne déjà choisie parmi les noms de sous-contrôleurs autorisés, par exemple "etudiant". Écris une concaténation valable pour chacun de ces noms.')
    edit('c4-e004', context='La fonction du modèle obtenirLesEtudiants($pdo) existe et renvoie la liste. $pdo est une connexion déjà disponible ; la vue vues/liste_etudiants.php utilise la variable $etudiants.')
    edit('c4-e006', context='$etudiants est une collection déjà fournie à la vue, par exemple [["nom" => "Anna"], ["nom" => "Alex"]]. Chaque entrée possède la clé nom.')
    edit('c4-e009', context='$action est une chaîne déjà reçue. $laConnexion est un objet du modèle avec la méthode publique getLesCategories() renvoyant la collection ; vues/v_categories.php utilise $lesCategories.')
    edit('c4-e010', context='$_REQUEST["produit"] est présent. L’objet du modèle $laConnexion possède getLeProduit($id) et getLesCategories(). La vue vues/v_modif_produit.php utilise $leProduit et $lesCategories.')
    edit('c4-e011', context='$modele est déjà initialisé. Sa méthode publique obtenirLesFilms() renvoie la collection ; la vue vues/liste_films.php utilise $films.')
    edit('c4-e012', context='$modele est déjà initialisé et possède la méthode publique obtenirUnFilm($id). $id est un identifiant valide ; vues/details_film.php utilise $film.')
    edit('c4-e013', context='$modele est déjà initialisé et propose obtenirFilmsParCategorie($idCategorie). $idCategorie est valide ; vues/liste_films.php utilise la variable $films.')
    edit('c4-e014', context='$modele existe et propose ajouterFilm($donnees) puis obtenirLesFilms(). La vue à charger est vues/liste_films.php et elle parcourt $films. Les données d’entrée sont déjà validées.')

    # Les explications restent utilisables seules : éliminer les renvois à une capture
    # et décrire les responsabilités plutôt qu’un numéro de stratégie absent de l’écran.
    replacements = {
        'La capture du cours confirme une moyenne de 12 et le statut Admis.': 'La moyenne vaut 12 ; elle dépasse le seuil de 10.',
        'La capture du support confirme cet ordre.': 'Le constructeur précède le echo final, puis le destructeur est appelé en fin de script.',
        'Le cours utilise la session pour ne pas perdre les ajouts précédents.': 'La session permet de conserver les ajouts entre plusieurs requêtes de la même navigation.',
        'C’est la stratégie 1.': 'Ici, l’objet métier connaît et appelle lui-même son DAO.',
        'Ce serait la stratégie 2.': 'Dans cette autre organisation, le programme principal connaît le DAO et l’objet métier reste indépendant.',
        'Cela correspond à la stratégie 1.': 'Dans cette autre organisation, l’objet métier connaît son DAO et lui délègue sa sauvegarde.',
        'Le support demande de ne pas contourner les DAO.': 'L’accès aux données doit passer par les méthodes des DAO pour garder la persistance centralisée.',
        'L’énoncé précise le défaut à appliquer.': 'Le constructeur affecte explicitement le défaut dans la branche correspondant au nombre reçu.',
    }
    def clean(value):
        if isinstance(value, str):
            for before, after in replacements.items(): value = value.replace(before, after)
            return value
        if isinstance(value, list): return [clean(x) for x in value]
        if isinstance(value, dict): return {k: clean(v) for k, v in value.items()}
        return value
    for chapter in banks:
        banks[chapter] = [clean(q) for q in banks[chapter]]
