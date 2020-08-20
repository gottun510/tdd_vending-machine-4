# from unittest import TestCase
from vending_machine.hoge.coin import Coin, VendingMachine


class TestVendingMachine():

    def test_check_coin(self):
        machine = VendingMachine()
        assert machine.check_coin(Coin(50)) == True
        assert machine.check_coin(Coin(40)) == False

    def test_treatment_coin(self):
         machine = VendingMachine()
         machine.treatment_coin(Coin(50))
         assert machine.contained[0].amount == Coin(50).amount
         
         assert machine.treatment_coin(Coin(20)).amount == 20


    def test_catch_coin(self):
        machine = VendingMachine()
        machine.check_coin(Coin(50))
        assert Coin(50).amount == machine.contained[0].amount

        machine_invalid = VendingMachine()
        coin30 = Coin(30)
        result = machine_invalid.check_coin(coin30)
        assert result == coin30
        assert machine_invalid.contained == []

    def test_coin_total(self):
        machine = VendingMachine()
        machine.check_coin(Coin(500))
        machine.check_coin(Coin(100))
        machine.check_coin(Coin(50))
        assert 500 + 100 + 50 == machine.coin_total()

    def test_refund(self):
        machine = VendingMachine()
        coin500 = Coin(500)
        coin100 = Coin(100)
        coin50 = Coin(50)
        machine.check_coin(coin500)
        machine.check_coin(coin100)
        machine.check_coin(coin50)

        assert [coin500, coin100, coin50] == machine.refund()
        assert [] == machine.contained

    # def test_catch_coin_invalid(self):


# class TestStock():
#     def test_check(self):

#         assert stock.check() == []
