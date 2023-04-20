class Vartotojas:
    def __init__(self, vardas, pavarde, biudzetas) -> None:
        '''Įrašomas Vartotojas(vardas, pavarde, biudzetas)'''
        self.vardas = vardas
        self.pavarde = pavarde
        self.__biudzetas = biudzetas
    
    def __get_biudzetas(self):
        print(f'Jūsų dabartinsi biudžetas: {self.__biudzetas}')
    
