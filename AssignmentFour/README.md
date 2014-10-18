Assignment 4
============

Client/Server Using Sockets
===========================

Create two Python scripts: one a server; the other a client that will use the server.

Server
------
The server will listen on port 12321. The server will accept a string of characters representing three numbers separated
by spaces. These will be float, float, integer. The first number is the balance on a loan. The second number is the 
annual interest rate on a loan, represented as a decimal. The third number is the number of months in the term of the 
loan. So, for example
> 10000 .10  24

describes a loan with an initial balance of $10,000 borrowed at an annual rate of 10% due in 24 months. The server will 
respond with a string representing the monthly payment of the loan. For example, in this case, the server should respond
with
> 461.4492633751660000

Note that the amount is not rounded. Once the server has responded, the program should terminate.

Client
------
The client script will accept three command line arguments: the initial balance; the annual interest rate as a percent-
age; and, the number of months in the term of the loan. So, if your script is named loan_client.py, it might be invoked 
from the command line as
> loan_client.py  10000  10 24

for a loan with an initial balance of $10,000 borrowed at an annual rate of 10% due in 24 months. (The same loan 
described above) The client should send the three numbers to the server and should print the result received, displaying
a suitable message and rounding the display result to two decimal places. So, the output might look like this:

> The loan payment will be 461.45