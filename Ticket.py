from datetime import datetime

class Ticket:
    def __init__(self, ticket_id, title, description, priority="Normal"):
        self.ticketID = ticket_id
        self.title = title
        self.description = description
        self.status = "OUVERT"  # le ticket commence son cycle de vie dans le statut ouvert une fois crée
        self.priority = priority
        self.creationDate = datetime.now()
        self.updateDate = datetime.now()

        self.comments = []  # liste vide qui va contenir les commentaires ajoutés au fil du temps
        self.assignedTo = None  # aucun développeur assigné au départ

    def assignTo(self, user):  # Relation "assigns" du diagramme : on garde une référence vers l'utilisateur assigné
        self.assignedTo = user
        self.status = "ASSIGNÉ"  # le ticket passe de statut ouvert a assigné
        self.updateDate = datetime.now()  # on trace le moment de l'assignation

    def updateStatus(self, status):  # Méthode générique pour changer le statut (OUVERT, ASSIGNÉ, VALIDATION, TERMINÉ)
        self.status = status  # statut est égale a statut actuelle
        self.updateDate = datetime.now()

    def addComment(self, comment):  # ajoute un commentaire a la liste
        self.comments.append(comment)

    def __str__(self):
        # Représentation lisible, appelée automatiquement par print(ticket)
        return f"Ticket #{self.ticketID} - {self.title} [{self.status}] (priorité: {self.priority})"