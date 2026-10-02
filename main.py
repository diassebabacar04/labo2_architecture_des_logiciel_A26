from User import User
from Admin import Admin
from Ticket import Ticket
from FichierTexte import FichierTexte
from Image import Image
from Video import Video
from ExportateurPDF import ExportateurPDF


tickets = []


# ==================================================
# COMPTES DE TEST
# ==================================================

utilisateurs = [
    User(
        1,
        "Ibrahima",
        "ibrahima@test.com",
        "ibrahima",
        "1234"
    ),

    User(
        2,
        "Babacar",
        "babacar@test.com",
        "babacar",
        "1234"
    ),

    User(
        3,
        "Ahmed Aziz",
        "ahmed.aziz@test.com",
        "ahmed",
        "1234"
    ),

    User(
        4,
        "Mohammad Amine",
        "mohammad.amine@test.com",
        "mohammad",
        "1234"
    )
]


admins = [
    Admin(
        1,
        "Rahmatoullah",
        "rahmatoullah@test.com",
        "rahmatoullah",
        "admin123"
    ),

    Admin(
        2,
        "Abdalla",
        "abdalla@test.com",
        "abdalla",
        "admin123"
    )
]


# ==================================================
# CONNEXION
# ==================================================

def se_connecter():

    print("\n=== Connexion ===")

    username = input("Nom d'utilisateur : ")
    password = input("Mot de passe : ")

    # Recherche parmi les Users
    for user in utilisateurs:

        if user.username == username and user.password == password:

            print(f"\nConnexion réussie.")
            print(f"Bienvenue {user.name} !")

            menu_user(user)
            return

    # Recherche parmi les Admins
    for admin in admins:

        if admin.username == username and admin.password == password:

            print(f"\nConnexion réussie.")
            print(f"Bienvenue {admin.name} !")

            menu_admin(admin)
            return

    print("\nNom d'utilisateur ou mot de passe incorrect.")


# ==================================================
# MENU USER
# ==================================================

def menu_user(user):

    while True:

        print(f"\n=== Menu User : {user.name} ===")
        print("1. Créer un ticket")
        print("2. Consulter un ticket")
        print("3. Mettre à jour un ticket")
        print("4. Exporter un ticket en PDF")
        print("5. Déconnexion")

        choix = input("Choix : ")

        # ------------------------------------------
        # CRÉER UN TICKET
        # ------------------------------------------

        if choix == "1":

            titre = input("Titre : ")

            priorite = input(
                "Priorité (laisser vide pour 'Normal') : "
            ) or "Normal"

            ticket = Ticket(
                len(tickets) + 101,
                titre,
                priority=priorite
            )

            while True:

                print("\n=== Description du ticket ===")
                print("1. Ajouter du texte")
                print("2. Ajouter une image")
                print("3. Ajouter une vidéo")
                print("4. Terminer")

                choix_contenu = input("Choix : ")

                if choix_contenu == "1":

                    texte = input("Texte : ")

                    contenu = FichierTexte(texte)

                    ticket.addContenu(contenu)

                    print("Texte ajouté.")

                elif choix_contenu == "2":

                    chemin = input("Chemin de l'image : ")

                    contenu = Image(chemin)

                    ticket.addContenu(contenu)

                    print("Image ajoutée.")

                elif choix_contenu == "3":

                    chemin = input("Chemin de la vidéo : ")

                    contenu = Video(chemin)

                    ticket.addContenu(contenu)

                    print("Vidéo ajoutée.")

                elif choix_contenu == "4":
                    break

                else:
                    print("Choix invalide.")

            ticket = user.createTicket(ticket)

            tickets.append(ticket)

            # Les admins peuvent maintenant gérer ce ticket
            for admin in admins:
                admin.registerTicket(ticket)

        # ------------------------------------------
        # CONSULTER UN TICKET
        # ------------------------------------------

        elif choix == "2":

            if not tickets:
                print("Aucun ticket.")
                continue

            for i, ticket in enumerate(tickets):
                print(f"{i} - {ticket}")

            try:

                i = int(input("Numéro du ticket : "))

                user.viewTicket(tickets[i])

            except (ValueError, IndexError):
                print("Numéro de ticket invalide.")

        # ------------------------------------------
        # METTRE À JOUR UN TICKET
        # ------------------------------------------

        elif choix == "3":

            if not tickets:
                print("Aucun ticket.")
                continue

            for i, ticket in enumerate(tickets):
                print(f"{i} - {ticket}")

            try:

                i = int(input("Numéro du ticket : "))

                nouveau_titre = input(
                    "Nouveau titre "
                    "(laisser vide pour ne pas modifier) : "
                )

                nouvelle_priorite = input(
                    "Nouvelle priorité "
                    "(laisser vide pour ne pas modifier) : "
                )

                user.updateTicket(
                    tickets[i],
                    title=nouveau_titre or None,
                    priority=nouvelle_priorite or None
                )

            except (ValueError, IndexError):
                print("Numéro de ticket invalide.")

        # ------------------------------------------
        # EXPORTER EN PDF
        # ------------------------------------------

        elif choix == "4":

            if not tickets:
                print("Aucun ticket.")
                continue

            for i, ticket in enumerate(tickets):
                print(f"{i} - {ticket}")

            try:

                i = int(
                    input("Numéro du ticket à exporter : ")
                )

                exportateur = ExportateurPDF()

                exportateur.exporter(tickets[i])

            except (ValueError, IndexError):
                print("Numéro de ticket invalide.")

        # ------------------------------------------
        # DÉCONNEXION
        # ------------------------------------------

        elif choix == "5":

            print(f"{user.name} est déconnecté.")
            break

        else:
            print("Choix invalide.")


# ==================================================
# MENU ADMIN
# ==================================================

def menu_admin(admin):

    while True:

        print(f"\n=== Menu Admin : {admin.name} ===")
        print("1. Assigner un ticket")
        print("2. Fermer un ticket")
        print("3. Afficher tous les tickets")
        print("4. Déconnexion")

        choix = input("Choix : ")

        # ------------------------------------------
        # ASSIGNER UN TICKET
        # ------------------------------------------

        if choix == "1":

            if not tickets:
                print("Aucun ticket.")
                continue

            for i, ticket in enumerate(tickets):
                print(f"{i} - {ticket}")

            try:

                i = int(input("Numéro du ticket : "))

                print("\n=== Utilisateurs disponibles ===")

                for j, user in enumerate(utilisateurs):
                    print(f"{j} - {user.name}")

                j = int(
                    input(
                        "Numéro de l'utilisateur à assigner : "
                    )
                )

                admin.assignTicket(
                    tickets[i],
                    utilisateurs[j]
                )

            except (ValueError, IndexError):
                print("Choix invalide.")

        # ------------------------------------------
        # FERMER UN TICKET
        # ------------------------------------------

        elif choix == "2":

            if not tickets:
                print("Aucun ticket.")
                continue

            for i, ticket in enumerate(tickets):
                print(f"{i} - {ticket}")

            try:

                i = int(input("Numéro du ticket : "))

                admin.closeTicket(tickets[i])

            except (ValueError, IndexError):
                print("Numéro de ticket invalide.")

        # ------------------------------------------
        # AFFICHER TOUS LES TICKETS
        # ------------------------------------------

        elif choix == "3":

            if not tickets:
                print("Aucun ticket.")

            else:

                for ticket in tickets:
                    print(ticket)

                    if ticket.assignedTo is not None:
                        print(
                            f"   Assigné à : "
                            f"{ticket.assignedTo.name}"
                        )
                    else:
                        print("   Non assigné")

        # ------------------------------------------
        # DÉCONNEXION
        # ------------------------------------------

        elif choix == "4":

            print(f"{admin.name} est déconnecté.")
            break

        else:
            print("Choix invalide.")


# ==================================================
# PROGRAMME PRINCIPAL
# ==================================================

def main():

    while True:

        print("\n==============================")
        print("   GESTIONNAIRE DE TICKETS")
        print("==============================")

        print("1. Se connecter")
        print("2. Quitter")

        choix = input("Choix : ")

        if choix == "1":
            se_connecter()

        elif choix == "2":
            print("Fin du programme.")
            break

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()