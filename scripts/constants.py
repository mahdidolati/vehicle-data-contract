from scripts.entities.db_interface import DbInterface
from scripts.cryptography.ttp_util import ThirdParty
from scripts.helpful_scripts import get_account
from scripts.entities.ipfs_interface import IpfsInterface


class Const:
    ipfs = IpfsInterface()
    db = DbInterface(get_account(2))
    ttp = ThirdParty()

