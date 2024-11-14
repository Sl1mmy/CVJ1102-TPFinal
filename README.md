
# CVJ1102-TPFinal

Simulation de combat avec Excel pour le cours CVJ1102 - Mathématique pour le jeu

## Excel

**Feuille Simulation:**
roule une seule simulation avec les valeurs initiales de Vigueur et d'Agilité inscrit par l'utilisateur.

 **Feuille Preuve24Tours:**
preuve d'un résultat possible de 24 tours dans une seule simulation. 


## Helper Files

### combat_sim.py:
Roule x simulations utilisant les variables `agilite` et `vigueur`.

Exemple d'utilisation
```python
JOUEUR 1: agilite et vigueur: 50 40 #input 
JOUEUR 2: agilite et vigueur: 50 40 #input

#simulations:
Partie 0: J1 a gagné en 5 
Partie 1: J1 a gagné en 3
...
Partie 999: J1 a gagné en 3

#résultats:
Nombre de tours moyen: 3.892

Nombre de tours du meilleur combat: 11

Valeurs aléatoires pour le meilleur combat (Joueur 1):
[53.44782694681469, 14.200016000390708, 48.26826275697758, 19.51275544506552, 28.301464861506673, 21.183325873610674, 35.69505775217726, 86.168300460618456, 25.596448196274054, 44.90202218085367, 38.44625602164894]

Valeurs aléatoires pour le meilleur combat (Joueur 2):
[28.16619025363103, 82.60481227894373, 27.245603084481054, 21.572620532990992, 37.08896735340617, 29.964655589659497, 48.47742837416905, 0.6749833051113756, 3.97556201461488, 46.0077420597136, 15.448985822904753]

Voulez-vous rejouer avec les mêmes stats? (y/n): n #possibilité de relancer une simulation
Voulez-vous lancer un nouveau combat avec d'autres stats? (y/n): n #possibilité de changer les valeurs initiales
Fin du programme.
```

### range_solver.py:

recherches les meilleures valeurs pour `agilite` et `vigueur`.

exemple de résultat avec la range de toutes les valeurs possibles et une incrémentation de 1:
```python
Meilleure combinaison pour le nombre moyen de tours le plus élevé :
Joueur 1 : Agilité 11, Vigueur 79
Joueur 2 : Agilité 12, Vigueur 78
Nombre moyen de tours le plus élevé : 4.82

Nombre de tours le plus élevé dans une seule simulation : 17
Joueur 1 : Agilité 18, Vigueur 72
Joueur 2 : Agilité 25, Vigueur 65

Valeurs aléatoires pour le meilleur combat (Joueur 1) :
[23.834830832699602, 6.159679179227389, 51.20645329650819, 44.12489735528163, 38.774614094311225, 78.83357910069499, 49.93176387193671, 38.29576817931733, 21.017639130394862, 27.845000289885874, 62.99472906625009, 59.52341420403182, 27.483943052789755, 1.94222072857292, 38.08171114446901, 11.333751320537992, -12.510248707622118]

Valeurs aléatoires pour le meilleur combat (Joueur 2) :
[33.2719521379445, 32.256218128980315, 78.93621198256372, 65.41027576607189, 48.17002015398245, 27.61781241943787, 54.010477512733175, -11.398545219398585, 58.99428263349577, 27.929778779699088, 47.94844542888073, 57.707659941691546, 67.39702064032693, -4.899736062774828, 
-4.4185148635252105, 30.77252750075381, 58.49392518218258]
```

