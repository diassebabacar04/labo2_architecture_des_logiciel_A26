from datetime import datetime

class Admin:
    def __init__(self, adminID, name, email):#definissions du constructeur __init__:
        self.adminID=adminID
        self.name=name
        self.email=email
        self._tickets = [] #liste vide qui va contenir les tickets gérés par cet admin

    def assignTicket(self, ticket, user):
        ticket.assignTo(user)
        print(f"{self.name} a assigné le ticket #{ticket.ticketID} a {user.name}")
    
    def closeTicket(self, ticket):
        ticket.updateStatus("Terminé")
        print(f"{self.name} a fermé le ticket #{ticket.ticketID}")

    def viewAllTickets(self):
        return list(self._tickets)

    def registerTicket(self, ticket):
        self._tickets.append(ticket)

    def __str__(self):#Représentation lisible, appelée automatiquement par print(admin)
        return f"Admin({self.adminID}) - {self.name} <{self.email}>"   