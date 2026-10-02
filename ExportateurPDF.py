from reportlab.pdfgen import canvas
from FichierTexte import FichierTexte
from Image import Image
from Video import Video


class ExportateurPDF:

    def exporter(self, ticket):
        nom_fichier = f"ticket_{ticket.ticketID}.pdf"

        pdf = canvas.Canvas(nom_fichier)

        y = 800

        # Informations du ticket
        pdf.drawString(50, y, f"Ticket #{ticket.ticketID}")
        y -= 25

        pdf.drawString(50, y, f"Titre : {ticket.title}")
        y -= 20

        pdf.drawString(50, y, f"Statut : {ticket.status}")
        y -= 20

        pdf.drawString(50, y, f"Priorité : {ticket.priority}")
        y -= 30

        pdf.drawString(50, y, "Description :")
        y -= 25

        # Parcours des contenus
        for contenu in ticket.contenus:

            if isinstance(contenu, FichierTexte):
                pdf.drawString(70, y, f"Texte : {contenu.texte}")
                y -= 25

            elif isinstance(contenu, Image):
                pdf.drawString(70, y, f"Image : {contenu.chemin}")
                y -= 20

                try:
                    pdf.drawImage(
                        contenu.chemin,
                        70,
                        y - 150,
                        width=200,
                        height=150,
                        preserveAspectRatio=True
                    )

                    y -= 170

                except Exception:
                    pdf.drawString(
                        70,
                        y,
                        "Impossible de charger l'image."
                    )
                    y -= 25

            elif isinstance(contenu, Video):
                pdf.drawString(
                    70,
                    y,
                    f"Vidéo : {contenu.chemin}"
                )
                y -= 25

        pdf.save()

        print(f"PDF créé : {nom_fichier}")