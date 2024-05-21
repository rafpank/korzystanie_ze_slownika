definicje = {}

while(True):
  print("1: Dodaj nową definicję")
  print("2: Znajdź definicję")
  print("3: Usuń definicję")
  print("4: Zakończ program")

  wybor = input("Co chcesz zrobić? ")

  if wybor == "1":
    klucz = input("Podaj klucz, czyli słowo do zdefiniowania: ")
    definicja = input("Podaj definicję klucza: ")
    definicje[klucz] = definicja
    print("Definicja został dodana \n")
  elif wybor == "2":
    szukana_defincja = input("Podaj definicję którą chcesz odnaleźć: \n")
    if szukana_defincja in definicje:
      print(definicje[szukana_defincja])
    else:
      print(f"Nie znaleźono definicji: {szukana_defincja} \n")
  elif wybor == "3":
    usuwana_definicja = input("Podaj jaką definicję chcesz usunąć: ")
    if usuwana_definicja in definicje:
      del definicje[usuwana_definicja]
      print(f"Definicja {usuwana_definicja}, została usunięta \n")
    else:
      print(f"Nie znaleziono definicji: {usuwana_definicja} \n")
  elif wybor == "4":
    print("Koniec programu")
    break
  else:
    print("Podałeś nieprawidłową wartość")