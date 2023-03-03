from eth_utils import address
from web3 import Web3
import os
from solcx import compile_standard
from dotenv import load_dotenv
import json
from entities.contract_api import get_compiled_contract
from constants import Const


class Insurance:
    def __init__(self):
        pass

    def read(self, contract_path, contract_name, contract_address):
        bytecode, abi = get_compiled_contract(contract_path, contract_name)
        contract = Const.w3.eth.contract(
            abi=abi,
            address=contract_address
        )
        print(contract.functions.retrieve().call())