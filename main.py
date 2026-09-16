from User import User
from Admin import Admin
from Ticket import Ticket


def main():
    dev1 = User(1, "aminata diasse", "amina.diasse@uqac.ca", role="Développeuse")
    dev2 = User(2, "cheikh diasse", "cheikh.diasse@uqac.ca", role="Développeur")
    admin1 = Admin(1, "Babacar", "babacar.admin@uqac.ca")

    print(dev1)
    print(dev2)
    print(admin1)

    ticket1 = dev1.createTicket(
        Ticket(101, "Bug d'affichage", "Le bouton de connexion ne répond pas sur mobile.", priority="Haute")
    )
    admin1.registerTicket(ticket1)

    dev2.viewTicket(ticket1)

    print(vars(ticket1))

    admin1.assignTicket(ticket1, dev2)

    ticket1.addComment("Reproduction confirmée sur iOS Safari.")
    ticket1.updateStatus("VALIDATION")

    dev1.updateTicket(ticket1, priority="Critique")

    admin1.closeTicket(ticket1)

    print(vars(ticket1))

    for t in admin1.viewAllTickets():
        print(t)


if __name__ == "__main__":
    main()