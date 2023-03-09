from scripts.entities.car import Car
from scripts.entities.insurance import Insurance
from brownie import accounts


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
    

def main():
    run()
