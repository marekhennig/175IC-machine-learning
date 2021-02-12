import csv
import pandas

with open('C:\\Users\\Mopek\\OneDrive\\Pulpit\\Zad_Wyklad_8\\film_ratings.csv') as csv_file:
 csv_reader = csv.reader(csv_file, delimiter=',')
 line_count = 0
 for row in csv_reader:
      if line_count == 0:
          print(f'Column names are {", ".join(row)}')
          line_count += 1
      else:
          print(f'\tOcena dla filmu z gatunku{row[1]} o nazwie {row[2]} to {row[4]}.')
          line_count += 1
print(f'Processed {line_count} lines.')
csv_reader =''
#Odczytanie pliku metodą słownikową
with open('C:\\Users\\Mopek\\OneDrive\\Pulpit\\Zad_Wyklad_8\\film_ratings.csv', mode='r') as csv_file:
  csv_reader = csv.DictReader(csv_file, delimiter=',')
  line_count = 0
  for row in csv_reader:
   if line_count == 0:
    print(f'Column names are {", ".join(row)}')
    line_count += 1
   print(f'\tOcena dla filmu z gatunku {row["gatunek"]}  o nazwie {row["tytul"]} to {row["ocena"]}.')
   line_count += 1

#Zapis do pliku
with open('C:\\Users\\Mopek\\OneDrive\\Pulpit\\Zad_Wyklad_8\\film_ratings2.csv', mode='w') as csv_file:
  csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  csv_writer.writerow(['Fantasy', 'Fantastyczne Zwierzęta Nie Da Się Ich Znaleźć', 'Wielka Brytania', '8'])
  csv_writer.writerow(['Fantasy', 'Mikołaj Odda Mi Kiedyś 6000zł Które ukradł', 'Polska', '1'])

#Zapis do pliku z wykorzystaniem słownika
with open('C:\\Users\\Mopek\\OneDrive\\Pulpit\\Zad_Wyklad_8\\film_ratings3.csv', mode='w') as csv_file:
    fieldnames = ['gatunek', 'tytul', 'produkcja', 'ocena']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow({'gatunek':'Fantasy', 'tytul':'Fantastyczne Zwierzęta Nie Da Się Ich Znaleźć', 'produkcja':'Wielka Brytania', 'ocena':'8'})
    csv_writer.writerow({'gatunek':'Fantasy', 'tytul':'Mikołaj Odda Mi Kiedyś 6000zł Które ukradł', 'produkcja':'Polska', 'ocena':'1'})

#Wykorzystanie Zewnętrznych CSV - pandas z laboratoriów
df = pandas.read_csv('C:\\Users\\Mopek\\OneDrive\\Pulpit\\Zad_Wyklad_8\\film_ratings.csv')
df