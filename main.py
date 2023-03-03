from solcx import install_solc
from entities.car import Car
from entities.insurance import Insurance


def run():
    car_id = 0
    car = Car(car_id)
    car_id = car_id + 1
    car.init("./sol_contracts/", "SimpleStorageContract.sol")
    car.use()

    insurance1 = Insurance()
    insurance1.read("./sol_contracts/", "SimpleStorageContract.sol", car.contract_address)

    car.use()
    insurance1.read("./sol_contracts/", "SimpleStorageContract.sol", car.contract_address)
    

if __name__ == "__main__":
    install_solc('0.6.0')
    run()
        