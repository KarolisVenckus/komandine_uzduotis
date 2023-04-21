'Klasės'
'Irasas (abstraktus)'

'savybė suma'
'savybė komentaras'
'Islaidos(Irasas)'

'savybė gavejas'
'Pajamos(Irasas)'

'-savybė siuntejas'
'-Biudzetas'

'-savybe zurnalas: sąrašas įrašų'
'Biudzetas turi turėti metodus:'

'ataskaitai'
'balansas'
'pajamų įrašo sukūrimas ir įtraukimui į žurnalą'
'išlaidų įrašo sukūrimas ir įtraukimui į žurnalą'
'Programos meniu ir funkcionalumą galite įgyvendinti tiek per klasę, tiek pagrindinėje programoje.'

import os
os.system('cls')

# class Irasas():
#     balansas = 0
#     def __init__(self, suma, komentaras):
#         self.suma = suma
#         self.komentaras = komentaras

#     def islaidos(self, suma):
#         pass



# class Islaidos(Irasas):
#     def islaidos(self, suma):
#         self.balansas = self.balansas - suma
#         print(f"Isemimas sekmingas, balansas yra {self.balansas}")

class Irasas():
    def __init__(self, suma, komentaras):
        self.suma = suma
        self.komentaras = komentaras

class Islaidos(Irasas):
    def __init__(self, suma, komentaras, gavejas):
        super().__init__(suma, komentaras)
        self.gavejas = gavejas

class Pajamos(Irasas):
    def __init__(self, suma, komentaras, siuntejas):
        super().__init__(suma, komentaras)
        self.siuntejas = siuntejas

class Biudzetas():
    def __init__(self):
        self.zurnalas = []

    def ataskaita(self):
        print("Biudzeto ataskaita:")
        for irasas in self.zurnalas:
            print(f"{irasas.komentaras}: {irasas.suma}")
        print()

    def balansas(self):
        balansas = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, Islaidos):
                balansas -= irasas.suma
            elif isinstance(irasas, Pajamos):
                balansas += irasas.suma
        print(f"Einamasis balansas: {balansas}")
        print()

    def naujas_pajamu_irasas(self, suma, komentaras, siuntejas):
        pajamos = Pajamos(suma, komentaras, siuntejas)
        self.zurnalas.append(pajamos)
        print("Pajamų įrašas sėkmingai pridėtas.")
        print()

    def naujas_islaidu_irasas(self, suma, komentaras, gavejas):
        islaidos = Islaidos(suma, komentaras, gavejas)
        self.zurnalas.append(islaidos)
        print("Išlaidų įrašas sėkmingai pridėtas.")
        print()


biudzetas = Biudzetas()

while True:
    print("Pasirinkite veiksmą:")
    print("1. Pridėti naują pajamų įrašą")
    print("2. Pridėti naują išlaidų įrašą")
    print("3. Spausdinti biudžeto ataskaitą")
    print("4. Spausdinti einamąjį balansą")
    print("5. Išeiti iš programos")

    choice = input("Jūsų pasirinkimas: ")
    print()

    if choice == "1":
        suma = float(input("Įveskite pajamų sumą: "))
        komentaras = input("Įveskite komentarą: ")
        siuntejas = input("Įveskite pajamų siuntėją: ")
        biudzetas.naujas_pajamu_irasas(suma, komentaras, siuntejas)

    elif choice == "2":
        suma = float(input("Įveskite išlaidų sumą: "))
        komentaras = input("Įveskite komentarą: ")
        gavejas = input("Įveskite išlaidų gavėją: ")
        biudzetas.naujas_islaidu_irasas(suma, komentaras, gavejas)

    elif choice == "3":
        biudzetas.ataskaita()

    elif choice == "4":
        biudzetas.balansas()

    elif choice == "5":
        print("Geros dienos!")
        break

    else:
        print("Neteisingas pasirinkimas, bandykite dar kartą.")
        print()

# while True:
#     os.system('cls')

#     # Pagrindinis meniu
#     print("-BUHALTERIJA-")
#     print("------- Meniu -------\n")
#     print("1: Patikrinti balansa")
#     print("2: Irasyti pajamas")
#     print("3: Irasyti islaidas")
#     print("4: Peržiūrėti ataskaita")

#     print("0: Uždaryti programa")

#     pasirinkimas = input("\nPasirinkite: ")

#     # Patikrinti balansa
#     if pasirinkimas == "1":
#         break

#     # Irasyti pajamas
#     elif pasirinkimas == "2":
#         break

#     # Irasyti islaidas 
#     elif pasirinkimas == "3":
#         #os.system('cls')
#         print("Irasyti islaidas")
#         print('Įveskite islaidos suma:')            
#         suma = input(">: ")
#         print('Įveskite komentara:')
#         komentaras = input(">: ")
#         kazkas = Islaidos()
#         kazkas.suma = suma
#         print(kazkas.suma())
#         input("press enter")

    
#     # Perziureti ataskaita    
#     elif pasirinkimas == "4":
#         break

    
#     # Iseiti is programos
#     elif pasirinkimas == "0":
#         break

#     # Neteisingai pasirinktas meniu punktas
#     else:
#         print('Blogas pasirinkimas, bandykite dar karta')