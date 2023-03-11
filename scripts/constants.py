from scripts.entities.db_interface import DbInterface
from scripts.cryptography.ttp_util import ThirdParty


class Const:
    db = DbInterface()
    ttp = ThirdParty()
