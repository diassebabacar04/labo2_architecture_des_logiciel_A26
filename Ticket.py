from datetime import datetime
from contenu import Contenu


class Ticket:

    def __init__(self, ticket_id, title, priority="Normal"):
        self.ticketID = ticket_id
        self.title = title
        self.status = "OUVERT"
        self.priority = priority
        self.creationDate = datetime.now()
        self.updateDate = datetime.now()

        self.comments = []
        self.assignedTo = None

        # La description est composée de plusieurs contenus
        self.contenus = []

    def assignTo(self, user):
        self.assignedTo = user
        self.status = "ASSIGNÉ"
        self.updateDate = datetime.now()

    def updateStatus(self, status):
        self.status = status
        self.updateDate = datetime.now()

    def addComment(self, comment):
        self.comments.append(comment)
        self.updateDate = datetime.now()

    def addContenu(self, contenu):
        if isinstance(contenu, Contenu):
            self.contenus.append(contenu)
            self.updateDate = datetime.now()
        else:
            print("Erreur : le contenu doit être de type Contenu.")

    def __str__(self):
        return (
            f"Ticket #{self.ticketID} - {self.title} "
            f"[{self.status}] (priorité: {self.priority})"
        )