from numpy import average
from fight import Fight

def main():
    while True:
        rerun = 'y'
        
        stats1 = input("\nJOUEUR 1: agilite et vigueur: ").split()
        stats2 = input("\nJOUEUR 2: agilite et vigueur: ").split()

        stats1 = tuple(map(float, stats1))
        stats2 = tuple(map(float, stats2))

        while rerun.lower() == 'y':
            nb_iterations = 1000
            max_single_turns = 0

            best_joueur1_random_values = []
            best_joueur2_random_values = []

            turns = []
            for iteration in range(nb_iterations):
                new_fight = Fight(stats1, stats2)
                outcome, n_turns, j1_random_vals, j2_random_vals = new_fight.run()
                turns.append(n_turns)
                print(f"Partie {iteration}: {outcome} a gagné en {n_turns}")

                if n_turns > max_single_turns:
                    max_single_turns = n_turns
                    best_joueur1_random_values = j1_random_vals
                    best_joueur2_random_values = j2_random_vals

            print(f"\nNombre de tours moyen: {average(turns)}")

            print(f"\nNombre de tours du meilleur combat: {max_single_turns}")
            print("\nValeurs aléatoires pour le meilleur combat (Joueur 1):")
            print(best_joueur1_random_values)
            print("\nValeurs aléatoires pour le meilleur combat (Joueur 2):")
            print(best_joueur2_random_values)
            
            # Ask if the user wants to rerun with the same stats
            rerun = input("\nVoulez-vous rejouer avec les mêmes stats? (y/n): ")

        # Ask if the user wants to start a new fight with different stats
        new_fight = input("\nVoulez-vous lancer un nouveau combat avec d'autres stats? (y/n): ")
        if new_fight.lower() != 'y':
            print("Fin du programme.")
            break


if __name__ == "__main__":
    quit(main())