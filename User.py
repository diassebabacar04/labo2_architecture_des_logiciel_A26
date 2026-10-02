from datetime import datetime


class User:

    def __init__(self, user_id, name, email, username, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.username = username
        self.password = password

    def createTicket(self, ticket):
        print(f"{self.name} a créé le ticket : {ticket}")
        return ticket

    def viewTicket(self, ticket):
        print(f"{self.name} a consulté le ticket : {ticket}")

        print("\n--- Description ---")

        if not ticket.contenus:
            print("Aucun contenu.")
        else:
            for contenu in ticket.contenus:
                print(contenu)

    def updateTicket(self, ticket, title=None, priority=None):
        if title is not None:
            ticket.title = title

        if priority is not None:
            ticket.priority = priority

        ticket.updateDate = datetime.now()

        print(f"{self.name} a mis à jour le ticket : {ticket}")

    def __str__(self):
        return f"User({self.user_id}) - {self.name} <{self.email}>"