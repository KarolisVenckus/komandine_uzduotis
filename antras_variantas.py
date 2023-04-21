import os

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
        self.pajamos = []
        self.islaidos = []

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
        input("Paspauskite ENTER, kad tęstumėte...")
        os.system('cls')

    elif choice == "2":
        suma = float(input("Įveskite išlaidų sumą: "))
        komentaras = input("Įveskite komentarą: ")
        gavejas = input("Įveskite išlaidų gavėją: ")
        biudzetas.naujas_islaidu_irasas(suma, komentaras, gavejas)
        input("Paspauskite ENTER, kad tęstumėte...")
        os.system('cls')

    elif choice == "3":
        biudzetas.ataskaita()
        input("Paspauskite ENTER, kad tęstumėte...")
        os.system('cls')

    elif choice == "4":
        biudzetas.balansas()
        input("Paspauskite ENTER, kad tęstumėte...")
        os.system('cls')

    elif choice == "5":
        print("Geros dienos!")
        break

    else:
        print("Neteisingas pasirinkimas, bandykite dar kartą.")
        print()