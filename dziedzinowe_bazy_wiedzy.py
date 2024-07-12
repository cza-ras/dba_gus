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

        wyniki.to_csv('../Projects/dbw_gus/dane/zmienne.csv', index=False)