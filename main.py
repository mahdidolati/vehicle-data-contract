from solcx import install_solc
from entities.car import Car
from entities.insurance import Insurance


def run():
    car_account_address = "0x49aA9BFBE623CcCfB8F39d337AA6e41694Fab55A"
    car_private_key = "0xc193c1f3d2ee522b8cd39fd7c4105009fa5b922e4532cd0e74b6ce9e319b9623"
    contract_path = "./sol_contracts/"
    contract_name = "SimpleStorageContract.sol"
    car = Car(car_account_address, car_private_key, contract_path, contract_name)
    car.init()
    car.use()

    insurance_account_address = "0x3574910dE3dB99Fdb6CF776A0C400F83FB8b2559"
    insurance_private_key = "0x1d459bc114e21596175bcecf9de4c3331a948d749dd5da6b70cbffcabd710b23"
    insurance1 = Insurance(insurance_account_address, insurance_private_key)
    insurance1.pay(car)
    insurance1.read(car)

    car.use()
    insurance1.read(car)
    

if __name__ == "__main__":
    install_solc('0.6.8')
    run()
        