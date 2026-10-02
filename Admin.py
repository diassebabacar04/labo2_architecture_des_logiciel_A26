class Admin:

    def __init__(self, adminID, name, email, username, password):
        self.adminID = adminID
        self.name = name
        self.email = email
        self.username = username
        self.password = password

        self._tickets = []

    def assignTicket(self, ticket, user):
        ticket.assignTo(user)

        print(
            f"{self.name} a assigné le ticket "
            f"#{ticket.ticketID} à {user.name}"
        )

    def closeTicket(self, ticket):
        ticket.updateStatus("TERMINÉ")

        print(
            f"{self.name} a fermé le ticket "
            f"#{ticket.ticketID}"
        )

    def viewAllTickets(self):
        return list(self._tickets)

    def registerTicket(self, ticket):
        self._tickets.append(ticket)

    def __str__(self):
        return f"Admin({self.adminID}) - {self.name} <{self.email}>"