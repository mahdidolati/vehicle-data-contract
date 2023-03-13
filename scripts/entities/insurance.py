from scripts.constants import Const
from brownie import Contract


class Insurance:
    def __init__(self, account):
        self.account = account

    def read(self, car, item_address):
        cipher_text = Const.db.retrieve(self, car, item_address)
        r2 = Const.ttp.att_dec(cipher_text, "insurance")
        print(f"The data received from db is {r2}")

    def deposit(self, car):
        contract = Contract(car.contract.address)
        fee = contract.getFee.call()
        print(f"Fee of accessing data is: {fee}")
        tx_receipt = contract.deposit({    
            "from": self.account,
            "value": fee
        })
        tx_receipt.wait(1)
        print(f"{self.account.address} used {self.account.gas_used}")   
