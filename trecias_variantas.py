import os
import datetime

class Irasas():
    def __init__(self, suma, komentaras, dataa):
        '''Konstruktorius, skirtas sukurti naują Irasas objektą.
        
        Argumentai:
        suma (int): suma
        komentaras (str): įvedamo įrašo komentaras
             
        Grąžinamos reikšmės:
        None
        '''   
        self.suma = suma
        self.komentaras = komentaras
        self.dataa = dataa

class Islaidos(Irasas):
    '''Klasė, skirta biudžeto islaidu irašams laikyti'''
    def __init__(self, suma, komentaras, dataa, gavejas):
        '''
        Konstruktorius, skirtas sukurti naują Islaidos objektą.
        
        Argumentai:
        suma (float): suma
        komentaras (str): įvedamų pajamų komentaras
        siuntejas (str): iš kur gautos pajamos
        
        Grąžinamos reikšmės:
        None
        '''
        super().__init__(suma, komentaras, dataa)
        self.gavejas = gavejas

class Pajamos(Irasas):
    '''Klasė, skirta biudžeto pajamų irašams laikyti'''
    def __init__(self, suma, komentaras, dataa, siuntejas):
        '''
        Konstruktorius, skirtas sukurti naują Pajamos objektą.
        
        Argumentai:
        suma (float): suma
        komentaras (str): įvedamų pajamų komentaras
        siuntejas (str): iš kur gautos pajamos
        
        Grąžinamos reikšmės:
        None
        '''
        super().__init__(suma, komentaras, dataa)
        self.siuntejas = siuntejas

class Biudzetas():
    '''Klasė, skirta biudžeto žurnalui laikyti'''
    def __init__(self):
        '''
        Konstruktorius, skirtas sukurti naują Biudzetas objektą.
        
        Grąžinamos reikšmės:
        None
        '''
        self.__zurnalas = []
        #self.pajamos = []
        #self.islaidos = []

    def ataskaita(self):
        '''
        Funkcija, kuri atspausdina biudžeto ataskaitos informaciją.
        
        Grąžinamos reikšmės:
        None
        '''
        print("Biudzeto ataskaita:")
        for irasas in self.__zurnalas:
            if isinstance(irasas, Pajamos):
                #self.pajamos = [irasas.dataa, irasas.komentaras, irasas.suma]
                print("Pajamos")
                print(f"Data: {irasas.dataa} {irasas.komentaras}: {irasas.suma}")
            else:
                print("Islaidos")
                print(f"Data: {irasas.dataa} {irasas.komentaras}: {irasas.suma}")
        print()

    def balansas(self):
        '''
        Funkcija, kuri atspausdina balanso informaciją.
        
        Grąžinamos reikšmės:
        None
        '''
        balansas = 0
        for irasas in self.__zurnalas:
            if isinstance(irasas, Islaidos):
                balansas -= irasas.suma
            elif isinstance(irasas, Pajamos):
                balansas += irasas.suma
        print(f"Einamasis balansas: {balansas}")
        print()

    def naujas_pajamu_irasas(self, suma, komentaras, dataa, siuntejas):
        '''
        Funkcija, kuri atspausdina naują pajamų įrašo informaciją.
        
        Grąžinamos reikšmės:
        None
        '''
        pajamos = Pajamos(suma, komentaras, dataa, siuntejas)
        self.__zurnalas.append(pajamos)
        print("Pajamų įrašas sėkmingai pridėtas.")
        print()

    def naujas_islaidu_irasas(self, suma, komentaras, dataa, gavejas):
        '''
        Funkcija, kuri atspausdina naują pajamų įšlaidų informaciją.
        
        Grąžinamos reikšmės:
        None
        '''
        islaidos = Islaidos(suma, komentaras, dataa, gavejas)
        self.__zurnalas.append(islaidos)
        print("Išlaidų įrašas sėkmingai pridėtas.")
        print()

biudzetas = Biudzetas()

while True:
    print("\n+++++++++++++++++++++++++++")
    print("*********BIUDŽETAS*********")
    print("---------------------------\n")
    print("Pasirinkite veiksmą:")
    print("1. Pridėti naują pajamų įrašą")
    print("2. Pridėti naują išlaidų įrašą")
    print("3. Spausdinti biudžeto ataskaitą")
    print("4. Spausdinti einamąjį balansą")
    print("5. Išeiti iš programos")

    choice = input("Jūsų pasirinkimas: ")
    print()

    if choice == "1":
        os.system('cls')
        suma = float(input("Įveskite pajamų sumą: "))
        komentaras = input("Įveskite komentarą: ")
        siuntejas = input("Įveskite pajamų siuntėją: ")
        dataa = datetime.datetime.now().replace(microsecond=0)
        biudzetas.naujas_pajamu_irasas(suma, komentaras, dataa, siuntejas)

    elif choice == "2":
        os.system('cls')
        suma = float(input("Įveskite išlaidų sumą: "))
        komentaras = input("Įveskite komentarą: ")
        gavejas = input("Įveskite išlaidų gavėją: ")
        dataa = datetime.datetime.now().replace(microsecond=0)
        biudzetas.naujas_islaidu_irasas(suma, komentaras, dataa, gavejas)

    elif choice == "3":
        os.system('cls')
        biudzetas.ataskaita()

    elif choice == "4":
        os.system('cls')
        biudzetas.balansas()

    elif choice == "5":
        print("Geros dienos!")
        break

    else:
        print("Neteisingas pasirinkimas, bandykite dar kartą.")
        print()