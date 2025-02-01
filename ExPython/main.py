from Ex1 import RataDate
from Ex3 import TimpTransfer

alegere = input("Ce tip de problema vreti sa rezolvati? (rata de date | timp de trasnfer): ")
if alegere == "rata de date":
    nr_biti = int(input("Nr. de biti: "))
    nr_secunde = int(input("Nr. de secunde: "))
    rezolvare = RataDate(nr_biti, nr_secunde)
    print(rezolvare)
elif alegere == "timp de transfer":
    comprimat = input("Fisierul este comprimat?: ")
    comprimat_bool = False
    procent = 0
    if comprimat == "da":
        comprimat_bool = True
        procent = int(input("Procent: "))
    latime = int(input("Latimea fisierului: "))
    inaltime = int(input("Inaltimea fisierului: "))
    culoare_adv = input("Imaginea este colorata?: ")
    culoare_adv_bool = False
    if culoare_adv == "da":
        culoare_adv_bool = True
    nr_biti_transf = int(input("Nr. de biti transferati: "))
    unitatea_de_masura_a_bitilor = input("Unitatea de masura a bitilor / secunda: ")
    rezolvare = TimpTransfer(comprimat_bool, procent, latime, inaltime, culoare_adv_bool, nr_biti_transf,
                             unitatea_de_masura_a_bitilor)
    print(rezolvare)

