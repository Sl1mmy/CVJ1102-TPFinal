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

        difference = abs(self.joueur1.impact - self.joueur2.impact)
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

            print(f"\nNombre de tours moyen: {np.average(turns)}")

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