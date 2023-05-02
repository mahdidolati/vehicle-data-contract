from scripts.entities.car import Car
from scripts.entities.insurance import Insurance
from scripts.entities.researcher import Researcher
from brownie import accounts, MockV3Aggregator
from scripts.constants import Const
from time import time
from scripts.util.helpful_scripts import get_account, deploy_mocks
from scripts.util.my_logger import MyLogger


def run():
    deploy_mocks()
    price_feed_address = MockV3Aggregator[-1].address

    car_account = get_account(0)
    car = Car(car_account)
    researcher_account = get_account(3)
    researcher = Researcher(researcher_account)
    insurance_account = get_account(1)
    insurance = Insurance(insurance_account)

    car.deploy(price_feed_address)

    car.use_ipfs()
    car.use_ipfs()    
    insurance.read_ipfs(car, car.location_id[-1])
    print(f"Car: {car.account.balance()} -- Insurance: {insurance.account.balance()}")

    car.use_ipfs()
    researcher.request_and_pay(car, car.location_id[-1])
    car.review_ipfs()
    researcher.read_ipfs(car, car.location_id[-1] + "_i")
    print(f"Car: {car.account.balance()} -- Researcher: {researcher.account.balance()}")

    car.use_ipfs()
    researcher.request_and_pay(car, car.location_id[-1])
    car.review_ipfs()
    researcher.read_ipfs(car, car.location_id[-1] + "_i")
    print(f"Car: {car.account.balance()} -- Researcher: {researcher.account.balance()}")

    Const.logger.print()
    Const.db.close()


def main(itr_num_str, policy_len_str, clause_len_str):
    itr_num = int(itr_num_str)
    policy_len = int(policy_len_str)
    clause_len = int(clause_len_str)
    policy_clauses = [
        ["insurance", "(inspecting or renewing)", "(international or national)", "(public or private)", "(direct or indirect)", "(one or two)"],
        ["police", "(searching or checking)", "(local or national)", "(permit or law)", "(english or french)", "(three or four)"],
        ["court", "(investigating or enforcing)", "(region or state)", "(starting or ending)", "(ball or bin)", "(five or six)"],
        ["customs", "(import or export)", "(verifying or statistics)", "(tax or tariff)", "(list or receipt)", "(seven or eight)"],
        ["customs2", "(import2 or export2)", "(verifying2 or statistics2)", "(tax2 or tariff2)", "(list2 or receipt2)", "(nine or ten)"],
        ["customs23", "(import23 or export23)", "(verifying23 or statistics23)", "(tax23 or tariff23)", "(list23 or receipt23)", "(nine3 or ten3)"]
    ]
    attributes = {
        "insurance": ["insurance", "inspecting", "international", "public", "direct", "one"],
        "police": ["police", "searching", "local", "permit", "english", "three"],
        "court": ["court", "investigating", "region", "starting", "ball", "five"],
        "customs": ["customs", "import", "verifying", "tax", "list", "seven"],
        "customs2": ["customs2", "import2", "verifying2", "tax2", "list2", "nine3"]
    }
    if policy_len <= len(policy_clauses) and clause_len <= len(policy_clauses[0]):
        for i in range(policy_len):
            clause = policy_clauses[i][0]
            for j in range(1, clause_len):
                clause = clause + " and " + policy_clauses[i][j]
            clause = "(" + clause + ")"
            if i == 0:
                access_policy = clause
            else:
                access_policy = access_policy + " or " + clause
        Const.access_policy = access_policy
        print(Const.access_policy)
        Const.attributes = dict()
        for k in attributes:
            Const.attributes[k] = attributes[k][0:clause_len]
            Const.attributes[k] = [s.upper() for s in Const.attributes[k]]
        Const.logger = MyLogger("{}-{}-{}".format(itr_num, policy_len, clause_len))
        run()
