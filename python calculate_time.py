import csv
import json

fichier_csv = 'Tutur33-codetime-records-17_02_2024 19_23_09.csv'

with open(fichier_csv, 'r') as fichier:
  lecteur_csv = csv.DictReader(fichier)
  minutes = 0
  editor = {}
  platform = {}
  project = {}
  relative_file = {}
  language = {}


  for ligne in lecteur_csv:
    if ligne['event_time'] is not None:
      minutes += 1
    if ligne['editor'] in editor:
      editor[ligne['editor']] += 1
    else:
      editor[ligne['editor']] = 1
    if ligne['platform'] in platform:
      platform[ligne['platform']] += 1
    else:
      platform[ligne['platform']] = 1
    if ligne['project'] in project:
      project[ligne['project']] += 1
    else:
      project[ligne['project']] = 1
    if ligne['relative_file'] in relative_file:
      relative_file[ligne['relative_file']] += 1
    else:
      relative_file[ligne['relative_file']] = 1
    if ligne['language'] in language:
      language[ligne['language']] += 1
    else:
      language[ligne['language']] = 1

            
heures = minutes / 60
print(f"Temps total de code : {heures} heures")


# Calcul des pourcentages
for key in editor:
  editor[key] = round((editor[key] / minutes) * 100)

for key in platform:
  platform[key] = round((platform[key] / minutes) * 100)

for key in project:
  project[key] = round((project[key] / minutes) * 100)

for key in relative_file:
  relative_file[key] = round((relative_file[key] / minutes) * 100)

for key in language:
  language[key] = round((language[key] / minutes) * 100)

# Création d'un dictionnaire global
data = {
  "editor": editor,
  "platform": platform,
  "project": project,
  "relative_file": relative_file,
  "language": language
}

# Écriture dans un fichier JSON
with open('data.json', 'w') as f:
  json.dump(data, f, indent=4)

print("Les données ont été écrites dans le fichier data.json.")