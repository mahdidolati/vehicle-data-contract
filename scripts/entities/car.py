from scripts.constants import Const
from brownie import SimpleStorage
from time import time


class Car:
    def __init__(self, account):
        self.account = account
        self.contract = None
        self.contract_address = None
        self.location = [0]
        self.speed = [0]
        self.milage = 0

    def deploy(self, price_feed_address):
        self.contract = SimpleStorage.deploy(price_feed_address, { "from" : self.account })
        ret = self.contract.getEthPrice.call()
        print("----", ret)
        # print(f"Contract deployed at {self.contract}")
        # print(f"{self.account.address} used {self.account.gas_used}")        

    def use(self):
        self.location.append((self.location[-1] + 1) % 20)
        self.speed.append((self.speed[-1] + 1) % 100)
        self.milage = self.milage + 1

        tx_receipt = self.contract.store(self.milage, { "from" : self.account }) 
        tx_receipt.wait(1)
        print(f"{self.account.address} used {self.account.gas_used}")        
        
    def read(self):
        retrieved_number = self.contract.retrieve.call() 
        print(f"Number Retrieved : {retrieved_number}")
        print(f"Account 0: {self.account.address} used {self.account.gas_used}")
        print(f"Account 0: {self.account.address} balance {self.account.balance()}")