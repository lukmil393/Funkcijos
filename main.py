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
# def generate_rnd_str(length):
#   symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
#   text = ""
#   for i in range(length):
#     text += symbols[random.randint(0,len(symbols) -1)]
#   return text
#
# def spausdinti_su_apgaubtais_skaiciais(text):
#   i = 0
#   while i < len(text):
#     if text [i].isdigit():
#       skaiciu_grupe = text[i]
#       i += 1
#       while i < len(text) and text[i].isdigit():
#         skaiciu_grupe += text[i]
#         i += 1
#       print(f"[{skaiciu_grupe}]")
#     else:
#       print(text[i])
#       i += 1
# atsitiktinis_tekstas = generate_rnd_str(10)
# print("Sugeneruotas tekstas:", atsitiktinis_tekstas)
# print("Simboliai stulpeliu (su sugrupuotais skaičiais):")
# spausdinti_su_apgaubtais_skaiciais(atsitiktinis_tekstas)

# 3.  Parašykite funkciją, kuri skaičiuotų, ir gražintų iš kiek sveikų skaičių jos argumentas dalijasi be liekanos
# (išskyrus vienetą ir patį save). Pvz padavus 10 turi grąžinti 2,  o padavus 20 gražintų 4.
# def dalikliu_kiekis(num):
#   kiekis = 0
#   for i in range(2, num):
#     if num % i == 0:
#       kiekis += 1
#   return kiekis
# print(dalikliu_kiekis(10))
# print(dalikliu_kiekis(20))

# 4. Sugeneruokite masyvą iš 100 elementų, kurio reikšmės atsitiktiniai skaičiai nuo 33 iki 77.
# Išrūšiuokite masyvą pagal daliklių be liekanos kiekį mažėjimo tvarka, panaudodami trečio uždavinio funkciją.

# masyvas = [random.randint(33, 77) for _ in range(100)]
# rusiuotas = sorted(masyvas, key=dalikliu_kiekis, reverse=True)
# print("Originalus masyvas:")
# print(masyvas)
# print ("Išrūšiuotas pagal daliklių kiekį mažėjimo tvarka):")
# print(rusiuotas)

# 11. Sukurkite Funkciją kuri priimtų sakinį, jį užkoduotų ir grąžintų.
# Kodavimas - sakinį apsukame iš kitos pusės. Pvz “Naglis” turi gautis “silgaN”.

# def koduotas_sakinys(sakinys):
#     apsuktas = sakinys[::-1]
#     return apsuktas
# sakinys = "Lukas"
# kodas = koduotas_sakinys(sakinys)
# print(kodas)


# 12. Sukurti funkciją, kuri apsuka tik žodžius. “Labas rytas” -> “sabal satyr” ir atspausdina rezultatą
# def apsukti_zodzius(sakinys):
#   zodziai = sakinys.split()
#   apsukti = [zodis[::-1] for zodis in zodziai]
#   return " ".join(apsukti)
# sakinys = "labas rytas"
# rezultatas = apsukti_zodzius(sakinys)
# print(rezultatas)

# 13.Sukurkite funkciją, kuri priimtų masyvą ir atspausdintų tik tuos elementus kurie yra skaičiai.
# def spausdinti_tik_skaicius(masyvas):
#   for elementas in masyvas:
#     if isinstance(elementas, int):
#       print(elementas)
# duomenys = [10, "labas", 5, 8, 55, "medis"]
# spausdinti_tik_skaicius(duomenys)

# 14. Sukurkite funkciją, kuri iš paduoto masyvo atspausdina tik sveikuosius skaičius.
# (jei pavyks, patobulinkite, kad funkcija priimtų antrą parametrą
# True/False kuris nuspręstų ar spausdins tik sveikuosius skaičius ar skaičius su kableliu.

# def spausdinti_skaicius(masyvas, tik_sveikieji=True):
#   for elementas in masyvas:
#     if tik_sveikieji:
#       if isinstance(elementas, int) and not isinstance(elementas, bool):
#         print(elementas)
#     else:
#       if isinstance(elementas, float):
#         print(elementas)
# duomenys = 10, 2.54, 42, True, -5, 0, False, "kebabas, 8.88"
# print("Tik sveikieji skaiciai:")
# spausdinti_skaicius(duomenys, tik_sveikieji=True)
# print("\nTik skaiciai su kableliu:")
# spausdinti_skaicius(duomenys, tik_sveikieji=False)

# 15. Sukurkite funkciją word_count kuri priimtų textą ir gražintų kiek jame yra žodžių.
# def word_count(text):
#   words = text.split()
#   return len(words)
# tekstas = "Siandien yra labai labai grazi diena"
# print("Zodziu skaicius:", word_count(tekstas))

# 16. Sukurkite funkciją kuri priima du parametrus. Skaičių masyvą ir boolean.
# Funkcija gražina prafiltruotą masyvą. Kai antras parametras True/tik poriniais skaičiais, False/tik neporiniais skaičiais.
# def filtruoti_masyva(masyvas, poriniai=True):
#   if poriniai:
#     return [x for x in masyvas if x % 2 == 0]
#   else:
#     return [x for x in masyvas if x % 2 != 0]
# masyvas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#
# print(filtruoti_masyva(masyvas, True))
# print(filtruoti_masyva(masyvas, False))

# 17. Sukurkite funkciją number_is_prime. Funkcija priima skaičių, gražina True/False ar skaičius pirminis.

def number_is_prime(number):
  if number < 2:
        return False
  for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
      return False
    else:
      return True
skaicius = random.randint(1, 100)
print(f"Skaicius: {skaicius}")
print(number_is_prime(skaicius))