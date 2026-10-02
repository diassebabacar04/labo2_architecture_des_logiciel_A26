# Laboratoire 2 – Architecture des logiciels

Ce projet est une application Python permettant de gérer des tickets.

Un ticket peut contenir plusieurs types de contenu dans sa description :
- Texte
- Image
- Vidéo

Le système possède deux types de comptes :
- **User** : création, consultation et modification des tickets.
- **Admin** : assignation et fermeture des tickets.

Les tickets peuvent également être exportés au format PDF.

---

## 1. Prérequis

Le programme nécessite Python.

Vérifier que Python est installé :

```bash
python --version
```

Le projet utilise également la bibliothèque `reportlab` pour générer les fichiers PDF.

Installation :

```bash
python -m pip install reportlab
```

---

## 2. Lancer le programme

Ouvrir un terminal dans le dossier du projet puis exécuter :

```bash
python main.py
```

Le menu principal apparaît :

```text
==============================
   GESTIONNAIRE DE TICKETS
==============================

1. Se connecter
2. Quitter
```

---

## 3. Comptes de test

Six comptes sont déjà créés dans le programme.

### Comptes User

| Nom | Nom d'utilisateur | Mot de passe |
|---|---|---|
| Ibrahima | ibrahima | 1234 |
| Babacar | babacar | 1234 |
| Ahmed Aziz | ahmed | 1234 |
| Mohammad Amine | mohammad | 1234 |

### Comptes Admin

| Nom | Nom d'utilisateur | Mot de passe |
|---|---|---|
| Rahmatoullah | rahmatoullah | admin123 |
| Abdalla | abdalla | admin123 |

Le rôle n'est pas choisi pendant la connexion. Il est déjà associé au compte.

---

## 4. Tester la connexion User

Dans le menu principal :

```text
Choix : 1
```

Exemple de connexion :

```text
Nom d'utilisateur : ibrahima
Mot de passe : 1234
```

Le menu User apparaît :

```text
=== Menu User : Ibrahima ===

1. Créer un ticket
2. Consulter un ticket
3. Mettre à jour un ticket
4. Exporter un ticket en PDF
5. Déconnexion
```

---

## 5. Créer un ticket

Choisir :

```text
1. Créer un ticket
```

Exemple :

```text
Titre : Problème de connexion
Priorité : Haute
```

Le programme demande ensuite de construire la description :

```text
=== Description du ticket ===

1. Ajouter du texte
2. Ajouter une image
3. Ajouter une vidéo
4. Terminer
```

### Ajouter du texte

Choisir :

```text
1
```

Puis entrer par exemple :

```text
Impossible de se connecter à l'application.
```

Un objet `FichierTexte` est alors ajouté au ticket.

### Ajouter une image

Choisir :

```text
2
```

Puis entrer le chemin d'une image présente sur l'ordinateur.

Exemple :

```text
C:\Users\Utilisateur\Pictures\erreur.png
```

Un objet `Image` est ajouté au ticket.

### Ajouter une vidéo

Choisir :

```text
3
```

Puis entrer le chemin de la vidéo.

Exemple :

```text
C:\Users\Utilisateur\Videos\erreur.mp4
```

Un objet `Video` est ajouté au ticket.

Il est possible d'ajouter plusieurs contenus au même ticket.

Lorsque la description est terminée :

```text
4. Terminer
```

---

## 6. Consulter un ticket

Dans le menu User :

```text
2. Consulter un ticket
```

Les tickets disponibles sont affichés.

Exemple :

```text
0 - Ticket #101 - Problème de connexion [OUVERT] (priorité: Haute)
```

Choisir :

```text
0
```

Le programme affiche le ticket ainsi que les différents contenus de sa description.

---

## 7. Modifier un ticket

Choisir :

```text
3. Mettre à jour un ticket
```

Sélectionner ensuite le ticket.

Il est possible de modifier :
- le titre ;
- la priorité.

Laisser une valeur vide permet de conserver sa valeur actuelle.

---

## 8. Exporter un ticket en PDF

Choisir :

```text
4. Exporter un ticket en PDF
```

Puis sélectionner le ticket.

Le programme utilise la classe :

```text
ExportateurPDF
```

Un fichier est créé sous la forme :

```text
ticket_101.pdf
```

Le PDF contient les informations du ticket et sa description.

Pour les images, le programme tente également de les intégrer dans le document.

---

## 9. Tester le rôle Admin

Se déconnecter du compte User puis choisir de nouveau :

```text
1. Se connecter
```

Exemple :

```text
Nom d'utilisateur : rahmatoullah
Mot de passe : admin123
```

Le menu Admin apparaît :

```text
=== Menu Admin : Rahmatoullah ===

1. Assigner un ticket
2. Fermer un ticket
3. Afficher tous les tickets
4. Déconnexion
```

---

## 10. Assigner un ticket

Choisir :

```text
1. Assigner un ticket
```

Sélectionner d'abord le ticket.

Le programme affiche ensuite les quatre utilisateurs disponibles :

```text
0 - Ibrahima
1 - Babacar
2 - Ahmed Aziz
3 - Mohammad Amine
```

Choisir l'utilisateur auquel le ticket doit être assigné.

Le statut du ticket devient :

```text
ASSIGNÉ
```

---

## 11. Fermer un ticket

Dans le menu Admin :

```text
2. Fermer un ticket
```

Sélectionner le ticket.

Son statut devient :

```text
TERMINÉ
```

---

## 12. Scénario de test complet

Pour vérifier rapidement le fonctionnement du projet :

1. Lancer `python main.py`.
2. Se connecter avec `ibrahima / 1234`.
3. Créer un ticket.
4. Ajouter un texte à la description.
5. Ajouter une image.
6. Terminer la création du ticket.
7. Consulter le ticket.
8. Exporter le ticket en PDF.
9. Se déconnecter.
10. Se connecter avec `rahmatoullah / admin123`.
11. Afficher les tickets.
12. Assigner le ticket à Babacar.
13. Vérifier que son statut est `ASSIGNÉ`.
14. Fermer le ticket.
15. Vérifier que son statut est `TERMINÉ`.

---

## Structure principale

```text
main.py
User.py
Admin.py
Ticket.py
contenu.py
FichierTexte.py
Image.py
Video.py
ExportateurPDF.py
```

`Contenu` est une classe abstraite. `FichierTexte`, `Image` et `Video` héritent de cette classe et implémentent leur propre méthode `charger()`.

Un `Ticket` peut contenir plusieurs objets `Contenu`, ce qui permet d'ajouter de nouveaux types de contenu sans devoir refaire toute la classe `Ticket`.
