import argparse
import os

file = open('C:\\Users\\Mopek\\OneDrive\\Pulpit\\Zad_Wyklad_6\\Hennig.txt')
"""
# #otwarcie pliku tylko do odczytu
file = open('Hennig.txt','r')
# #otwarcie pliku tylko zapisu
file = open('Hennig.txt','w')
#typ pliku
type(file)
#Otwarcie pliku binarnego tylko do odczytu
file = open('Hennig.txt', 'rb')
#Otwarcie pliku binarnego do zapisu
file = open('Hennig.txt','wb')
#Otwarcie pliku RAW
file = open('Hennig.txt', 'rb',buffering=0)
type(file)
#Czytanie i wyświetlenie pliku
with open('Hennig.txt', 'r') as reader:
 print(reader.read())
#Porcjowanie Wyświetlanych danych - w bajtach
with open('Hennig.txt', 'r') as reader:
 print(reader.read(8))
 print(reader.read(8))
 print(reader.read(8))
 print(reader.read(8))"""
#Wyświetlanie textu linia po linii
with open('C:\\Users\\Mopek\\OneDrive\\Pulpit\\Zad_Wyklad_6\\Hennig.txt', 'r') as reader:
 Head = reader.readlines()
 for line in reader:
  print(line, end='')
#Working With Two Files at the Same Time And Reversing
d_path = 'C:\\Users\\Mopek\\OneDrive\\Pulpit\\Zad_Wyklad_6\\Hennig.txt'
d_r_path = 'C:\\Users\\Mopek\\OneDrive\\Pulpit\\Zad_Wyklad_6\\Hennig_reversed.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    Hennig = reader.readlines()
    writer.writelines(reversed(Hennig))
#Otwarcie Pliku Graficznego po kilka bitów
with open('C:\\Users\\Mopek\\OneDrive\\Pulpit\\Zad_Wyklad_6\\hennig.png', 'rb') as byte_reader:
    print(byte_reader.read(1))
    print(byte_reader.read(3))
    print(byte_reader.read(2))
    print(byte_reader.read(1))
    print(byte_reader.read(1))


#APPEND FILE
with open('C:\\Users\\Mopek\\OneDrive\\Pulpit\\Zad_Wyklad_6\\Hennig.txt', 'a') as a_writer:
    a_writer.write('\nNOWA LINIA NICZYM HISZPAŃSKA INKWIZYCJA - NIESPODZIEWANA')
with open('C:\\Users\\Mopek\\OneDrive\\Pulpit\\Zad_Wyklad_6\\Hennig.txt', 'r') as reader:
 print(reader.read())

#Tworzenie własnego menedżera kontekstu
class my_file_reader():
    def __init__(self, file_path):
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path)
        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()

