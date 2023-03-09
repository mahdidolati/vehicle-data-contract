from eth_utils import address
from web3 import Web3
import os
from solcx import compile_standard
from dotenv import load_dotenv
import json
from entities.contract_api import get_compiled_contract
from constants import Const


class Insurance:
    def __init__(self, account_address, account_pk):
        self.address = account_address
        self.private_key = account_pk
        self.nonce = 0

    def get_nonce(self):
        n = self.nonce
        self.nonce = self.nonce + 1
        return n

    def read(self, car):
        bytecode, abi = get_compiled_contract(car.contract_path, car.contract_name)
        contract = Const.w3.eth.contract(
            abi=abi,
            address=car.contract_address
        )
        print(contract.functions.retrieve().call())

    def pay(self, car):
        balance = Const.w3.eth.getBalance(self.address)
        print(balance)
        #gas_limit = self.contract.createProposal("ADHD", "Foo", 2, {from: web3.eth.accounts[1], gas:3000000})
        #
        bytecode, abi = get_compiled_contract(car.contract_path, car.contract_name)
        contract = Const.w3.eth.contract(
            abi=abi,
            address=car.contract_address
        )
        call_fun = contract.functions.fund().buildTransaction({
            "chainId": Const.chain_id,
            "from": self.address,
            "nonce": self.get_nonce(),
            "value": Const.w3.toWei(2536750*10**10, "wei")
        })
        sign_call_fun = Const.w3.eth.account.sign_transaction(call_fun, private_key=self.private_key)
        tx_call_fun_hash = Const.w3.eth.send_raw_transaction(sign_call_fun.rawTransaction)
        tx_call_fun_receipt = Const.w3.eth.wait_for_transaction_receipt(tx_call_fun_hash)