# Cw1
tekst = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
# Cw2
print(f'W tekście jest liczba liter {tekst.count("a")}')
Imie = "Maksymilian"
Nazwisko = "Pliszczyński"
# cw3
from datetime import datetime

print('{} {}'.format('jeden', 'dwa'))
print('{1} {0}'.format('1', '2'))
print('{:>10}'.format('Witam'))
print('{:f}'.format(3.141592653589793))
print('{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)))
# cw4
print(dir("witam"))
help("witam".capitalize())

# cw5 Wyszukaj w Internecie pojęcie „extended slice” w kontekście Pythona i wyświetl swoje imię i nazwisko z odwróconą kolejnością znaków z kapitalikami. Np. Fotzsyzrk Kaipor
im = "Maks"
naz = "Pliszczyński"
print(f'{im[::-1].capitalize()} {naz[::-1].capitalize()}')
# cw6 Stwórz listę z wartościami od 1 do 10. Następnie podziel listę tak, aby pierwsze 5 liczb zostało w oryginalnej liście a pozostałe 5 znalazło się w nowej liście.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = lista[5:]
lista = lista[:5]
print(lista)
print(lista2)
# cw7 Połącz te listy ponownie. Dodaj do listy wartość „0” na początku. Utwórz kopię połączonej listy i wyświetl listę posortowaną malejąco.
lista.extend(lista2)
lista.insert(0, 0)
lista_copy = lista
lista_copy.sort(reverse=True)
print(lista_copy)
# cw8 Za pomocą krotek stwórz listę studentów swojej grupy przypisując numer indeksu do imienia i nazwiska (dane nie muszą być prawdziwe).
student1 = (132421, "Bogusław", "Linda")
studnet2 = (132231, "Student", "Pierwszy")
student3 = (141283, "Jacek", "Sikorski")
Lista = [student1, studnet2, student3]
print(Lista)
# cw9 Przekształć poprzednie zadanie na słownik, a następnie dodaj pary zawierające wiek, adres email, rok urodzenia oraz adres.
studnet4 = dict(wiek=21,
                email='maks@yyy.com',
                adres='Olsztyn'
                )
studnet5 = dict(wiek=23,
                email='eeee@qqqq.com',
                adres='Bydgoszcz'
                )
studnet6 = dict(wiek=22,
                email='witam@yyy.com',
                adres='Wrocław'
                )
print(studnet6.keys())
print(studnet6.values())
# cw 10 Stwórz listę zawierającą numery telefonów z powtórzeniami, a następnie usuń powtórzenia za pomocą rzutowania na set.
tel_list = ["696022332", "578123482", "123456789", "696022332", "123456789"]
tel_list = set(tel_list)
print(tel_list)
# cw 11
for i in range(11):
    print(i)
# cw12
for i in range(20, 105, 5).__reversed__():
    print(i)
# 13Połącz całą wiedzę wydobytą z zajęć (i zadań) i stwórz program wypisujący dane z listy, która zawiera kilka słowników.
osoba1 = dict(
    imie='maks',
    nazwisko='witam',
    wiek=21,
    email='maks@yyy.com',
    adres='Olsztyn'
)
osoba2 = dict(
    imie='Janek',
    nazwisko='Sobieraj',
    wiek=25,
    email='janek@yyy.com',
    adres='Warszawa'
)
osoba3 = dict(
    imie='Adam',
    nazwisko='Lesniczy',
    wiek=23,
    email='adam@yyy.com',
    adres='Bydgoszcz'
)
MasterList = [osoba1,osoba2,osoba3]
print(f'Dane osób {MasterList}')

# cw1 Stwórz funkcję, która jako parametry przyjmuje dwie listy a_list oraz b_list. Następnie zwróć listę, która będzie posiadać parzyste indeksy z listy a_list oraz nieparzyste z b_list.
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b_list = [123, 123, 23435, 2123]


def funkcja(a_list, b_list):
    for i in a_list:
        if (i % 2) == 0:
            print(i)
    for i in b_list:
        if (i % 2) != 0:
            print(i)


print(funkcja(a_list, b_list))


# cw2Stwórz funkcję, która przyjmuje parametr data_text, a następnie zwróci następujące informacje o parametrze w formie słownika (dict):
def funkcja2(wartosci):
    wartosci = dict(
        długość=len(wartosci),
        litery=[char for char in wartosci]
    )
    print(wartosci.values())


data_text = "dddddddddd"
print(funkcja2(data_text))


# cw3
def funkcja3(text, letter):
    for litera in text:
        if (litera != letter):
            print(litera)


text = 'ddeeeebil'
print(funkcja3(text, chr(101)))


# cw 4 Funkcja temperatury
def funkcja4(temperatura):
    Kelvin = temperatura + 273.15
    Fahrenheit = (temperatura * 1.8) + 32
    Rankie = Kelvin * 1.8
    print(Kelvin)
    print(Fahrenheit)
    print(Rankie)


temperature_type = 10
print(funkcja4(temperature_type))


# cw5
class kalkulator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
calc = kalkulator(1,6)
print(calc.add())
#cw6
class ScienceCalculator : kalkulator


def __init__(self, a, b):
    self.a = a
    self.b = b
