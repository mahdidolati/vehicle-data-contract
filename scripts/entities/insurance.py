import os
import json
from scripts.constants import Const
from brownie import Contract


class Insurance:
    def __init__(self, account):
        self.account = account

    def get_nonce(self):
        n = self.nonce
        self.nonce = self.nonce + 1
        return n

    def read(self, car):
        contract = Contract(car.contract.address)
        retrieved_number = contract.retrieve.call() 
        print(f"Number Retrieved : {retrieved_number}")

    def pay(self, car):
        contract = Contract(car.contract.address)
        tx_receipt = contract.fund({    
            "from": self.account,
            "value": 50735 * 500000000000
        })
        tx_receipt.wait(1)