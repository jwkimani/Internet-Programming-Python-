#!C:\Python34\python.exe

__author__ = 'James W. Kimani'

import psycopg2
import cgitb
import cgitb
cgitb.enable()
from jinja2 import Environment, FileSystemLoader
import psycopg2

conn = psycopg2.connect(host = "localhost",user="birt", password="birt")

print("Content-Type: text/html; charset=UTF-8")
print("")

crs = conn.cursor()
cmd = '''
     select customernumber,customername, creditlimit
     from customers

    '''
crs.execute(cmd)
customer_list = crs.fetchall()

for cust in customer_list:
    cmd = '''
        select amount from payments
        where customerNumber = %s

    '''
    crs.execute(cmd,(cust[0],))
    payment_list = crs.fetchall()
    total_payment = 0
    for payment in payment_list:
        total_payment += payment[0]

    cmd = '''
        select orderNumber
        from orders
        where  customerNumber = %s

    '''
    crs.execute(cmd,(cust[0],))
    order_list = crs.fetchall()


    for order in order_list:
        cmd = '''
        select priceEach, quantityOrdered
        from orderdetails
        where orderNumber = %s
    '''
        crs.execute(cmd,(order[0],))
        order_orderList = crs.fetchall()
        Order_Made = 0

        for totalOrder in order_orderList:
            Order_Made += totalOrder[0]*totalOrder[1]

        available_credit = cust[2] + total_payment - Order_Made

"""
do database, pass it to List_information.html
"""
ldr = FileSystemLoader("templates")
env = Environment(loader=ldr)
template = env.get_template("List_Information.html")
template_rendered = template.render(customer_list=customer_list)

#payment_list=total_payment, order_list=Order_Made, available_credit=available_credit
print(template_rendered)



