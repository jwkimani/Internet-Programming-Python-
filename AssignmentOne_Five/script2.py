__author__ = 'James W. Kimani'


import sys
import psycopg2

def main(argv):
    productLine = sys.argv[1]
    conn = psycopg2.connect(database="birt", user = "birt", password="birt")
    get_cmd = "select productcode, productname, productscale, productvendor, quantityinstock, buyprice, msrp from products where productline = '{}' ".format(productLine)
    crs = conn.cursor()
    crs.execute(get_cmd)
    header = "{:20} {:<50} {:<20} {:<40} {:<30} {:<20} {:<10}".format("Product Code", "Product Name", "Product Scale", "Product Vendor", "Quantity in Stock", "Buy Price", "M.S.R.P")
    print("{:=^197}".format('='))
    print(header)
    print("{:=^197}".format('='))
    for p in crs:
        print("{:20} {:<50} {:<20} {:<40} {:<30} {:<20} {:<10}".format(p[0], p[1], p[2], p[3], p[4], p[5], p[6]))
        print("{:-^197}".format('-'))
    conn.close()

if __name__ == "__main__":
    main(sys.argv[1])
