import datetime

class Irasas():
    def __init__(self, suma, komentaras, dataa):
        self.suma = suma
        self.komentaras = komentaras
        self.dataa = dataa

class Islaidos(Irasas):
    def __init__(self, suma, komentaras, dataa, gavejas):
        super().__init__(suma, komentaras, dataa)
        self.gavejas = gavejas

class Pajamos(Irasas):
    def __init__(self, suma, komentaras, dataa, siuntejas):
        super().__init__(suma, komentaras, dataa)
        self.siuntejas = siuntejas

class Biudzetas():
    def __init__(self):
        self.zurnalas = []
        self.pajamos = []
        self.islaidos = []

    def ataskaita(self):
        print("Biudzeto ataskaita:")
        for irasas in self.zurnalas:
            if isinstance(irasas, Pajamos):
                #self.pajamos = [irasas.dataa, irasas.komentaras, irasas.suma]
                print("Pajamos")
                print(f"Data: {irasas.dataa} {irasas.komentaras}: {irasas.suma}")
            else:
                print("Islaidos")
                print(f"Data: {irasas.dataa} {irasas.komentaras}: {irasas.suma}")
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

    def naujas_pajamu_irasas(self, suma, komentaras, dataa, siuntejas):
        pajamos = Pajamos(suma, komentaras, dataa, siuntejas)
        self.zurnalas.append(pajamos)
        print("Pajamų įrašas sėkmingai pridėtas.")
        print()

    def naujas_islaidu_irasas(self, suma, komentaras, dataa, gavejas):
        islaidos = Islaidos(suma, komentaras, dataa, gavejas)
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
        dataa = datetime.datetime.now().replace(microsecond=0)
        biudzetas.naujas_pajamu_irasas(suma, komentaras, dataa, siuntejas)

    elif choice == "2":
        suma = float(input("Įveskite išlaidų sumą: "))
        komentaras = input("Įveskite komentarą: ")
        gavejas = input("Įveskite išlaidų gavėją: ")
        biudzetas.naujas_islaidu_irasas(suma, komentaras, datetime.datetime.now().replace(microsecond=0), gavejas)

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