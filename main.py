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
# def spausdinti_masyva(arr):
#     for i in arr:
#         print(i, end=" ")
# arr = [1,2,3,4,5]
# spausdinti_masyva(arr)

# 5. Sukurkite Funkciją kuri priima du kintamuosius, min ir max reikšmėms nustatyti ir sugeneruoja random int skaičių ir jį gražintų.

# def generuoti_atsitiktini_skaiciu(min_reiksme, max_reiksme):
#     return random.randint(min_reiksme, max_reiksme)
# rezultatas = generuoti_atsitiktini_skaiciu(1, 10)
# print(f"Atsitiktinis skaičius: {rezultatas}")

# 6. Sukurkite Funkciją kuri sugeneruotų random skaičių masyvą ir jį gražintų.
# Funkcija priima tris kintamuosius, min, max ir length reikšmėms nustatyti.
# 7. Sukurkite Funkciją kuri panaudotų 6toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį), susumuotų ir gražintų reikšmę.
# 8. Sukurkite Funkciją kuri priimtų 6toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį (double).
# def sugeneruoti_random_skaiciu_masyva(min_value, max_value, length):
#     masyvas = [random.randint(min_value, max_value) for _ in range(length)]
#     return masyvas
# random_skaiciai = sugeneruoti_random_skaiciu_masyva(10, 30, 5)
# print(random_skaiciai)
#
# def masyvo_suma(masyvas):
#     suma = sum(masyvas)
#     return suma
# print(masyvo_suma(random_skaiciai))
#
# def masyvo_vidurkis(masyvas):
#     if len(masyvas) == 0:
#         return 0
#     return sum(masyvas) / len(masyvas)
# print(masyvo_vidurkis(random_skaiciai))

# 9. Sukurkite Funkciją kuri priimtų du skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis.
# Pirmas skaičius- išoriniam ciklui, antras vidiniam.

# def staciakampis(eiluciu_skaicius, zenklu_skaicius):
#     for i in range(eiluciu_skaicius):
#         for j in range(zenklu_skaicius):
#             print("*", end="")
#         print()
# staciakampis(4, 16)

# 10. Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių(simbolių) ir tarpų.
# Sakinys - “Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį) (simboliu yra 23, tarpu yra 3)

# def analizuojam_sakini(sakinys):
#     simboliai = 0
#     tarpai = 0
#     for simbolis in sakinys:
#         if simbolis == " ":
#             tarpai += 1
#         else:
#             simboliai += 1
#     print(f"Simbolių yra: {simboliai}")
#     print(f"Tarpų yra: {tarpai}")
# analizuojam_sakini("Šiandien labai graži diena")

# 11. Sukurkite Funkciją kuri priimtų sakinį, jį užkoduotų ir grąžintų.
# Kodavimas - sakinį apsukame iš kitos pusės. Pvz “Naglis” turi gautis “silgaN”.

# def koduotas_sakinys(sakinys):
#     apsuktas = sakinys[::-1]
#     return apsuktas
# sakinys = "Lukas"
# kodas = koduotas_sakinys(sakinys)
# print(kodas)

# -------------------------------- SUNKESNI -----------------------------------------
# 1. Parašykite funkciją, kurios argumentas būtų tekstas, kuris būtų atspausdinamas konsolėje pridedant “---” pradžioje ir gale.
# PVZ (---labas---)
# def blablabla(tekstas):
#     print(f"---{tekstas}---")
# blablabla("Test")

# 2. Sugeneruokite atsitiktinį stringą iš raidžių ir skaičių (10 simbolių). Atspausdinkite simbolius stulpeliu.
# Jei tai skaičius apgaubkite “ [ 7 ]”. Jei skaičiai eina keli iš eilės, apgaubkite juos kartu. [75]
def generate_rnd_str(length):
  symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
  text = ""
  for i in range(length):
    text += symbols[random.randint(0,len(symbols) -1)]
  return text

def spausdinti_stulpeliu(tekstas):
  for simbolis in tekstas:
    print(simbolis)

atsitiktinis_tekstas = generate_rnd_str(10)
print("Sugeneruotas tekstas: ", atsitiktinis_tekstas)
print("Simboliai stulpeliu:")
spausdinti_stulpeliu(atsitiktinis_tekstas)

def spausdinti_su_apgaubtais_skaiciais(text):
  for simbolis in text:
    if simbolis.isdigit():
      print(f"[{simbolis}]")
    else:
      print(simbolis)



