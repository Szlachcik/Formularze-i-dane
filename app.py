import csv

with open('currency.csv') as plikCSV:
    czytnikCSV = csv.reader(plikCSV, delimiter = ';')

    for wiersz in czytnikCSV:
        print(wiersz)



    def przeliczWaluty():
        # Pobranie informacji co użytkownik chce przeliczyć i w jakiej ilości
        podajWalute = input("Wpisz kod jednej z walut którą chciałbyś zakupić:\n")
        ilosc = input("Ile chciałbyś zakupić " + podajWalute + "?\n")

        # program przelicza wybraną walutę na PLN
        if podajWalute == "USD":
            wynik = int(ilosc) * 4.0963
            print(f'Będzie Cię to kosztować %0.2f' % wynik + " zł")
        elif podajWalute == "AUD":
            wynik = int(ilosc) * 2.9773
            print(f'Będzie Cię to kosztować %0.2f' % wynik + " zł")
        elif podajWalute == "CAD":
            wynik = int(ilosc) * 3.2051
            print(f'Będzie Cię to kosztować %0.2f' % wynik + " zł")
        elif podajWalute == "EUR":
            wynik = int(ilosc) * 4.6427
            print(f'Będzie Cię to kosztować %0.2f' % wynik + " zł")
        elif podajWalute == "HUF":
            wynik = int(ilosc) * 0.012531
            print(f'Będzie Cię to kosztować %0.2f' % wynik + " zł")
        elif podajWalute == "CHF":
            wynik = int(ilosc) * 4.4833
            print(f'Będzie Cię to kosztować %0.2f' % wynik + " zł")
        elif podajWalute == "GBP":
            wynik = int(ilosc) * 5.5342
            print(f'Będzie Cię to kosztować %0.2f' % wynik + " zł")
        elif podajWalute == "JPY":
            wynik = int(ilosc) * 0.035592
            print(f'Będzie Cię to kosztować %0.2f' % wynik + " zł")
        elif podajWalute == "CZK":
            wynik = int(ilosc) * 0.1863
            print(f'Będzie Cię to kosztować %0.2f' % wynik + " zł")
        elif podajWalute == "DKK":
            wynik = int(ilosc) * 0.6243
            print(f'Będzie Cię to kosztować %0.2f' % wynik + " zł")
        elif podajWalute == "NOK":
            wynik = int(ilosc) * 0.4654
            print(f'Będzie Cię to kosztować %0.2f' % wynik + " zł")
        elif podajWalute == "SEK":
            wynik = int(ilosc) * 0.4535
            print(f'Będzie Cię to kosztować %0.2f' % wynik + " zł")
        elif podajWalute == "XDR":
            wynik = int(ilosc) * 5.7452
            print(f'Będzie Cię to kosztować %0.2f' % wynik + " zł")
        else:
            print("Error: Spróbuj jeszcze raz.")


    przeliczWaluty()