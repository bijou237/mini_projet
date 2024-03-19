class Personne:
    def __init__(self, nom, age):
        self._nom = nom
        self._age = age
    
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    
    def afficher_details(self):
        print("Nom:", self.nom)
        print("Age:", self.age)
