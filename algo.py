
import json
from collections import defaultdict

import random
from datetime import datetime

def exporter_vers_json(xls_path,json_path):
    try:
        import xlrd

        workbook = xlrd.open_workbook(xls_path)
        sheet = workbook.sheet_by_index(0)

        data = defaultdict(list)
        
        for ligne in range(1,sheet.nrows):
            img_name = sheet.cell_value(ligne,0)
            date = sheet.cell_value(ligne,1)
            data[date].append(img_name)

        with open(json_path, 'w') as file:
            json.dump(data, file,indent=2)
        print(f"Données exportées vers {json_path}")

    except Exception as ex:
        print(f"Erreur Excel : {ex}")

xls_path = "session_images.xls"
json_path = "timeline_data.json"

exporter_vers_json(xls_path,json_path)
