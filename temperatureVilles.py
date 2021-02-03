# coding: UTF-8
"""
Script: pythonProject6/temperatureVilles.py
Création: nthiers, le 15/01/2021
"""


# Imports
import time
import requests
import mysql.connector

# Fonctions
def get_temperature(ville):
    url="http://api.openweathermap.org/data/2.5/weather?q="+ville+",fr&units=metric&lang=fr&appid=0a73790ec47f53b9e1f2e33088a0f7d0"
    return float(requests.get(url).json()['main']['temp'])

def get_pression(ville):
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + ville + ",fr&units=metric&lang=fr&appid=0a73790ec47f53b9e1f2e33088a0f7d0"
    return float(requests.get(url).json()['main']['pressure'])

def set_bdd(ville, temperature, pression):
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='bdd_temperaturevilles')
    cursor = cnx.cursor()
    update_val = ("UPDATE temperaturevilles SET temperature = (%s),pression = (%s) WHERE ville = (%s)")
    data = (temperature, pression, ville)
    cursor.execute(update_val, data)
    cnx.commit()
    cursor.close()
    cnx.close()

# Programme principal
def main():
    List_ville = ["grenoble", "lyon", "meylan", "apprieu"]
    while True:
        for element in List_ville:
            print(element, ":", get_temperature(element), "°C avec une pression de ", get_pression(element))
            set_bdd(element, get_temperature(element), get_pression(element))
        print(f'Températures misent à jour')
        time.sleep(300)


if __name__ == '__main__':
    main()
# Fin
