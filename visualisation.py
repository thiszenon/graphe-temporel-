
import xlrd
from collections import defaultdict

#Fonctions qui recherche les images par date
def trouver_images(session, date_recherche):

    workbook = xlrd.open_workbook(session)
    sheet = workbook.sheet_by_index(0)

    images_trouvees = []


    dates_dict = defaultdict(list)

    for ligne_index in range(1,sheet.nrows):
        nom_image = sheet.cell_value(ligne_index,0)
        date = sheet.cell_value(ligne_index,1)
        
        if date == date_recherche:
            images_trouvees.append(nom_image)
    return images_trouvees

## entreé de l'utilisateur
print("Format : MM/AAAA")
date_recherche = input("Entrer la date à rechercher : ")



fichier = "session_images.xls"
resultats = trouver_images(fichier,date_recherche)

if resultats:
    print(f"\n{len(resultats)} images trouvées pour la date {date_recherche}")
    for img in resultats:
        print(f" - {img}")
else:
    print(f"\nAucune image trouvée pour la date {date_recherche}")





