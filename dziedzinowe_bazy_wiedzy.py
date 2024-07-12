import requests
import json
from prettytable import PrettyTable

class gus_dziedzinowe_bazy:

    #pobierz zmienne i zapisz w pliku TXT
    def pobierz_zmienne():
        api_url = "https://api-dbw.stat.gov.pl/api/1.1.0/variable/variable-section-periods?ile-na-stronie=5000&numer-strony=0&lang=pl"
        r = requests.get(api_url)
        if r.status_code == 200:
            zmienne = json.loads(r.content)
            wyniki = PrettyTable()
            wyniki.field_names = ['ID_ZMIENNA','NAZWA_ZMIENNEJ','ID_PRZEKRÓJ','NAZWA_PRZEKROJU','ID_OKRES']

            for result in zmienne["data"]:
                wyniki.add_row([result["id-zmienna"], result["nazwa-zmienna"], result["id-przekroj"], result["nazwa-przekroj"], result["id-okres"]])
    
        else:
            print('Połączenie z API nieudane')
        
        dane = wyniki.get_string()

        with open('../zmienne.txt', 'w') as plik:
            plik.write(dane)