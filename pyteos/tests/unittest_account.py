import unittest
import setup
import eosf
import time

from eosf_wallet import Wallet
from eosf_account import account_factory, AccountMaster


eosf.set_verbosity([eosf.Verbosity.EOSF, eosf.Verbosity.OUT]) #, eosf.Verbosity.DEBUG])
eosf.set_throw_error(False)
#setup.set_command_line_mode()

cryptolions = "88.99.97.30:38888"

class Test1(unittest.TestCase):

    def run(self, result=None):
        super().run(result)
        print("""

NEXT TEST ====================================================================
""")

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass


    def test_05(self):
        setup.use_keosd(False)
        eosf.reset(is_verbose=0)
        wallet = Wallet()
        account_master = AccountMaster()
        wallet.import_key(account_master)
        ######################################################################

        account_factory("account_alice")
        print(account_alice.info())

        account_factory("account_carrol")
        print("The name attribute of the 'account_carrol' account object is '{}'" \
            .format(account_carrol))
        print("{}".format(account_carrol.code()))

        account_factory("account_alice")
        self.assertTrue(account_alice.error)

        account_factory("account_test")
        contract_test = eosf.Contract(account_test, "eosio.token")
        deploy = contract_test.deploy()
        account_test.code()

        time.sleep(1)

        action = account_test.push_action(
            "create", 
            '{"issuer":"' 
                + str(account_master) 
                + '", "maximum_supply":"1000000000.0000 EOS", \
                "can_freeze":0, "can_recall":0, "can_whitelist":0}')

        action = contract_test.push_action(
        "issue", 
        '{"to":"' + str(account_alice)
            + '", "quantity":"100.0000 EOS", "memo":"memo"}', \
            account_master)


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    unittest.main()
