import requests
import json
import datetime
import time

def getData(country):
    key = 0
    while key != 1:
        try:
            result = requests.get(f"https://disease.sh/v2/countries/{country}")
        except Exception:
            print("\nİnternet bağlantısı sağlanamadı!!! Tekrar deneniyor....\n")
            time.sleep(6)
        else:
            print("\nApi ile bağlantı sağlandı...")
            print("\nVeriler karşı taraftan alındı...\n")
            key = 1
    result = json.loads(result.text)
    print("**************************************************************************\n\n")
    print(f"Toplam Vaka                  = {result['cases']}")
    print(f"Bugünkü Vaka                 = {result['todayCases']}")
    print(f"Aktif Vaka                   = {result['active']}")
    print(f"Toplam Ölüm                  = {result['deaths']}")
    print(f"Bugünkü Ölüm                 = {result['todayDeaths']}")
    print(f"Toplam İyileşen              = {result['recovered']}")
    print(f"Yoğun Bakımsaki Hasta Sayısı = {result['critical']}")
    print(f"Toplam test                  = {result['tests']}\n")
    print(f"\nSon Güncelleme      == {datetime.datetime.now()}")
    print("\n\n**************************************************************************\n")
    print("Veriler anlık olarak https://covid19.saglik.gov.tr/ üzerinden güncellenmektedir.\ngithub.com/msrexe")
print("\t\t\t\tCOVID-19 Tracker")
c = input("\nÜlke girin (Ör:Turkey,USA) : ")
getData(c)
time.sleep(45)
