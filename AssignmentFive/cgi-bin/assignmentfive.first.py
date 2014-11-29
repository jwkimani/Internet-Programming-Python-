#!C:\Python34\python.exe
__author__ = 'James W. Kimani'

import psycopg2
conn = psycopg2.connect(host = "localhost",user="birt", password="birt")

print ("Content-Type: text/html; charset=UTF-8")
print ('''
<!DOCTYPE html>
<html>
<head>
    <title>Classic Models</title>
    <link href = '/style1.css' rel='stylesheet' type ='text/css'/>
</head>
<body>

''')

print ("<h1> First Application </h1>")

print("<h2>")
print ("<table class = 'grid'>")
print ("<tr><th>Customer number</th><th>"
       "Customer name</th><th>"
       "Total of payments made</th><th>"
       "Total value of all orders made </th><th>"
       "Credit limit</th><th>"
       "Amount of available credit</th></tr>")
print ("</table>")
print ("</h2>")
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

    print("""
   <style>
table th, th{
    border: 1px solid black;
    border-collapse: collapse;}
</style>

 <table class = 'grid'><tr>
      <td><th>""",cust[0],"""</th></td>
      <td><th>""",cust[1],"""</th></td>
      <td><th>""",total_payment,"""</th></td>
      <td><th>""",Order_Made,"""</th></td>
      <td><th>""",cust[2],"""</th></td>
      <td><th>""",available_credit,"""</th></td>
</tr></table>
        """)
    #line = line_template.format(cust[0],cust[1],total_payment,Order_Made,cust[2],available_credit )

print ('''
<p> Link to <a href="http://localhost/cgi-bin/assignmentfive.second.py"> Access to Second Application</a></p>
</body>
</html>
      ''')




