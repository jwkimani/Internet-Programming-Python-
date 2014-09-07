__author__ = 'Ben Setzer'

import unittest
from Loan import Loan

class TestLoan(unittest.TestCase):
    #  one set of loan parameters
    bal1 = 1200
    rate1 = .12
    num1 = 12
    pmt1 = 106.61854641401
    bal1_6 = 717.350320703218
    bal1_11 = 210.080657084758
    bal1_16 = -323.064857489090
    int1_6 = 7.17350320703218
    int1_11 = 2.10080657084758
    int1_16 = -3.23064857489090

    bal2 = 5000
    rate2 = .24
    num2 = 15
    pmt2 = 389.12736125122
    bal2_6 = 3495.369600693820
    bal2_11 = 1834.136060908720
    bal2_15 = 381.497412991396
    int2_6 = 69.90739201387640
    int2_11 = 36.68272121817440
    int2_15 = 7.62994825982792


    def setUp(self):
        self.loan1 = Loan(TestLoan.bal1, TestLoan.rate1, TestLoan.num1, 0)
        self.loan1.computeMonthlyPayment()
        self.loan2 = Loan(TestLoan.bal2, TestLoan.rate2, TestLoan.num2, 0)
        self.loan2.computeMonthlyPayment()

    def test_1_monthly_payment(self):
        self.assertAlmostEqual(self.loan1.monthlyPayment, TestLoan.pmt1)

    def test_1_remaining_balance(self):
        self.assertAlmostEqual(self.loan1.remainingBalance(11), TestLoan.bal1_11)
        self.assertAlmostEqual(self.loan1.remainingBalance(6), TestLoan.bal1_6)
        self.assertAlmostEqual(self.loan1.remainingBalance(16), TestLoan.bal1_16)

    def test_1_interest_accrued(self):
        self.assertAlmostEqual(self.loan1.interestAccrued(6), TestLoan.int1_6)
        self.assertAlmostEqual(self.loan1.interestAccrued(16), TestLoan.int1_16)
        self.assertAlmostEqual(self.loan1.interestAccrued(11), TestLoan.int1_11)

    def test_2_monthly_payment(self):
        self.assertAlmostEqual(self.loan1.monthlyPayment, TestLoan.pmt1)

    def test_2_remaining_balance(self):
        self.assertAlmostEqual(self.loan2.remainingBalance(11), TestLoan.bal2_11)
        self.assertAlmostEqual(self.loan2.remainingBalance(6), TestLoan.bal2_6)
        self.assertAlmostEqual(self.loan2.remainingBalance(15), TestLoan.bal2_15)

    def test_2_interest_accrued(self):
        self.assertAlmostEqual(self.loan2.interestAccrued(6), TestLoan.int2_6)
        self.assertAlmostEqual(self.loan2.interestAccrued(15), TestLoan.int2_15)
        self.assertAlmostEqual(self.loan2.interestAccrued(11), TestLoan.int2_11)


if __name__ == '__main__':
    unittest.main()
