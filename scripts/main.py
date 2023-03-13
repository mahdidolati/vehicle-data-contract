from scripts.entities.car import Car
from scripts.entities.insurance import Insurance
from brownie import accounts, MockV3Aggregator
from scripts.constants import Const
from time import time
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def run():
    deploy_mocks()
    price_feed_address = MockV3Aggregator[-1].address

    car_account = get_account(0)
    car = Car(car_account)
    car.deploy(price_feed_address)
    car.use()
    
    insurance_account = get_account(1)
    insurance = Insurance(insurance_account)
    insurance.read(car)
    insurance.pay(car)

    print(f"Car: {car.account.balance()} -- Insurance: {insurance.account.balance()}")

    # ID = insurance.account.address
    # data_adr = f"adr-{time()}"
    # data_val = bytes(f"new data-{time()}", "utf-8")
    # data_val = Const.ttp.id_enc(data_val, ID)
    
    # Const.db.save(data_adr, data_val)

    # cipher_text = Const.db.retrieve(data_adr)
    # data_val2 = Const.ttp.id_dec(cipher_text, ID)
    # print(data_val2)

    # Const.db.close()

    data_val = Const.ttp.att_enc("hello", "system_admin or market_group")
    data_adr = f"adr-{time()}"
    Const.db.save(data_adr, data_val)
    
    cipher_text = Const.db.retrieve(data_adr)
    r2 = Const.ttp.att_dec(cipher_text, "system_admin")
    print(r2)
    
    r3 = Const.ttp.att_dec(cipher_text, "developer")
    print(r3)

    Const.db.close()


def main():
    run()
