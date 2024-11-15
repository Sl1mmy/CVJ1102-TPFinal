import numpy as np

class Joueur:
    def __init__(self, agilite, vigueur):
        self.__agilite = agilite
        self.__vigueur = vigueur
        self.__impact = 0
        self.agilite_random_values = []  # Store random values for each turn

    @property
    def agilite(self):
        return self.__agilite
    
    @agilite.setter
    def agilite(self, agilite):
        self.__agilite = agilite

    @property
    def vigueur(self):
        return self.__vigueur

    @vigueur.setter
    def vigueur(self, vigueur):
        self.__vigueur = vigueur

    @property
    def impact(self):
        return self.__impact
    
    @property
    def is_alive(self):
        return self.__vigueur > 0

    def calculate_impact(self):
        self.__impact = (0.7 * self.__vigueur) + (0.4 * self.__agilite)
        return self.__impact
    
    def calculate_agilite(self, moyenne=40, ecart_type=25):
        random_value = np.random.normal(moyenne, ecart_type, 1)[0]
        self.agilite_random_values.append(random_value)
        self.__agilite = (self.__agilite + random_value) / 2
        

class Fight:
    def __init__(self, stats1, stats2, moyenne=40, ecart_type=25):
        self.joueur1 = Joueur(*stats1)
        self.joueur2 = Joueur(*stats2)
        self.moyenne = moyenne
        self.ecart_type = ecart_type

        self.n_turns = 0

    def run(self):
        while(self.joueur1.is_alive and self.joueur2.is_alive):
            self.next()
            self.n_turns += 1
        
        if self.joueur1.is_alive:
            outcome = "J1"
        else:
            outcome = "J2"

        return outcome, self.n_turns, self.joueur1.agilite_random_values, self.joueur2.agilite_random_values

    def next(self):
        self.calculate_agilite(self.moyenne, self.ecart_type)
        self.calculate_impact()

        difference = abs(self.joueur1.impact - self.joueur2.impact) * 0.2
        if(self.joueur1.impact > self.joueur2.impact):
            self.joueur1.vigueur += difference
            self.joueur2.vigueur -= difference
        elif(self.joueur2.impact > self.joueur1.impact):
            self.joueur1.vigueur -= difference
            self.joueur2.vigueur += difference

    def calculate_agilite(self, moyenne=40, ecart_type=25):
        self.joueur1.calculate_agilite(moyenne, ecart_type)
        self.joueur2.calculate_agilite(moyenne, ecart_type)
    
    def calculate_impact(self):
        self.joueur1.calculate_impact()
        self.joueur2.calculate_impact()

    
def main():
    nb_iterations = 100
    max_avg_turns = 0

    max_single_turns = 0
    max_single_turns_stats = (None, None)
    best_joueur1_random_values = []
    best_joueur2_random_values = []

    best_stats = (None, None)

    # New variable to track the first iteration where no turns are less than 13
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
                if iteration_all_turns_min_13 is None and all(t >= 15 for t in turns):
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