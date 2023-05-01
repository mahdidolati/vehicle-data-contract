from scripts.entities.car import Car
from scripts.entities.insurance import Insurance
from scripts.entities.researcher import Researcher
from brownie import accounts, MockV3Aggregator
from scripts.constants import Const
from time import time
from scripts.util.helpful_scripts import get_account, deploy_mocks


def run():
    deploy_mocks()
    price_feed_address = MockV3Aggregator[-1].address

    car_account = get_account(0)
    car = Car(car_account)
    researcher_account = get_account(3)
    researcher = Researcher(researcher_account)
    insurance_account = get_account(1)
    insurance = Insurance(insurance_account)

    car.deploy(price_feed_address)

    car.use_ipfs()
    car.use_ipfs()    
    insurance.read_ipfs(car, car.location_id[-1])
    print(f"Car: {car.account.balance()} -- Insurance: {insurance.account.balance()}")

    car.use_ipfs()
    researcher.request_and_pay(car, car.location_id[-1])
    car.review_ipfs()
    researcher.read_ipfs(car, car.location_id[-1] + "_i")
    print(f"Car: {car.account.balance()} -- Researcher: {researcher.account.balance()}")

    car.use_ipfs()
    researcher.request_and_pay(car, car.location_id[-1])
    car.review_ipfs()
    researcher.read_ipfs(car, car.location_id[-1] + "_i")
    print(f"Car: {car.account.balance()} -- Researcher: {researcher.account.balance()}")

    Const.logger.print()
    Const.db.close()


def main():
    run()
