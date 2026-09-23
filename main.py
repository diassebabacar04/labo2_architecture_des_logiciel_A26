from User import User
from Admin import Admin
from Ticket import Ticket


tickets = []
utilisateurs = []
admins = []


def se_connecter_user():
    nom = input("Nom : ")
    email = input("Email : ")
    role = input("Rôle (laisser vide pour 'Développeur') : ") or "Développeur"
    user = User(len(utilisateurs) + 1, nom, email, role=role)
    utilisateurs.append(user)
    print(f"Connecté en tant que : {user}")
    menu_user(user)


def se_connecter_admin():
    nom = input("Nom : ")
    email = input("Email : ")
    admin = Admin(len(admins) + 1, nom, email)
    admins.append(admin)
    print(f"Connecté en tant que : {admin}")
    menu_admin(admin)


def menu_user(user):
    while True:
        print(f"\n=== Menu User : {user.name} ===")
        print("1. Créer un ticket")
        print("2. Consulter un ticket")
        print("3. Mettre à jour un ticket")
        print("4. Retour")
        choix = input("Choix : ")

        if choix == "1":
            titre = input("Titre : ")
            description = input("Description : ")
            t = user.createTicket(Ticket(len(tickets) + 101, titre, description))
            tickets.append(t)
        elif choix == "2":
            if not tickets:
                print("Aucun ticket.")
                continue
            for i, t in enumerate(tickets):
                print(f"{i} - {t}")
            i = int(input("Numéro du ticket : "))
            user.viewTicket(tickets[i])
        elif choix == "3":
            if not tickets:
                print("Aucun ticket.")
                continue
            for i, t in enumerate(tickets):
                print(f"{i} - {t}")
            i = int(input("Numéro du ticket : "))
            priorite = input("Nouvelle priorité : ")
            user.updateTicket(tickets[i], priority=priorite)
        elif choix == "4":
            break
        else:
            print("Choix invalide.")


def menu_admin(admin):
    while True:
        print(f"\n=== Menu Admin : {admin.name} ===")
        print("1. Assigner un ticket")
        print("2. Fermer un ticket")
        print("3. Afficher tous les tickets")
        print("4. Retour")
        choix = input("Choix : ")

        if choix == "1":
            if not tickets:
                print("Aucun ticket.")
                continue
            if not utilisateurs:
                print("Aucun utilisateur enregistré, connecte-toi d'abord en tant que User au moins une fois.")
                continue
            for i, t in enumerate(tickets):
                print(f"{i} - {t}")
            i = int(input("Numéro du ticket : "))
            for j, u in enumerate(utilisateurs):
                print(f"{j} - {u}")
            j = int(input("Numéro de l'utilisateur à assigner : "))
            admin.assignTicket(tickets[i], utilisateurs[j])
        elif choix == "2":
            if not tickets:
                print("Aucun ticket.")
                continue
            for i, t in enumerate(tickets):
                print(f"{i} - {t}")
            i = int(input("Numéro du ticket : "))
            admin.closeTicket(tickets[i])
        elif choix == "3":
            for t in tickets:
                print(t)
        elif choix == "4":
            break
        else:
            print("Choix invalide.")


def main():
    while True:
        print("\n=== Menu principal ===")
        print("1. Se connecter comme User")
        print("2. Se connecter comme Admin")
        print("3. Quitter")
        choix = input("Choix : ")

        if choix == "1":
            se_connecter_user()
        elif choix == "2":
            se_connecter_admin()
        elif choix == "3":
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
