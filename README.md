Visualisation de polynômes en Python
🎯 Objectif du projet

Ce programme permet de tracer un ou plusieurs polynômes du second degré sur un même graphique, à partir des coefficients saisis par l’utilisateur.

L’objectif est de faire le lien entre :

les mathématiques (polynômes)

la programmation en Python

la visualisation graphique avec matplotlib

🧠 Principe mathématique

Un polynôme du second degré est défini par trois coefficients :

f(x) = ax² + bx + c


Exemple :

f(x) = 2x² + 3x - 5
→ coefficients : [2, 3, -5]


Le programme utilise la fonction numpy.polyval pour calculer les valeurs du polynôme sur l’intervalle choisi.

🖥️ Fonctionnement du programme

L’utilisateur choisit le nombre de polynômes à tracer (1 à 3).

Pour chaque polynôme, il entre les coefficients :

coefficient de x²

coefficient de x

constante

L’utilisateur définit :

l’intervalle [xmin, xmax]

le pas de discrétisation

Le programme :

calcule les valeurs y associées

trace tous les polynômes sur un même graphique

affiche une légende avec les polynômes correctement formatés

📌 Exemple d’utilisation

Entrée utilisateur :

Polynôme : 2x² + 3x − 5

Intervalle : [-10 ; 10]

Pas : 0.1

Résultat :

Affichage du graphique avec le polynôme tracé et légendé, par exemple : 2x² + 3x - 5

🛠️ Bibliothèques utilisées

numpy

matplotlib

📚 Niveau et contexte

Projet réalisé dans un objectif pédagogique (niveau Licence 1), sans utilisation de notions avancées comme la POO ou les polynômes de degré quelconque.

🚀 Améliorations possibles

Gérer des polynômes de degré variable

Ajouter l’affichage des racines ou dérivées

Ajouter plus de styles et couleurs pour les tracés

Optimiser la saisie pour un plus grand nombre de polynômes