from scripts.entities.car import Car
from scripts.entities.insurance import Insurance
from scripts.cryptography.example_1 import ThirdParty
from brownie import accounts
import sqlite3
import pickle
import json
from time import time


def run():
    car_account = accounts[0]
    car = Car(car_account)
    car.deploy()
    car.use()
    
    insurance_account = accounts[1]
    insurance = Insurance(insurance_account)
    insurance.read(car)
    insurance.pay(car)

    print(f"Car: {car.account.balance()} -- Insurance: {insurance.account.balance()}")

    sqliteConnection = sqlite3.connect("database.db")
    cursor = sqliteConnection.cursor()
    print(f"Database created and Suncessfully Connected to SQLite")

    ttp = ThirdParty()
    ID = "bob@mail.com"
    data_adr = f"hello-{time()}"
    data_val = b"new data"
    data_val = ttp.id_enc(ID, data_val)
    insert_query = """INSERT INTO vehicle_data (DATA_ADR, DATA_VAL) VALUES (?, ?)"""
    count = cursor.execute(insert_query, (data_adr, data_val,))
    sqliteConnection.commit()
    print(f"Inserted {count.rowcount}.")

    select_query = """SELECT * FROM vehicle_data WHERE DATA_ADR = ? LIMIt 1"""
    cursor.execute(select_query, (data_adr,))
    rows = cursor.fetchall()
    if len(rows) > 0:
        cipher_text = rows[0][1]
        data_val2 = ttp.id_dec(ID, cipher_text)
        print(data_val2)

    cursor.close()
    sqliteConnection.close()


def main():
    run()
