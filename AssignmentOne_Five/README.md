Assignment 1.5
==============

Create two Python scripts that will print out information from the Classic Models database.

Script 1
---------

Write a Python script that will create a list of all products in the database, providing the following information for each product:

-Product Code
-Product Name
-Product Line
-Product Scale
-Product Vendor
-Quantity in stock
-Buy price
-**M**anufacturer’s **S**uggested **R**etail **P**rice
Note, the product description is omitted since it can be very long.

The table should align the fields into columns. The table will probably be very wide. Print a row of headers for the columns first.

Assume a PostgreSQL database in standard configuration. The Classic Models data will be in a database/schema named _birt_. The user _birt_ with password _birt_ will have access to the schema.

Script 2
--------

Write a Python script that will accept a single command line parameter: the name of a product line. The script will list all the products in that product line. Display the information as in the previous script, omitting the Product Line column. Before the table, the script should print the product line, suitably labeled.

Assume a PostgreSQL database in standard configuration. The Classic Models data will be in a database/schema named birt. The user birt with password birt will have access to the schema.