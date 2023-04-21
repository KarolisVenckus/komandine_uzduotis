import date

today = date.today()

class Vartotojas:
    def __init__(self, vardas, pavarde, biudzetas) -> None:
        '''Įrašomas Vartotojas(vardas, pavarde, biudzetas)'''
        self.vardas = vardas
        self.pavarde = pavarde
        self.__biudzetas = biudzetas
    
    def __get_biudzetas(self):
        print(f'Jūsų dabartinsi biudžetas: {self.__biudzetas}')
    


class BalansoLikutis:
    def __init__(self, balansas, pin_kodas):
        self.__balansas = balansas
        self.__pin_kodas = pin_kodas

    def rodyti_balansa(self, suma, pin_kodas):
        if pin_kodas == self.__pin_kodas:
            self.__balansas -= suma
            print(f'PIN kodas teisingas. Sąskaitos likutis - {self.__balansas} EUR')
        else:
            print(f'PIN kodas neteisingas')

saskaita = BalansoLikutis(1000, 0000)

saskaita.rodyti_balansa(100, int(input("Įveskite 4 skaitmenų PIN kodą:")))