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

def set_bdd(ville, temperature):
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='bdd_temperaturevilles')
    cursor = cnx.cursor()
    update_val = ("UPDATE temperaturevilles SET temperature = (%s) WHERE ville = (%s)")
    data = (temperature, ville)
    cursor.execute(update_val, data)
    cnx.commit()
    cursor.close()
    cnx.close()

# Programme principal
def main():
    List_ville = ["grenoble", "lyon", "meylan", "apprieu"]
    while True:
        for element in List_ville:
            print(element, ":", get_temperature(element))
            set_bdd(element, get_temperature(element))
        print(f'Températures misent à jour')
        time.sleep(300)


if __name__ == '__main__':
    main()
# Fin
