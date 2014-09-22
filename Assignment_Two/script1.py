__author__ = 'jkimani2'

'''
The first script will list all customers with the following information:

Customer number
Customer name
Total of payments made
Total value of all orders made
Credit limit
Amount of available credit (credit limit plus the total payments made minus the total value of all orders made)
The list should be in a tabular format with data lined up in columns.
'''

import psycopg2

conn = psycopg2.connect(database="birt", user = "birt", password="birt")
get_customerNumber = "select customernumber from customers"
crs = conn.cursor()
crs.execute(get_customerNumber)
results = crs.fetchall()
crs2 = conn.cursor()
crs3 = conn.cursor()

cusnum = []
for a in range(0,len(results)):
    cusnum.append(results[a][0])

for p in cusnum:
    crs2.execute("select amount from payments where customernumber = %i" % (p))
    for c in crs2:
        print(c[0], p)
