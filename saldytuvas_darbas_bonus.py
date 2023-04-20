# skysti_produktai = ['pienas', 'jogurtas', 'kefyras', 'gira', 'degtine', 'obuoliu sultys']
# kieti_produktai = ['kvieciu miltai', 'rugiu miltai', 'kukuruzu miltai', 'ryziu miltai', 'makaronai penne']
# paruosti_patiekalai = ['krosanai', 'amerikietiški blyneliai','lietiniai blynai', 'spurgos']

# saldytuvo_produktai = skysti_produktai + kieti_produktai + paruosti_patiekalai

# import os
# os.system('cls')

# saldytuvas = {}

# while True:
# #    os.system('cls')

#     print('------- Meniu -------')
#     print('1: Įdėti produktus')
#     print('2: Išimti produktus')
#     print('3: Peržiūrėti sarašą')
#     print('4: Bendras svoris')
#     print('0: išeiti')

    

#     def prideti_produktus():
#         print(f"{'Numeracija':<10} {'Produktai'}")  # string formating to add column names for 'task index' & 'task name'
#         for i, task in enumerate(saldytuvo_produktai):
#             print("{:<10} {}".format(i, task))  # formated & descriptive in terminal / harder to read as code
#             produkto_pasirinkimas = input('Įveskite norima produktą: ')
#             produktu_kiekis = float(input('Įveskite produkto kiekį (kg/L): '))
#         return[produkto_pasirinkimas, produktu_kiekis]
    
#     def isimti_produktus():
#         return
    
#     def perziureti_sarasa():
#         return
    
#     def bendras_svoris():
#         return
    

        

#     pasirinkimas = input('Pasirinkite: ')

#     if pasirinkimas == "0":
#         os.system('cls')
#         print('------- Viso gero -------')
#         break

#     elif pasirinkimas == "1":

#  #       os.system('cls')
#         prideti_produktus()

#     elif pasirinkimas == "2":
#  #       os.system('cls')
#         isimti_produktus()

#     elif pasirinkimas == "3":
#  #       os.system('cls')
#         perziureti_sarasa()

#     elif pasirinkimas == "4":
#  #       os.system('cls')
#         bendras_svoris()

#     else:
#  #       os.system('cls')
#         print ('netinka')


# import os

# os.system('cls')

# kieti = {}
# skysti = {}
# paruosti = {}



# while True:
# #    os.system('cls')

#     print("------- Meniu -------")
#     print("1: Prideti produktus")
#     print("2: Isimti produktus")
#     print("3: Perziureti produktu sarasa")
#     print("4: Perziureti bendra produktu svori")
#     print("0: išeiti")

#     pasirinkimas = input("Pasirinkite: ")



#     if pasirinkimas == "1":

#         while True:
#             print (f'kieti produktai: {kieti}')
#             print (f'skysti produktai: {skysti}')
#             print (f'paruosti produktai: {paruosti}')
#             print("------- Meniu -------")
#             print("1: Prideti produktus")
#             print("0: Iseiti")
#             pasirinkimas1 = int(input("Pasirinkite:"))
#             if pasirinkimas1 == 1:
# #            os.system('cls')
#                 print (f'kieti produktai: {kieti}')
#                 print (f'skysti produktai: {skysti}')
#                 print (f'paruosti produktai: {paruosti}')
#                 print('Iveskite produkta:')
#                 produktas = input(">: ")
#                 print('Iveskite kieki:')
#                 kiekis = input(">: ")
#                 print('Iveskite tipa: kietas(k)/skystas(s)/paruoštas(p):')
#                 tipas = input(">: ")
#                 if tipas == "k":
#                     kieti[produktas] = kiekis
#                 if tipas == "s":
#                     skysti[produktas] = kiekis
#                 if tipas == "p":
#                     paruosti[produktas] = kiekis
#             elif pasirinkimas1 == 0:
#                 print("viso gero")
#                 break
#             else:
#                 break



#     elif pasirinkimas == "2":
#         pass
#     elif pasirinkimas == "3":
#          pass   
#     elif pasirinkimas == "4":
#          pass   

#     elif pasirinkimas == "0":
# #        os.system('cls')
#         print('------- Viso gero -------')
#         break

#     else:
#         print('Iveskite skaiciu is meniu')



import os
os.system('cls')
produktai = {}
receptas = {}

while True:
    os.system('cls')

    # Pagrindinis meniu
    print("-Programa šaldytuvas-")
    print("------- Meniu -------\n")
    print("1: Pridėti produktus į šaldytuvą")
    print("2: Išimti produktus iš šaldytuvo")
    print("3: Peržiūrėti šaldytuvo produktų sąrašą")
    print("4: Peržiūrėti bendrą produktų svorį šaldytuve")
    print("5: Ar išeina")
    print("0: Uždaryti šaldytuvą")

    pasirinkimas = input("\nPasirinkite: ") #

    # Meniu pasirinkimas - 1 
    if pasirinkimas == "1":
        os.system('cls')
        print (f'Produktų sąrašas: {produktai}')
        print('Įveskite produktą:')            
        produktas = input(">: ")
        print('Įveskite kiekį:')
        kiekis = input(">: ")
        produktai[produktas] = kiekis

    # Meniu pasirinkimas - 2 
    elif pasirinkimas == "2":
        os.system('cls')
        print(f'Produktų sąrašas: {produktai}')
        print('Įveskite produktą:')
        produktas = input(": ")
        del produktai[produktas]

    # Meniu pasirinkimas - 3 
    elif pasirinkimas == "3":
        os.system('cls')
        print (f'Produktų sąrašas: {produktai}')
        input("Spauskite ENTER, kad grįžti į ankstesnį meniu")
    
    # Meniu pasirinkimas - 4     
    elif pasirinkimas == "4":
        os.system('cls')
        is_viso = 0
        produktai_list = list(produktai.values())
        for produktas in produktai_list:
            is_viso = is_viso + float(produktas)
        print(f'Bendras produktų svoris šaldytuve: {is_viso:.01f} kg')
        input("Spauskite ENTER, kad grįžti į ankstesnį meniu")

    # Meniu pasirinkimas - 5
    if pasirinkimas == "5":
        while True:
            os.system('cls')
            print (f'Receptas: {receptas}')
            print('Įveskite vienos porcijos receptą (pvz.: pienas:1). Baigę įvesti produktus, paspauskite ENTER')
            pasirinkimas51 = input(">: ")
            if pasirinkimas51 != "":
                receptas[pasirinkimas51.split(":")[0]] = (pasirinkimas51.split(":")[1])
            else:
                break
        os.system('cls')
        print (f'Receptas: {receptas}')
        print('Įveskite porcijų kiekį:')
        porciju_kiekis = int(input(">: "))
        print (f'Receptas (1 porcija): {receptas}')
        for x in receptas:
            a = receptas.get(x)
            (receptas[x]) = float(receptas.get(x)) * porciju_kiekis
        print (f'Receptas ({porciju_kiekis} porcijos): {receptas}')   
        input("Spauskite ENTER, kad grįžti į ankstesnį meniu")

    
    # Meniu pasirinkimas - 0 
    elif pasirinkimas == "0":
        os.system('cls')
        print('------- Gražios dienos! -------')
        break

    # Meniu pasirinkimas - neteisingai
    else:
        print('Įveskite skaičių iš meniu')


