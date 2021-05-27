
#A teraz coś z zupełnie innej beczki. Wyobraź sobie, że tworzysz system obsługujący bibliotekę filmów i seriali.
# Wykorzystaj wiedzę na temat programowania obiektowego i napisz program, który spełnia następujące założenia:

 #   Jest w stanie przechowywać informacje na temat filmów, które znajdują się w systemie.
#   Każdy film powinien mieć następujące atrybuty:
    #    Tytuł
     #   Rok wydania
      #  Gatunek
      #  Liczba odtworzeń


#Umożliwia przechowywanie informacji na temat seriali. Każdy serial powinien mieć następujące atrybuty:

 #   Tytuł
  #  Rok wydania
   # Gatunek
   # Numer odcinka
   # Numer sezonu
   # Liczba odtworzeń

import random

class filmy:
    def __init__(self, tytuł, Rok_wydania, Gatunek, Liczba_odtworzeń):
        self.tytuł = tytuł
        self.Rok_wydania = Rok_wydania
        self.Gatunek = Gatunek
        self.Liczba_odtworzeń = Liczba_odtworzeń
    # Filmy i seriale mają metodę play, która zwiększa liczbę odtworzeń danego tytułu o 1.



    def play(self):
        self.Liczba_odtworzeń = self.Liczba_odtworzeń + 1
    def __str__(self):
        return f"{self.tytuł} {self.Rok_wydania} {self.Liczba_odtworzeń} "

#Po wyświetleniu serialu jako string pokazują się informacje o konkretnym odcinku, np.: “The Simpsons S01E05” (gdzie po S pokazany jest numer sezonu
# w notacji dwucyfrowej, natomiast po E - numer odcinka, również w zapisie dwucyfrowym). Po wyświetleniu filmu jako string widoczne są tytuł i rok wydania
# np. “Pulp Fiction (1994)”.
# Przechowuje filmy i seriale w jednej liście.


class seriale(filmy):
    def __init__(self, Numer_odcinka, Numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Numer_odcinka = Numer_odcinka
        self.Numer_sezonu = Numer_sezonu
    def __str__(self):
        return f"{self.tytuł} S{self.Numer_odcinka:02}E{self.Numer_sezonu:02} {self.Liczba_odtworzeń}"


film_1 = filmy (tytuł="Comando", Rok_wydania=1981, Gatunek="True shit", Liczba_odtworzeń=123)
film_2 = filmy (tytuł="Natural Born Killers", Rok_wydania=1993, Gatunek="True shit", Liczba_odtworzeń=21)
film_3 = filmy (tytuł="FIght Club", Rok_wydania=1996, Gatunek="Sociodelic", Liczba_odtworzeń=34)

serial_1 = seriale (tytuł="Twin Peaks", Rok_wydania=1990, Gatunek="Thriler", Numer_odcinka=1, Numer_sezonu=1, Liczba_odtworzeń=66)
serial_2 = seriale (tytuł="Twin Peaks", Rok_wydania=1990, Gatunek="Thriler", Numer_odcinka=2, Numer_sezonu=1, Liczba_odtworzeń=66)
serial_3 = seriale (tytuł="Twin Peaks", Rok_wydania=1990, Gatunek="Thriler", Numer_odcinka=3, Numer_sezonu=1, Liczba_odtworzeń=66)
serial_4 = seriale (tytuł="Star Wars", Rok_wydania=1993, Gatunek="Fantasy", Numer_odcinka=5, Numer_sezonu=2, Liczba_odtworzeń=0)

lista = [film_1, film_2, film_3, serial_1, serial_2, serial_3, serial_4]

#Napisz funkcje get_movies oraz get_series, które będą filtrować listę i zwracać odpowiednio tylko filmy oraz tylko seriale.
# Posortuj listę wynikową alfabetycznie.



def get_movies(lista):
    for i in lista:
        if str(type(i)) == "<class '__main__.filmy'>":
            print(i)

def get_series(lista):
    for i in lista:
        if str(type(i)) == "<class '__main__.seriale'>":
            print(i)

get_movies(lista)
get_series(lista)

# Napisz funkcję search, która wyszukuje film lub serial po jego tytule.


def search (lista):
    x = input("podaj tytuł: ")
    for i in lista:

        if x == i.tytuł:
            print (i)

search(lista)


print ("")
print ("")

#Napisz funkcję generate_views, która losowo wybiera element z biblioteki, a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.


def generate_views(lista):
    x = len(lista)
    y = random.randrange(0, x - 1)
    losowy = lista[y]
    losowy.Liczba_odtworzeń = random.randrange(1, 100)
    print(losowy)

generate_views(lista)

("")
("")

# Napisz funkcję, która uruchomi generate_views 10 razy.

def gen10(lista):
    for i in range(9):
        generate_views(lista)

gen10(lista)
print ("")

print ("top_titles")

# Napisz funkcję top_titles(), która zwróci wybraną ilość najpopularniejszych
# tytułów z biblioteki.

def top_titles(lista, rodzaj):
    lista2 = sorted(lista, key=lambda lista: lista.Liczba_odtworzeń)
    lista3 = reversed(lista2)

    x = 0
    for i in lista3:
        x = x + 1
        if rodzaj == 'filmy' and str(type(i)) == "<class '__main__.filmy'>":
            print(i)
        if rodzaj == 'seriale' and str(type(i)) == "<class '__main__.seriale'>":
            print(i)
        if x == 10:
            break

top_titles(lista, 'seriale')

top_titles(lista, 'filmy')


# Napisz funkcję, która za pomocą pętli dodaje pełne sezony seriali do biblioteki.
# Funkcja powinna przyjmować parametry takie jak: tytuł serialu, rok wydania, gatunek, numer sezonu, liczba odcinków do dodania.

def dodaj_seriale(lista, tytul, rok_wydania, gatunek, liczba_odcinkow, sezon):
    for i in range(1, liczba_odcinkow + 1):
        serial = seriale(tytuł=tytul, Rok_wydania=rok_wydania, Gatunek=gatunek, Numer_odcinka=i, Numer_sezonu=sezon, Liczba_odtworzeń=0)
        lista.append(serial)

dodaj_seriale(lista, "Dexter", 1999, "Horror", 10, 1)

for i in lista:
    print(i)

exit()

