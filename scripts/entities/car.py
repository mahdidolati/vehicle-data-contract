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
        Const.logger.add_item("Case1", "DeployTime", t2 - t1)
        Const.logger.add_item("Case1", "DeployGas", self.account.gas_used)
        # print(f"Contract deployed at {self.contract}")
        # print(f"{self.account.address} used {self.account.gas_used}")    

    def review_ipfs(self):
        addrs, strs = self.contract.getRequests.call()
        Const.logger.add_item("Case2", "GetReqGas", self.account.gas_used)
        for i in range(len(addrs)):
            data_id = strs[i]
            print("CAR", "New Request", addrs[i], "for", data_id)
            data_val = bytes(self.location_id_map[data_id], "utf-8")
            t1 = time()
            data_val = Const.ttp.id_enc(data_val, addrs[i])
            t2 = time()
            Const.logger.add_item("Case2", "EncTime", t2 - t1)
            t1 = time()
            data_adr = Const.ipfs.save(data_val)
            t2 = time()
            Const.logger.add_item("Case2", "IpfsSaveTime", t2 - t1)
            t1 = time()
            tx_receipt = self.contract.add_data_adr(data_id + "_i", data_adr, {
                "from" : self.account
            })
            tx_receipt.wait(1)
            t2 = time()
            Const.logger.add_item("Case2", "SetAddrTime", t2 - t1)
            Const.logger.add_item("Case2", "SetAddrGas", self.account.gas_used)

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
        t1 = time()
        data_val = Const.ttp.att_enc(str(self.location[-1]), Const.access_policy)
        t2 = time()
        Const.logger.add_item("Case1", "EncTime", t2 - t1)
        t1 = time()
        data_adr = Const.ipfs.save(data_val)
        t2 = time()
        Const.logger.add_item("Case1", "IpfsSaveTime", t2 - t1)
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
        Const.logger.add_item("Case1", "SetAddrTime", t2 - t1)
        Const.logger.add_item("Case1", "SetAddrGas", self.account.gas_used)
        self.location_id.append(data_id)
        
    def read(self):
        print("CAR", f"ETH price is: {self.contract.getEthPrice.call()}")
        print("CAR", f"{self.account.address} used {self.account.gas_used} has {self.account.balance()}")
