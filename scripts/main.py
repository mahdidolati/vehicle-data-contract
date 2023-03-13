from scripts.entities.car import Car
from scripts.entities.insurance import Insurance
from scripts.entities.researcher import Researcher
from brownie import accounts, MockV3Aggregator
from scripts.constants import Const
from time import time
from scripts.helpful_scripts import get_account, deploy_mocks


def run():
    deploy_mocks()
    price_feed_address = MockV3Aggregator[-1].address

    car_account = get_account(0)
    car = Car(car_account)
    car.deploy(price_feed_address)
    car.use()
    
    insurance_account = get_account(1)
    insurance = Insurance(insurance_account)
    insurance.deposit(car)
    insurance.read(car, car.location_address[-1])

    print(f"Car: {car.account.balance()} -- Insurance: {insurance.account.balance()}")

    car.use()

    researcher_account = get_account(3)
    researcher = Researcher(researcher_account)
    researcher.request(car, car.location_address[-1])

    car.review()
    researcher.deposit(car)
    researcher.read(car, car.location_address[-1] + "_i")

    Const.db.close()


def main():
    run()
