from solcx import install_solc
from entities.car import Car

def run():
    # a public directory to map cars to contracts
    contract_db = dict()

    car_id = 0
    car = Car(car_id)
    car_id = car_id + 1
    car.init()
    contract_db[car.id] = car.abi
    car.use()
    car.read()

    # insurance1 = InsuranceCompany()
    # car_abi = contract_db[car.id]


if __name__ == "__main__":
    install_solc('0.6.0')
    run()
        