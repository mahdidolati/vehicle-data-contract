from scripts.db.db_interface import DbInterface
from scripts.db.ipfs_interface import IpfsInterface
from scripts.cryptography.ttp_util import ThirdParty
from scripts.util.helpful_scripts import get_account
from scripts.util.my_logger import MyLogger


class Const:
    ipfs = IpfsInterface()
    db = DbInterface(get_account(2))
    ttp = ThirdParty()
    logger = MyLogger()

