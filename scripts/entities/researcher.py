from scripts.constants import Const
from brownie import Contract


class Researcher:
    def __init__(self, account):
        self.account = account

    def read(self, car, item_address):
        cipher_text = Const.db.retrieve(self, car, item_address)
        r2 = Const.ttp.id_dec(cipher_text, self.account.address)
        print("RESEARCHER", f"The data received from db is {r2}")

    def request(self, car, item_address):
        contract = Contract(car.contract.address)
        tx_receipt = contract.requestAccess(item_address, {
            "from": self.account
        })
        tx_receipt.wait(1)
        print("RESEARCHER", f"{self.account.address} used {self.account.gas_used}")

    def deposit(self, car):
        contract = Contract(car.contract.address)
        fee = contract.getFee.call()
        print("RESEARCHER", f"Fee of accessing data is: {fee}")
        tx_receipt = contract.deposit({    
            "from": self.account,
            "value": fee
        })
        tx_receipt.wait(1)
        print("RESEARCHER", f"{self.account.address} used {self.account.gas_used}")   
