import random
# 1. Sukurkite Funkciją kuri priima du kintamuosius. Juos susumuoja ir atspausdina.
# def susumuoti_ir_atspausdinti(a, b):
#     suma = a + b
#     print("Suma: ", suma)
# susumuoti_ir_atspausdinti(1, 2)
# print(susumuoti_ir_atspausdinti(1, 2))

# 2. Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina reikšmę. Reikšmė yra : 9.8596; Gautą reikšmę atspausdinkite.
# def PISq():
#     return 9.8596
# rezultatas = PISq()
# print(rezultatas)

# 3. Sukurkite Funkciją kuri priima du kintamuosius. Funkcija gražina skaičių sandaugą.; Gautą reikšmę atspausdinkite.
# def sandauga(a, b):
#     return a * b
# rezultatas = sandauga(1, 2)
# print(rezultatas)

# 4.  Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.
def spausdinti_masyva(arr):
    for i in arr:
        print(i, end=" ")
arr = [1,2,3,4,5]
spausdinti_masyva(arr)

# 5. Sukurkite Funkciją kuri priima du kintamuosius, min ir max reikšmėms nustatyti ir sugeneruoja random int skaičių ir jį gražintų.

def generuoti_atsitiktini_skaiciu(min_reiksme, max_reiksme):
    return random.randint(min_reiksme, max_reiksme)
rezultatas = generuoti_atsitiktini_skaiciu(1, 10)
print(f"Atsitiktinis skaičius: {rezultatas}")