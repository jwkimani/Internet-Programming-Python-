__author__ = 'James W. Kimani'

'''
Write a Python script that will accept a single command line parameter: the name of a product line. The script will list
all the products in that product line. Display the information as in the previous script, omitting the Product Line
column. Omit the production description column as well. Before the table, the script should print the product line,
suitably labeled.

Assume a PostgreSQL database in standard configuration. The Classic Models data will be in a database/schema named birt.
The user birt with password birt will have access to the schema.
'''

import sys
import psycopg2

def main():
    productLine = sys.argv[1]
    conn = psycopg2.connect(database="birt", user = "birt", password="birt")
    get_cmd = "select productcode, productname, productscale, productvendor, quantityinstock, buyprice, msrp from " \
              "products where productline = %s"
    crs = conn.cursor()
    crs.execute(get_cmd, (productLine,))
    header = "{:20} {:<50} {:<20} {:<40} {:<30} {:<20} {:<10}".format("Product Code", "Product Name",
                                                                      "Product Scale", "Product Vendor", "Quantity in "
                                                                        "Stock", "Buy Price", "M.S.R.P")
    print(productLine)
    print("{:=^197}".format('='))
    print(header)
    print("{:=^197}".format('='))
    for p in crs:
        print("{:20} {:<50} {:<20} {:<40} {:<30} {:<20} {:<10}".format(p[0], p[1], p[2], p[3], p[4], p[5], p[6]))
        print("{:-^197}".format('-'))
    conn.close()

if __name__ == "__main__":
    main()
