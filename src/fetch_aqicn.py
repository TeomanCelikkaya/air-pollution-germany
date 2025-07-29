import os
import requests
from dotenv import load_dotenv

load_dotenv() #laedt die .env datei

API_TOKEN = os.getenv("AQICN_API_TOKEN")

def get_city_aqi(city: str):
    """Holt Luftqualitaetsdaten fuer eine bestimmte Stadt"""
    if not API_TOKEN:
        raise ValueError("API_TOKEN not found. Make sure to set it via .env or environment variable.")
    
    url = f"https://api.waqi.info/feed/{city}/?token={API_TOKEN}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'ok':
            return data['data']
        else:
            print(f"API Error: {data['data']}")
    else:
        print(f"HTTP Error {response.status_code}")

    return None

# get_city_aqi nimmt einen Stadtnamen als String an und bildet damit und dem API_Token eine URL.
# Mit der request funktion rufen wir diese URL dann auf und pruefen daraufhin die response 200 (verbindung ist erfolgreich)
# Ich speichere die response als Python dictionary in der variable data und pruefe auf den Status 'ok' (moeglich sind 'ok' oder 'Error') und geben die daten bei ok zuruck

if __name__ =="__main__":
    result = get_city_aqi("munich")
    if result:
        print(f"PM2.5 in Munich: {result['iaqi'].get('pm25', {}).get('v', 'n/a')} µg/m³")

    print("Verfügbare Messwerte:")
    for key, value in result['iaqi'].items():
        print(f"  {key.upper()}: {value['v']} µg/m³")