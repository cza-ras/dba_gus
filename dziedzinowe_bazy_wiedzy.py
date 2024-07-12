import requests
import json
import pandas as pd

class gus_dziedzinowe_bazy:

    #pobierz zmienne i zapisz w pliku CSV
    def pobierz_zmienne():
        api_url = "https://api-dbw.stat.gov.pl/api/1.1.0/variable/variable-section-periods?ile-na-stronie=5000&numer-strony=0&lang=pl"
        r = requests.get(api_url)
        if r.status_code == 200:
            zmienne = json.loads(r.content)
            wyniki = pd.DataFrame(zmienne['data'])    
        else:
            print('Połączenie z API nieudane')

        wyniki.to_csv('zmienne.csv', index=False)

    #pobierz dane dla zmiennj i zapisz w pliku CSV
    def pobierz_dane(zmienna, przekroj, rok, okres):
        api_url = f"https://api-dbw.stat.gov.pl/api/1.1.0/variable/variable-data-section?id-zmienna={zmienna}&id-przekroj={przekroj}&id-rok={rok}&id-okres={okres}&ile-na-stronie=5000"
        r = requests.get(api_url)
        if r.status_code == 200:
            zmienne = json.loads(r.content)
            wyniki = pd.DataFrame(zmienne['data'])    
        else:
            print('Połączenie z API nieudane')

        wyniki.to_csv('dane.csv', index=False)