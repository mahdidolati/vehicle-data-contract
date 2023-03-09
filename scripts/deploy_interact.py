from brownie import BasicContract, accounts
from brownie import Contract


def main():
    # accounts.load("mahdi")
    account = accounts[0]
    print(f"Account 0: {account.address} used {account.gas_used}")
    # deploy_contract = Contract("0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87")
    deploy_contract = BasicContract.deploy({"from": account})
    print(f"contract deployed at {deploy_contract}")

    transaction_receipt = deploy_contract.storeNumber(15, {"from":account}) 
    transaction_receipt.wait(1)

    # retrieved_number = deploy_contract.readNumber()
    retrieved_number = deploy_contract.readNumber.call() 
    print(f"Number Retrieved : {retrieved_number}")
    print(f"Account 0: {account.address} used {account.gas_used}")
    print(f"Account 0: {account.address} balance {account.balance()}")