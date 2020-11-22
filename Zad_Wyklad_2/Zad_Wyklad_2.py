import pandas as pd
from pandasgui import show

df = pd.read_csv("C:\\Users\\Mopek\\OneDrive\\Pulpit\\Zad_Wyklad_2\\samochody1tys.csv")
print("Użyte metody: 1.Sort values, 2. Group by, 3. Mean, 4. Drop, 5. Sum, 6. Head, 7. Rename, 8. Query, 9. Copy, 10. Value counts")
#show(df)

print("Sortowanie po przebiegu, od najmniejszego: ")
#show(df.sort_values('przebieg', ascending=True))
print("Średnia parametrów u danego producenta: ")
#show(df.groupby(by="marka").mean().drop(columns='id'))

print("Największa kapitalizacja rynkowa w udziale danego rodzaju używanego paliwa: ")
#show(df.groupby(by="rodzaj_silnika").sum().drop(columns=['id','rok_produkcji','przebieg','pojemnosc_silnika']).sort_values('cena', ascending=False).head(1))
print("Translacja nazw kolumn na j. angielski: ")
#show(df.rename(columns={'id':'id', 'marka':'mark','rok_produkcji':'production_year','rodzaj_silnika':'type_of_engine','pojemnosc_silnika':'engine_capacity','przebieg':'mileage','cena':'price','wojewodztwo':'province'}))
print("Pojazdy z województwa pomorskiego: ")
dfc = df.copy()
dfc.query('wojewodztwo == "Pomorskie"', inplace = True)
#show(dfc)
print("Ilość pojazdów poszczególnych marek na rynku: ")
show(df['marka'].value_counts())

