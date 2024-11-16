import numpy as np
from base import Fight
    
def main():
    nb_iterations = 100
    max_avg_turns = 0

    max_single_turns = 0
    max_single_turns_stats = (None, None)
    best_joueur1_random_values = []
    best_joueur2_random_values = []

    best_stats = (None, None)

    iteration_all_turns_min_13 = None

    # agilite_values range setup
    #agilite_values = np.arange(10, 91, 0.1)
    agilite_values = np.arange(10, 20.5, 0.01)   # Set Range

    for agilite1 in agilite_values:
        vigueur1 = 90 - agilite1
        for agilite2 in agilite_values:
            vigueur2 = 90 - agilite2

            stats1 = (agilite1, vigueur1)
            stats2 = (agilite2, vigueur2)
            
            turns = []
            for _ in range(nb_iterations):
                new_fight = Fight(stats1, stats2)
                _, n_turns, j1_random_vals, j2_random_vals = new_fight.run()
                turns.append(n_turns)
                
                # Update the maximum single turns if necessary
                if n_turns > max_single_turns:
                    max_single_turns = n_turns
                    max_single_turns_stats = (stats1, stats2)
                    best_joueur1_random_values = j1_random_vals
                    best_joueur2_random_values = j2_random_vals

                # Check if all turns in this iteration are >= 13
                if iteration_all_turns_min_13 is None and all(t >= 13 for t in turns):
                    iteration_all_turns_min_13 = (stats1, stats2)
                    #print(f"First iteration where all turns are >= 13 found: {iteration_all_turns_min_13}")

            avg_turns = np.average(turns)
            print(f"Stats J1: {stats1}, Stats J2: {stats2} -> Avg Turns: {avg_turns}")

            # Update if this combination has the highest average turns
            if avg_turns > max_avg_turns:
                max_avg_turns = avg_turns
                best_stats = (stats1, stats2)
    

    print(f"\nMeilleure combinaison pour le nombre moyen de tours le plus élevé :")
    print(f"Joueur 1 : Agilité {best_stats[0][0]}, Vigueur {best_stats[0][1]}")
    print(f"Joueur 2 : Agilité {best_stats[1][0]}, Vigueur {best_stats[1][1]}")
    print(f"Nombre moyen de tours le plus élevé : {max_avg_turns}")

    print(f"\nNombre de tours le plus élevé dans une seule simulation : {max_single_turns}")
    print(f"Joueur 1 : Agilité {max_single_turns_stats[0][0]}, Vigueur {max_single_turns_stats[0][1]}")
    print(f"Joueur 2 : Agilité {max_single_turns_stats[1][0]}, Vigueur {max_single_turns_stats[1][1]}")
    
    print("\nValeurs aléatoires pour le meilleur combat (Joueur 1) :")
    print(best_joueur1_random_values)
    print("\nValeurs aléatoires pour le meilleur combat (Joueur 2) :")
    print(best_joueur2_random_values)

    if iteration_all_turns_min_13:
        print(f"\nPremière itération où tous les tours sont >= 13 :")
        print(f"Joueur 1 : Agilité {iteration_all_turns_min_13[0][0]}, Vigueur {iteration_all_turns_min_13[0][1]}")
        print(f"Joueur 2 : Agilité {iteration_all_turns_min_13[1][0]}, Vigueur {iteration_all_turns_min_13[1][1]}")
    else:
        print("\nAucune itération n'a eu tous les tours >= 13.")

if __name__ == "__main__":
    quit(main())