import csv

scoreMax = 0
topRated = '' # titre du film le mieux noté
numMovies = 0 # films entre 2000 et 2010



with open('../deniro.csv', 'r') as csv_file:
  
  # le paramètre "delimiter" permet d'indiquer le caractère de séparation de colonne
  rows = csv.reader(csv_file, delimiter=',') 
  lineCount = 0
  for r in rows:
    if lineCount != 0: # pas la ligne d'entête
      if int(r[1]) > scoreMax:
        scoreMax = int(r[1])
        topRated = r[2]
      if int(r[0]) >= 2000 and int(r[0]) <= 2010:
        numMovies += 1

    lineCount += 1

#print(topRated, numMovies)
# création d'un fichier de rapport
with open('deniro-report.txt', 'w') as report_file:
  report_file.write('Film le mieux noté: %s\nNombre de films entre 2000 et 2010: %d' % (topRated, numMovies) )