__author__ = 'James W. Kimani'
'''
Server

The server will listen on port 12321. The server will accept a string of characters representing three numbers separated by spaces. These will be float, float, integer. The first number is the balance on a loan. The second number is the annual interest rate on a loan, represented as a decimal. The third number is the number of months in the term of the loan. So, for example

10000 .10  24
describes a loan with an initial balance of $10,000 borrowed at an annual rate of 10% due in 24 months. The server will respond with a string representing the monthly payment of the loan. For example, in this case, the server should respond with

461.4492633751660000
Note that the amount is not rounded. Once the server has responded, the program should terminate.

'''
from socket import socket
import math

listener_socket = socket()

listener_socket.bind(('', 12321)) #host: listen on any ip address
                                  #port: 12345

#listen
listener_socket.listen(5)

print("Now calling accept function")

(sock, address) = listener_socket.accept()
#script is now waiting for a connection
'''
print("Connection made and accepted")

print("Socket is "+ str(sock))
print("Address is "+ str(address))
'''
rcvd_data = sock.recv(2048)
print("Received: ", rcvd_data)
rcvd_string = rcvd_data.decode()#use standard decoding
print("Received string: ", rcvd_string)
rcvd_string = rcvd_string.split(' ',3)
#print("Principal is: %s\nRate is: %s\nTime is: %s" %(rcvd_string[0],rcvd_string[1], rcvd_string[2]))

initialBalance, interestRate, numMonth = int(rcvd_string[0]),int(rcvd_string[1])/1200, int(rcvd_string[2])

monthlyPayment = initialBalance * interestRate/(1 - math.pow(1 + interestRate, - numMonth))
print(monthlyPayment)

result = "The loan payment will be %s" % monthlyPayment

mnthPyment = str(monthlyPayment).encode()
sock.send(mnthPyment)
sock.close()

listener_socket.close()



