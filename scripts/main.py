from scripts.entities.car import Car
from scripts.entities.insurance import Insurance
from scripts.cryptography.ttp_util import ThirdParty
from brownie import accounts
from scripts.constants import Const
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

    ttp = ThirdParty()
    ID = insurance.account.address
    data_adr = f"adr-{time()}"
    data_val = bytes(f"new data-{time()}", "utf-8")
    data_val = ttp.id_enc(ID, data_val)
    
    Const.db.save(data_adr, data_val)

    cipher_text = Const.db.retrieve(data_adr)
    data_val2 = ttp.id_dec(ID, cipher_text)
    print(data_val2)

    Const.db.close()


def main():
    run()
