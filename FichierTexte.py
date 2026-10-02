from contenu import Contenu


class FichierTexte(Contenu):

    def __init__(self, texte):
        self.texte = texte

    def charger(self):
        return self.texte

    def __str__(self):
        return f"Texte : {self.texte}"