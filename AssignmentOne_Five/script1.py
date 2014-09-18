__author__ = 'James W. Kimani'

'''
Write a Python script that will create a list of all products in the database, providing the following information for each product:
    - Product Code
    - Product Name
    - Product Line
    - Product Scale
    - Product Vendor
    - Quantity in stock
    - Buy price
Manufacturer’s suggested retail price
Note, the product description is omitted since it can be very long.

The table should align the fields into columns. The table will probably be very wide. Print a row of headers for the
columns first.

Assume a PostgreSQL database in standard configuration. The Classic Models data will be in a database/schema named birt.
The user birt with password birt will have access to the schema.
'''

import psycopg2

conn = psycopg2.connect(database="birt", user = "birt", password="birt")
get_cmd = "select productcode, productname, productline, productscale, productvendor, quantityinstock, buyprice, msrp from products"
crs = conn.cursor()
crs.execute(get_cmd)

header = "{:20} {:<50} {:<30} {:<20} {:<40} {:<30} {:<20} {:<10}".format("Product Code", "Product Name", "Product Line", "Product Scale", "Product Vendor", "Quantity in Stock", "Buy Price", "M.S.R.P")
print("{:=^227}".format('='))
print(header)
print("{:=^227}".format('='))
for p in crs:
    print("{:20} {:<50} {:<30} {:<20} {:<40} {:<30} {:<20} {:<10}".format(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7]))
    print("{:-^227}".format('-'))
conn.close()

