__author__ = 'James W. Kimani'
import psycopg2

__author__ = 'James W. Kimani'
'''
list all people  in the clubs database
'''

conn = psycopg2.connect(database="Derby", user = "birt", password="birt")
get_cmd = "select customernumber, customername, creditlimit from customers"
crs = conn.cursor()
crs.execute(get_cmd)

header = "{:>17} {:>15} {:>40} {:>19}{:>12} {:>18}".format("Customer Number", "Customer Name", "Payments Total", "Total Over Values", "Credit Limit", "Available Credit")
print(header)
for p in crs:
    print("{:^17} {:<15} {:>40} {:>19}{:>12} {:>18}".format(p[0], p[1], p[2],"a","b","c"))
conn.close()

