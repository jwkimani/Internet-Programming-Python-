AssignmentOne: Create a loan class using python
=============

Internet Programming Fall 2014

In this problem you will create a Python class and a Python script that will use that class.

Class Loan
==========

The class Loan represents a basic consumer loan, such as a mortgage. The class has four instance fields: the number of months in the term of the loan; the initial balance of the loan; the annual interest rate of the loan, as a decimal; the monthly payment on the loan.

In a basic loan, a transaction is carried out at the end of each month. From month to month, the balance of the loan will change based on the payments made and the interest accrued. At the end of each month, the amount of interest for that month is computed. This is added to the balance. Then the monthly payment is subtracted from the balance. This leaves the current balance on the loan for the next month.

The following methods will provide access to the various important values about the loan:

remainingBalance(self, m) returns the balance remaining at the end of month number m. m should be greater than or equal to 1
The remaining balance at the end of month 1 is the initial balance
The balance at the end of month m is the remaining balance at the end of month m-1 plus the interest accrued at the end of month m-1 and minus the monthly payment

interestAccrued(self, m) returns the amount of interest earned at the end of the month m. m should be greater than or equal to 1.
Compute this by computing the remaining balance for m and multiplying it by the monthly interest rate.

__init__(self, initialBalance, annualRate, numberOfMonths, monthlyPayment) There should be an initializer that takes values for the four instance fields.
computeMonthlyPayment(self): computes the monthly payment based on the other values. The monthly payment should be computed so that the remaining balance after the last month in the term of the loan is 0. You can find the formula for computing the payment at many places on the web. This method will set the monthly payment instance field. It can return the computed value if you wish, but that is not required.
To guide you, there is a test program Test5.py that will use the methods and compare the results to precomputed values. Although this uses the Python unit test framework, you just run it as if it were a regular script.

The script
==========

Write a Python script, in a separate file, that will use the Loan class. The script should get three values from the command line, in this order: the initial balance; the annual interest rate as a percentage; the number of months in the term of the loan. Command line arguments (aka script parameters) will be discussed in class, notes

The script should create a Loan object using the three values and using 0 for the monthly payment. Then, the computeMonthlyPayment method should be called. Finally, a table of values should be printed with a number of rows equal to the number of months in the loan. Each row of the table should give these values, in order: the month number, starting at 1; the balance remaining, which will be the initial balance for the first month; the amount of interest accrued that month; the amount of the monthly payment, always the same; the remaining balance after adding interest and subtracting the monthly payment. Monetary amounts should display with exactly two decimal places. Figures should line up in neat columns. Headings should line up over the columns. See the example below.

For example, the command:

    loanScript.py   10000 10 20
will display a table for the loan with initial balance $1000, an annual interest rate of 10% and to be paid off at the end of 20 months. Here is the output from my version of the assignment. Note that the ‘Balance Out’ in the last row is 0.

Month      Balance In        Interest         Payment     Balance Out
    1        10000.00           83.33          544.90         9538.43
    2         9538.43           79.49          544.90         9073.02
    3         9073.02           75.61          544.90         8603.73
    4         8603.73           71.70          544.90         8130.53
    5         8130.53           67.75          544.90         7653.38
    6         7653.38           63.78          544.90         7172.26
    7         7172.26           59.77          544.90         6687.13
    8         6687.13           55.73          544.90         6197.96
    9         6197.96           51.65          544.90         5704.71
   10         5704.71           47.54          544.90         5207.35
   11         5207.35           43.39          544.90         4705.85
   12         4705.85           39.22          544.90         4200.16
   13         4200.16           35.00          544.90         3690.26
   14         3690.26           30.75          544.90         3176.12
   15         3176.12           26.47          544.90         2657.69
   16         2657.69           22.15          544.90         2134.93
   17         2134.93           17.79          544.90         1607.83
   18         1607.83           13.40          544.90         1076.33
   19         1076.33            8.97          544.90          540.40
   20          540.40            4.50          544.90           -0.00

