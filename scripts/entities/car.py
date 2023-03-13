from scripts.constants import Const
from brownie import VehicleContract
from time import time


class Car:
    def __init__(self, account):
        self.account = account
        self.contract = None
        self.location = 0
        self.location_address = []

    def deploy(self, price_feed_address):
        self.contract = VehicleContract.deploy(price_feed_address, { "from" : self.account })
        # print(f"Contract deployed at {self.contract}")
        # print(f"{self.account.address} used {self.account.gas_used}")        

    def use(self):
        self.location = (self.location + 1) % 20
        self.location_address.append("location" + str(time()))

        data_adr = self.location_address[-1]
        data_val = Const.ttp.att_enc(str(self.location), "police or insurance")
        Const.db.save(data_adr, data_val)        
        
    def read(self):
        print(f"ETH price is: {self.contract.getEthPrice.call()}")
        print(f"{self.account.address} used {self.account.gas_used} has {self.account.balance()}")
