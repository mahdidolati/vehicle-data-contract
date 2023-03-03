from solcx import install_solc
from entities.car import Car
from entities.insurance import Insurance


def run():
    car_account_address = "0xEBf52D1635488ebdec786350caC943FcD4aa8395"
    car_private_key = "0xfe5121b16d09c5d3ae2745cfbc57082c33efdbc3a2daaf0e8984810d2e7af6e0"
    contract_path = "./sol_contracts/"
    contract_name = "SimpleStorageContract.sol"
    car = Car(car_account_address, car_private_key, contract_path, contract_name)
    car.init()
    car.use()

    insurance1 = Insurance()
    insurance1.read(car)

    car.use()
    insurance1.read(car)
    

if __name__ == "__main__":
    install_solc('0.6.0')
    run()
        