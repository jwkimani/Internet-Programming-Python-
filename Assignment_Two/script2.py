__author__ = 'James W. Kimani'

'''
Create a script that will list:
-Customer number
-Customer name
-Total of payments made
-Total value of all orders made
-Credit limit
-Amount of available credit (credit limit plus the total payments made minus the total value of all orders made)
The list should be in a tabular format with data lined up in columns. The same information but will just list those
customers who have exceeded their credit
limit. That is, list customers for whom the total of the credit limit and the total payments made is less than the total
value of orders made.

Assume a PostgreSQL database in standard configuration. The Classic Models data will be in a database/schema named birt.
The user birt with password birt will have access to the schema.

'''

import psycopg2

#create a connection to the birt database
conn = psycopg2.connect(database="birt", user = "birt", password="birt")

customerNumbers = conn.cursor()
customerNumbers.execute("select distinct customernumber from customers")

#fetch all the customer numbers
cusnumberFetch = customerNumbers.fetchall()
#create an empty list to hold the customer numbers
customerNumberLst = []
#fill the customer number list with the unique customer numbers
for cusNum in range(0,len(cusnumberFetch)):
    customerNumberLst.append(cusnumberFetch[cusNum][0])

#sort the customer number list in ascending order
customerNumberLst.sort()

#names cursor
names = conn.cursor()

#credit limit cursor
creditLimitCrs = conn.cursor()

#payments cursor
payments = conn.cursor()

#orders cursor
orders = conn.cursor()

#order details cursor
orderDetails = conn.cursor()

#Table header
header = "{:<8} {:36} {:<15} {:<17} {:<17} {:<20}".format("Number", "Name", "Credit Limit", "Payments Made", "Orders Total", "Available Credit")
print("{:=^115}".format('='))
print(header)
print("{:=^115}".format('='))

for cusNum in customerNumberLst:
    #get the credit limit for each customer
    creditLimit = 0
    creditLimitCrs.execute("select creditlimit from customers where customernumber = %i" % cusNum)
    for cuscreditLimit in creditLimitCrs:
        creditLimit = cuscreditLimit[0]

    # get customer name
    cusName = ''
    names.execute("select customername from customers where customernumber = %i" % cusNum)
    for name in names:
        cusName = name[0]

    #get the total payments made for each customer based on their customer number
    totalPayments = 0
    payments.execute("select amount from payments where customernumber = %i" % cusNum)
    for eachPayment in payments:
        totalPayments += eachPayment[0]

    #get the order total for each order
    totalOrders = 0
    orders.execute("select ordernumber from orders where customernumber = %i" % cusNum)
    for orderNum in orders:
        orderDetails.execute("select quantityordered * priceeach from orderdetails where ordernumber = %i" % orderNum)
        for eachorderTotal in orderDetails:
            totalOrders += eachorderTotal[0]
    #get the amount of available credit: credit limit plus the total payments made minus the total value of all orders made
    available_credit = creditLimit + totalPayments - totalOrders
    # print only information for customer who have exceeded their credit limit
    if creditLimit + totalPayments < totalOrders:
        print("{:<8} {:<36} {:<15.2f} {:<17.2f} {:<17.2f} {:<20.2f}".format(cusNum, cusName, creditLimit,
                                                                            totalPayments, totalOrders, available_credit))
        print("{:-^115}".format('-'))
















