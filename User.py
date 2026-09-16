from datetime import datetime

class User:
    def __init__(self, user_id, name, email, role="Developpeur"):  # definissons du constructeur __init__
        self.user_id = user_id
        self.name = name
        self.email = email
        self.role = role

    def createTicket(self, ticket):
        print(f"{self.name} a crée le ticket : {ticket}")
        return ticket

    def viewTicket(self, ticket):
        print(f"{self.name} a consulté le ticket : {ticket}")

    def updateTicket(self, ticket, title=None, description=None, priority=None):
        if title is not None:
            ticket.title = title
        if description is not None:
            ticket.description = description
        if priority is not None:
            ticket.priority = priority

        ticket.updateDate = datetime.now()
        print(f"{self.name} a mis a jour le ticket :{ticket}")

    def __str__(self):
        return f"User({self.user_id}) - {self.name} <{self.email}> [{self.role}]"