
def listy():
# TODO listy : wprowdzenie tablicy posortowanie rosnąco malejąco wyjście z listy i wyjście z programu
    listy_decyzja  = input ("\nPodaj co chcesz zrobić z tą listą: \nrosnaco - sortuj rosnaco,\nmalejaco - sortuj malejeco,\nw - wyjscie do menu,\nquit - wyjscie z programu\n ")
    if listy_decyzja == 'w':
        menu()
    elif listy_decyzja == 'quit':
        quit()
    lista = input('\nWprowadź listę oddzielając kolejne liczby spacją')
    lista = lista.split(' ')
    for i in range(0, len(lista)):
        lista[i] = int(lista[i])
    if listy_decyzja == 'malejaco':
        print(sorted(lista, reverse=True))

    elif listy_decyzja == 'rosnaco':
        print(sorted(lista))

    else:
        print('\nNie ma takiego warunku')
def napisy ():
    # TODO Napisy : wprowadzenie napisu konwersja na małe litery duże litery porównanie dwóch napisów wyjście z napisów wyjscie z programua
        napisy_decyzja = input(
            '\n male - konweruja napis na małe litery,\n duze - konwertuja na duze litery,\n porownaj - porownuje dwa napisy,\n w - wyjście do menu głównego,\n quit  - wyjscie z programu')

        if napisy_decyzja == 'w':
            menu()
        elif napisy_decyzja == 'quit':
            quit()
        napis = input('\nPodaj napis')
        if napisy_decyzja == 'male':
            napis = napis.lower()
            print("\nNapis z małymi literami to " + napis)
            napisy()
        elif napisy_decyzja == 'duze':
            napis = napis.upper()
            print("\nNapis z samymi duzymi literami to " +napis)
            napisy()
        elif napisy_decyzja == 'porownaj':
            napis_porownanie = input('podaj drugi napis do porównania\n')
            if (napis==napis_porownanie):
                print ("Napisy są te same")
            else:
                print ("Napisy nie są takie same")
            napisy()

        else:
            print('Nie ma takiego warunku')

def menu():
    # TODO menu: wybór opcji napisy listy wyjście z programu
    wprowadzone = input(
        'listy - przejście do menu listy,\nnapisy - przejscie do menu napisy,\nw - wyjscie z programu\n')
    if wprowadzone == 'listy':
        listy()
    if wprowadzone == 'napisy':
        napisy()
    if wprowadzone == 'w':
        quit()
    else:
        print("\nNie ma takiej opcji ")
        menu()

menu()
