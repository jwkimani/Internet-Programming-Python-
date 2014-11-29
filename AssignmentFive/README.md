Assignment 5
============
Summary
-------

In this project you will create two applications. Both applications will use the Classic Models database. The first application will list data about customers similarly to the Assignment #2. The second application will allow a user to choose a customer and will then display information about that customer.

Please read the assignment carefully! Important requirements are state throughout this document.

The First Application
---------------------

The first application will list all customers with the following information:
>>
- Customer number
- Customer name
- Total of payments made
- Total value of all orders made
- Credit limit
- Amount of available credit (credit limit plus the total payments made minus the total value of all orders made)
_The rows should be ordered by customer number._

The Second Application
----------------------

The second application will present a page to the user allowing the user to choose a customer. When that page is submitted, the response will be a page with information about that customer:
>>
- Basic information
- Customer number
- Customer name
- Contact name
- Phone number
- Address
- Full name of the sales representative
- Financial information
- A message saying that customer has made no orders or, if the customer did make orders, a table listing the orders with
- order number
- order date
- total value of the order
- A message saying that the customer has made no payments or, if the customer did make payments, a table listing the payments with
- Check number
- Payment data
- Amount
- Organization

Besides the two applications, provide a welcome web page with links to the two applications

Provide styling through a common style file. Use your own or use one from class.

Use templates for the pages created by scripts. These templates should extend a base template to provide a common look.

The files should be located as follows:

| File                             | Location      |
|----------------------------------|---------------|
| Welcome page                     | Document root |
| Style file                       | Document root |
| Script for first application     | cgi-bin root  |
| Script for customer choice page  | cgi-bin root  |
| Script for customer data display | cgi-bin root  |
| Template files                   |               |

Test Setup
----------

The Classic Models database will be available from PostgreSQL with database named ‘_birt_’, user name ‘_birt_’, password ‘_birt_’ and host ‘_localhost_’.

Python version 3.4 will be used.

Make sure the submitted files are properly organized, see the Submissions section. The document files and any directories with the documents will be copied to the root document folder of a web server. The script files and any directories with them will be copied to the root cgi-bin directory of a web server.

Do not assume that the web server port will be 80.
