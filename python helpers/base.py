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