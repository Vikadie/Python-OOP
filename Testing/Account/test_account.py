from account import Account

import unittest
import types


class AccountTest(unittest.TestCase):

    def setUp(self):
        self.a = Account('George')

    def test_init(self):
        self.assertEqual(self.a.owner, 'George')
        self.assertEqual(self.a.amount, 0)
        self.assertEqual(self.a._transactions, [])
        self.assertEqual(self.a.balance, 0)

    def test_init_with_amount(self):
        account = Account('bob', 10)
        self.assertEqual(account.amount, 10)
        self.assertEqual(account.owner, 'bob')

    def test_add_transaction_amount_not_int(self):
        with self.assertRaises(ValueError) as exc:
            self.a.add_transaction('Not Int')
        self.assertEqual(str(exc.exception), 'please use int for amount')

    def test_add_transaction_amount_not_int_but_float(self):
        with self.assertRaises(ValueError) as exc:
            self.a.add_transaction(3.14)
        self.assertEqual(str(exc.exception), 'please use int for amount')

    def test_add_transaction_amount_OK(self):
        self.a.add_transaction(33)
        self.assertTrue(len(self.a._transactions) == 1)
        self.assertEqual(len(self.a), 1)

    def test_balance_is_property(self):
        self.assertTrue(self.a.balance == 0)

    def test_balance_return_sum_of_transactions(self):
        self.a.add_transaction(22)
        self.a.add_transaction(44)
        self.assertEqual(self.a.balance, 22 + 44)

    def test_validate_transaction_negative_balance(self):
        with self.assertRaises(ValueError) as exc:
            Account.validate_transaction(self.a, -30)
        self.assertEqual(str(exc.exception), 'sorry cannot go in debt!')

    def test_validate_transaction_invalid_amount(self):
        with self.assertRaises(ValueError) as exc:
            Account.validate_transaction(self.a, 30.5)
        self.assertEqual(str(exc.exception), 'please use int for amount')

    def test_validate_transaction_OK(self):
        res = Account.validate_transaction(self.a, 30)
        self.assertEqual(self.a.balance, 30)
        self.assertEqual(f"New balance: {sum(self.a._transactions)}", res)

    def test_invalid_transaction_should_not_change_the_balance(self):
        start_balance = self.a.balance
        with self.assertRaises(ValueError) as exc:
            Account.validate_transaction(self.a, -start_balance - 1)

        self.assertEqual(start_balance, self.a.balance)

    def test_if_validate_transaction_is_static_fn(self):
        self.assertTrue(isinstance(self.a.validate_transaction, types.FunctionType))

    def test_magic_method_str(self):
        string = str(self.a)
        self.assertEqual("Account of George with starting amount: 0", string)

    def test_magic_repr(self):
        representation = repr(self.a)
        self.assertEqual("Account(George, 0)", representation)

    def test_magic_len(self):
        self.assertEqual(len(self.a._transactions), 0)
        self.a.add_transaction(20)
        self.a.add_transaction(-20)
        self.a.add_transaction(20)
        self.a.add_transaction(-20)
        self.assertEqual(len(self.a._transactions), 4)
        self.assertEqual(self.a.balance, 0)

    def test_magic_getitem(self):
        self.a.add_transaction(10)
        self.a.add_transaction(20)
        self.a.add_transaction(30)
        self.assertEqual(self.a[2], 30)

    def test_magic_reversed(self):
        self.a.add_transaction(10)
        self.a.add_transaction(20)
        self.a.add_transaction(30)
        self.assertEqual(list(self.a), [10, 20, 30])
        self.assertEqual(list(reversed(self.a)), [30, 20, 10])

    def test_magic_method_eq(self):
        acc = Account("Pesho", 30)
        self.assertTrue(self.a == self.a)
        self.assertFalse(acc == self.a)
        self.assertNotEqual(acc, self.a)

    def test_magic_method_not_eq(self):
        acc = Account("Pesho", 30)
        self.assertTrue(acc != self.a)
        self.assertFalse(self.a != self.a)
        self.assertNotEqual(acc, self.a)

    def test_magic_method_gt(self):
        acc = Account("Pesho", 30)
        self.assertFalse(self.a > acc)
        self.assertTrue(acc > self.a)
        self.assertGreater(acc, self.a)

    def test_magic_method_ge(self):
        acc = Account("Pesho", 30)
        self.assertTrue(acc >= self.a)
        self.assertTrue(self.a >= self.a)
        self.assertFalse(self.a >= acc)
        self.assertGreaterEqual(acc, self.a)

    def test_magic_method_lt(self):
        acc = Account("Pesho", 30)
        self.assertFalse(acc < self.a)
        self.assertTrue(self.a < acc)
        self.assertLess(self.a, acc)

    def test_magic_method_le(self):
        acc = Account("Pesho", 30)
        self.assertTrue(self.a <= acc)
        self.assertFalse(acc <= self.a)
        self.assertLessEqual(self.a, acc)

    def test_add_accounts(self):
        acc = Account("Pesho", 30)
        acc_total = acc + self.a
        string = str(acc_total)
        self.assertEqual('Account of Pesho&George with starting amount: 30', string)
        self.assertEqual(list(acc_total), [])

    def test_add_accounts_n_transactions(self):
        self.a.add_transaction(20)
        self.a.add_transaction(-20)
        acc = Account("Pesho", 30)
        acc.add_transaction(40)
        acc.add_transaction(-40)
        acc_total = acc + self.a
        string = str(acc_total)
        self.assertEqual('Account of Pesho&George with starting amount: 30', string)
        self.assertEqual(list(acc_total), [40, -40, 20, -20])


if __name__ == '__main__':
    unittest.main()