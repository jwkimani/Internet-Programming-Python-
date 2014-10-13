Assignment 2
============

Create two Python scripts that will print out information from the Classic Models database.

The first script will list all customers with the following information:

> 
  - Customer number
  - Customer name
  - Total of payments made
  - Total value of all orders made
  - Credit limit
  - Amount of available credit (credit limit plus the total payments made minus the total value of all orders made)
  
The list should be in a tabular format with data lined up in columns.

The second script will list the same information but will just list those customers who have exceeded their credit limit.
That is, list customers for whom the total of the credit limit and the total payments made is less than the total value
of orders made.

Assume a PostgreSQL database in standard configuration. The [Classic Models](https://github.com/jwkimani/Internet-Programming/tree/master/Database)
data will be in a database/schema named _birt_.
The user _birt_ with password _birt_ will have access to the schema.

The page [customer-list.html](http://cs.kennesaw.edu/~bsetzer/4320fa14/nanoc/output/assignments/birt-sample/customer-list.html) 
displays the information. NOTE! you will be creating a table in pure text. The web page was just the most convenient way
to provide some data you could compare against.
