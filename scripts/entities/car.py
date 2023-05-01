from scripts.constants import Const
from brownie import VehicleContract
from time import time
import numpy as np


class Car:
    def __init__(self, account):
        self.account = account
        self.contract = None
        self.location = []
        self.location_address = []
        self.location_id = []
        self.location_map = {}
        self.location_id_map = {}
        self.first_loc = True

    def deploy(self, price_feed_address):
        t1 = time()
        self.contract = VehicleContract.deploy(price_feed_address, { "from" : self.account })
        t2 = time()
        Const.logger.add_item("deploy", t2 - t1)
        Const.logger.add_item("car_gas_deploy", self.account.gas_used)
        # print(f"Contract deployed at {self.contract}")
        # print(f"{self.account.address} used {self.account.gas_used}")    

    def review_ipfs(self):
        addrs, strs = self.contract.getRequests.call()
        Const.logger.add_item("car_gas_id", self.account.gas_used)
        for i in range(len(addrs)):
            data_id = strs[i]
            print("CAR", "New Request", addrs[i], "for", data_id)
            data_val = bytes(self.location_id_map[data_id], "utf-8")
            t1 = time()
            data_val = Const.ttp.id_enc(data_val, addrs[i])
            t2 = time()
            Const.logger.add_item("id_enc", t2 - t1)
            t1 = time()
            data_adr = Const.ipfs.save(data_val)
            t2 = time()
            Const.logger.add_item("ipfs_save_id", t2 - t1)
            t1 = time()
            tx_receipt = self.contract.add_data_adr(data_id + "_i", data_adr, {
                "from" : self.account
            })
            tx_receipt.wait(1)
            t2 = time()
            Const.logger.add_item("add_adr_id", t2 - t1)
            Const.logger.add_item("car_gas_id", self.account.gas_used)

    def get_random_loc(self):
        # if self.first_loc:
        #     self.first_loc = False
        #     return "51*30'46.04\"N 0*05'30.62\"E"
        rdeg = np.random.randint(low=-180, high=180, size=2)
        rmin = np.random.randint(low=0, high=60, size=2)
        rsec = np.ceil(np.random.uniform(low=0, high=59.9, size=2) * 100) / 100.0
        rloc = "{}*{}'{}\"N{}*{}'{}\"E".format(rdeg[0], rmin[0], rsec[0], rdeg[1], rmin[1], rsec[1])
        return rloc
        
    def use_ipfs(self):
        rloc = self.get_random_loc()
        self.location.append(rloc)
        data_id = "location" + str(time())   
        policy1 = "(insurance and (inspecting or renewing) and (international or national) and (public or private))"
        policy2 = "(police and (searching or checking) and (local or national) and (permit or law))"
        policy3 = "(court and (investigating or enforcing) and (region or state) and (starting or ending))"
        policy4 = "(customs and (import or export) and (verifying or statistics) and (tax or tariff))"
        access_policy = "{} or {} or {} or {}".format(policy1, policy2, policy3, policy4)     
        t1 = time()
        data_val = Const.ttp.att_enc(str(self.location[-1]), access_policy)
        t2 = time()
        Const.logger.add_item("att_enc", t2 - t1)
        t1 = time()
        data_adr = Const.ipfs.save(data_val)
        t2 = time()
        Const.logger.add_item("ipfs_save_att", t2 - t1)
        print("Saved into IPFS. Hash is: {}".format(data_adr))
        self.location_map[data_adr] = str(self.location[-1])
        self.location_id_map[data_id] = str(self.location[-1])
        self.location_address.append(data_adr)
        t1 = time()
        tx_receipt = self.contract.add_data_adr(data_id, data_adr, {
            "from" : self.account
        })
        tx_receipt.wait(1)
        t2 = time()
        Const.logger.add_item("add_adr_att", t2 - t1)
        Const.logger.add_item("car_gas_att", self.account.gas_used)
        self.location_id.append(data_id)
        
    def read(self):
        print("CAR", f"ETH price is: {self.contract.getEthPrice.call()}")
        print("CAR", f"{self.account.address} used {self.account.gas_used} has {self.account.balance()}")
