# P3_02_Démarche
1. Explication de la démarche:
L'essentiel de la démarche est simple. D'abord, j'ai analysé le travail demandé en terme d'élements,
fonctionnalités, étapes et contraintes.
Ensuite, en adoptant la programmation orientée objet, j'ai défini une modélisation possible du jeu
et des personnages sans aller dans les détails.
En effet, j'ai divisé le jeu en module, chaque module comprend une ou plusieurs classes.
J'ai mis la structure en une classe dans un module à part, les personnages à savoir le héro,
l'enemie et les objets dans un module à part, avec une classe par élement et enfin la classe game dans un module à part.
En gros, la structure est dans un fichier à part d'abord pour la facilité des modifications et ensuite vu que c'est une contrainte.
Le héro, l'enemie et les objets sont des élements visibles de mon jeu et qui ont en plus des attributs similaires: dimensions, positions...
Leurs classes sont regroupées dans un fichier à part.
La classe game est une fichier à part. C'est là où on trouve la fonction main qui gère la logique du jeu, la gain,
la perte et l'interface utilisateur.
Une fois ce travail d'analyse préliminaire est fait, et avant de commencer à écrire du code, j'ai préparer mon environnement virtuel.
Dans cet environnement, j'ai installé pygame avec pip.
J'ai organisé les modules en cascade à savoir chaque module est appelé dans le suivant avec un fichier chapeau à la fin,
que j'ai appelé escape, qui lancera le jeu et assure la fermeture.
Maintenant, en allant plus dans les détails de code, le premier module "structure" contient la classe responsable de créer la labyrinthe.
J'ai choisi de modéliser la labyrinthe sous forme de matrice dont les élements gèrent la présence et/ou l'apparition des personnages.
Ce module sera importé dans le module "character" contenant les classes pour créer MacGyver, le gardien et les objets.
L'appartion aléatoire des objets est garantit par le module random avec sa fonction sample. Vu que c'est justele héro qui bouge,
les fonctions de mouvements sont définis dans la classe hero.
Ce module est importé dans le module suivant "game". C'est dans "game" que les instances des personnages sont crées
et c'est là où la fonction main appelle ces instances en fonction des phases du jeu.
La logique du gain ou perte est gérée par les fonctions win et loose
qui à leurs tours engagent un affichage écran à l'aide de la fonction "display_msg"
ainsi qu'une orientation dujeu vers quitter ou rejouer avec la fonction "replay_or_quit".
Le dernier module "escape" est un module chapeau qui appelle à son tour le module "game".

2. Les difficultés rencontreés:
a. Comemnt configurer mon editeur de texte à utiliser automatiquement python " au lieu de python 2
--> Pour cela, je me suis dcumenté sur le set up de sublime texte et comment créer un nouveau build system.
    En chercahant la réponse, j'ai découvert la notion de path: à partir de quelle adresse la machine exécute python,
    comment on peut le trouver et le changer. J'ai découvert aussi le module sys et son utilsation.
    
b. Comment utiliser un environnement virtuel
--> Pour cela, je me suis documenté sur l'utilité, l'installation, l'activation et la desactivation d'un environnement virtuel.
    
c. Comment oraganiser mon travail en module
-->J'ai decouvert comment python fonctionne pour importer mes module ainsi que les adresses dans lesquelles il recherche pour importer

d. Comment fonctionne pygame 
--> Lire le site officiel de pygame ainsi que des tutos decrivant l'utilisation des fonctions les plus utilisées du module





