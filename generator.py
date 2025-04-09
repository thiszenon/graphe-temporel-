
import random
import xlwt

from datetime import datetime

#creer un nouveau fichier excel

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Images_data")

#En-têtes
sheet.write(0,0,"nom_image")
sheet.write(0,1, "date")

for i in range(1,101):
    month = random.randint(1,12)
    year = random.randint(2020,2023)

    image_name  = f"img{i}_{month:02d}_{year}.png"

    date_str = f"{month:02d}/{year}"

    sheet.write(i,0,image_name)
    sheet.write(i,1,date_str)

workbook.save("session_images.json")
print("Fichier generer avec succès")
