# TODO menu z wyborem listy napisy wyjście

wprowadzone  = input ('listy - przejście do menu listy,\nnapisy - przejscie do menu napisy,\nw - wyjscie z programu\n')

while True :
    if wprowadzone == 'w':
        break
    elif wprowadzone == 'listy' :
# TODO listy : wprowdzenie tablicy posortowanie rosnąco malejąco wyjście z listy i wyjście z programu
        listy_decyzja = input('\nmalejaco - sortuje tab malejaco,\nrosnaco - sortuje tab rosnąco,\nw - wyjście do menu głównego\n')
        lista = input ('Wprowadź listę odcielając kolejne liczby spacją')
        lista =int (lista.split(' '))
        konwertuj = int (lista[2])
        print (konwertuj)
        while True :
            if listy_decyzja == 'malejaco':
                print (sorted(lista , reverse=True))
                break
            elif  listy_decyzja == 'rosnaco':
                print(sorted(lista))
                break
            elif listy_decyzja == 'w':
                break
            else: print('\nNie ma takiego warunku')
    elif wprowadzone == 'napisy':
# TODO Napisy : wprowadzenie napisu konwersja na małe litery duże litery porównanie dwóch napisów wyjście z napisów wyjscie z programu
        while True :
            napisy_decyzja = input ('\nmale - konweruja napis na małe litery,\n duze - konwertuja na duze litery,\n porownaj - porownuje dwa napisy ,\n w - wyjście do menu głównego\n')
            napis = input('podaj napis')
            if napisy_decyzja == 'male':
                break
            elif napisy_decyzja == 'duze':
                break
            elif napisy_decyzja == 'porownaj':
                napis_porownanie = input ('podaj drugi napis do porównania\n')
                break ;
            elif napisy_decyzja == 'w':
                break ;
            else:
                print('Nie ma takiego warunku')
    else:
            print('\nNie ma takiego warunku')