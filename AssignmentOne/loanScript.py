__author__ = 'jkimani2'


import sys
from Loan import Loan


def main(argv):
    initialBalance = int(sys.argv[1])
    interestRate = int(sys.argv[2])
    term = int(sys.argv[3])
    myLoan = Loan(initialBalance, interestRate, term, 0)
    myLoan.computeMonthlyPayment()
    header = '{:<10s} {:<17s} {:<15s} {:<14s} {:<18s}'.format("Month", "Balance In", "Interest", "Payment", "Balance Out")
    print(header)
    for a in range(1, term + 1):
        results = '{:>5} {:>15.2f} {:>15.2f} {:>14.2f} {:18.2f}'.format(
            a, myLoan.remainingBalance(a), myLoan.interestAccrued(a), myLoan.monthlyPayment, myLoan.remainingBalance(a+1))
        print(results)

if __name__ == "__main__":
    main(sys.argv[1:])
