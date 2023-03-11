from scripts.entities.car import Car
from scripts.entities.insurance import Insurance
from brownie import accounts
from scripts.constants import Const
from time import time


def run():
    # car_account = accounts[0]
    # car = Car(car_account)
    # car.deploy()
    # car.use()
    
    # insurance_account = accounts[1]
    # insurance = Insurance(insurance_account)
    # insurance.read(car)
    # insurance.pay(car)

    # print(f"Car: {car.account.balance()} -- Insurance: {insurance.account.balance()}")

    # ID = insurance.account.address
    # data_adr = f"adr-{time()}"
    # data_val = bytes(f"new data-{time()}", "utf-8")
    # data_val = Const.ttp.id_enc(data_val, ID)
    
    # Const.db.save(data_adr, data_val)

    # cipher_text = Const.db.retrieve(data_adr)
    # data_val2 = Const.ttp.id_dec(cipher_text, ID)
    # print(data_val2)

    # Const.db.close()

    r = Const.ttp.att_enc("hello", "system_admin or market_group")
    r2 = Const.ttp.att_dec(r, "system_admin")
    print(r2)
    r3 = Const.ttp.att_dec(r, "pashm")
    print(r3)


def main():
    run()
