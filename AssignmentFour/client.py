__author__ = 'James W. Kimani'

'''
Client

The client script will accept three command line arguments: the initial balance; the annual interest rate as a percentage; and, the number of months in the term of the loan. So, if your script is named loan_client.py, it might be invoked from the command line as

loan_client.py  10000  10 24
for a loan with an initial balance of $10,000 borrowed at an annual rate of 10% due in 24 months. (The same loan described above) The client should send the three numbers to the server and should print the result received, displaying a suitable message and rounding the display result to two decimal places. So, the output might look like this:

The loan payment will be 461.45
'''
from socket import socket
import sys
try:
    sock = socket()

    sock.connect(('localhost', 12321))

    principal = sys.argv[1]
    rate = sys.argv[2]
    time = sys.argv[3]
    loan = "%s %s %s" %(principal, rate, time)
    byte_data = loan.encode() # convert string characters to bytes
    print("Connection made")

    sock.send(byte_data)
    reception = sock.recv(2048)

    rcvdmnth = reception.decode()
    mym = float(rcvdmnth)
    print("The loan payment will be %.2f" % mym)
    sock.close()

except Exception:
    print("Please enter 3 arguments")

