from contenu import Contenu


class Image(Contenu):

    def __init__(self, chemin):
        self.chemin = chemin

    def charger(self):
        try:
            with open(self.chemin, "rb") as fichier:
                return fichier.read()

        except FileNotFoundError:
            print(f"Image introuvable : {self.chemin}")
            return None

    def __str__(self):
        return f"Image : {self.chemin}"