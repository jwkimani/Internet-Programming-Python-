__author__ = 'James Kimani'
import math


class Loan(object):
    def __init__(self,initialBalance, interestRate, numMonth, monthlyPayment):
        self.initialBalance = initialBalance
        self.interestRate = (interestRate/12.0)/100
        self.numMonth = numMonth
        self.monthlyPayment = monthlyPayment

    '''
    computes the monthly payment based on the other values. The monthly payment should be computed so that the remaining
    balance after the last month in the term of the loan is 0. The formula is M = P * ( R / (1 - (1 + R)^ -N)).
    '''
    def computeMonthlyPayment(self):
        monthlyPayment = self.initialBalance * self.interestRate/(1 - math.pow(1 + self.interestRate, -self.numMonth))
        self.monthlyPayment = monthlyPayment

    '''
    returns the balance remaining at the end of the month given. month should be greater than or equal to 1 The
    remaining balance at the end of month 1 is the initial balance The balance at the end of month m+1 is the remaining
    balance at the end of month m plus the interest accrued at the end of month m and minus the monthly payment.
    '''
    def remainingBalance(self, month):
        if month == 1:
            return self.initialBalance
        else:
            return self.remainingBalance(month - 1) + self.interestAccrued(month -1) - self.monthlyPayment

    '''
    returns the amount of interest earned at the end of the month given. month should be greater than or equal to 1
    '''
    def interestAccrued(self, month):
        assert month >= 1, "Month should be greater than or equal to 1. Please check your value"
        return self.remainingBalance(month) * self.interestRate * 1

