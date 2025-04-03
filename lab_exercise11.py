
# # Create following tables:

# # Table Name: CLIENT_MASTER
# # Column Name     Data Type       Size        Attributes
# # -----------------------------------------------------------------------------------------
# # CLIENTNO        Varchar         6           Primary Key/ First Letter must start with 'C'
# # NAME            Varchar         20          Not Null
# # CITY            Varchar         15
# # PINCODE         Number          8
# # STATE           Varchar         15
# # BALDUE          Number          10,2

# CREATE TABLE CLIENT_MASTER(
# 		CLIENTNO VARCHAR(6),
#         NAME VARCHAR(20) NOT NULL,
#         CITY VARCHAR(15),
#         PINCODE INT(8),
#         STATE VARCHAR(15),
#         BALDUE DECIMAL(10, 2),
#         PRIMARY KEY(CLIENTNO),
#         CHECK(CLIENTNO = 'C%')
# );



# # Table Name: PRODUCT_MASTER
# # Column Name     Data Type       Size        Attributes
# # -----------------------------------------------------------------------------------------
# # PRODUCTNO       Varchar         6           Primary Key/ First Letter must start with 'P'
# # DESCRIPTION     Varchar         15          Not Null
# # PROFITPERCENT   Number          4,2         Not Null
# # UNITMEASURE     Varchar         10          Not Null
# # QTYONHAND       Number          8           Not Null
# # REORDERLVL      Number          8           Not Null
# # SELLPRICE       Number          8,2         Not Null, cannot be 0
# # COSTPRICE       Number          8,2         Not Null, cannot be 0

# CREATE TABLE PRODUCT_MASTER(
# 		PRODUCTNO VARCHAR(6),
# 		DESCRIPTION VARCHAR(15) NOT NULL,
#         PROFITPERCENT DECIMAL(4, 2) NOT NULL,
#         UNITMEASURE VARCHAR(10) NOT NULL,
#         QTYONHAND INT(8) NOT NULL,
#         REORDERLVL INT(8) NOT NULL,
#         SELLPRICE DECIMAL(8, 2) NOT NULL,
#         COSTPRICE DECIMAL(8, 2) NOT NULL,
#         PRIMARY KEY(PRODUCTNO),
#         CHECK(SELLPRICE != 0),
#         CHECK(COSTPRICE != 0)
# );



# # Table Name: SALESMAN_MASTER
# # Column Name     Data Type       Size        Attributes
# # -----------------------------------------------------------------------------------------
# # SALESMANNO      Varchar         6           Primary Key / First letter must start with ‘S’
# # SALESMANNAME    Varchar         20          Not Null
# # ADDRESS1        Varchar         30          Not Null
# # ADDRESS2        Varchar         30
# # CITY            Varchar         20
# # PINCODE         Number          8
# # STATE           Varchar         20
# # SALAMT          Number          8,2         Not Null, cannot be 0
# # TGTTOGET        Number          6,2         Not Null, cannot be 0
# # YTDSALES        Number          6,2         Not Null
# # REMARKS         Varchar         60

# CREATE TABLE SALESMAN_MASTER(
# 		SALESMANNO VARCHAR(6),
#         SALESMANNAME VARCHAR(20) NOT NULL,
#         ADDRESS1 VARCHAR(30) NOT NULL,
#         ADDRESS2 VARCHAR(30),
#         CITY VARCHAR(20),
#         PINCODE INT(8),
#         STATE VARCHAR(20),
#         SALAMT DECIMAL(8,2) NOT NULL,
#         TGTTOGET DECIMAL(6,2) NOT NULL,
#         YTDSALES DECIMAL(6,2) NOT NULL,
#         REMARKS VARCHAR(60),
#         PRIMARY KEY(SALESMANNO),
#         CHECK(SALAMT != 0),
#         CHECK(TGTTOGET != 0)
# );



# # Table Name: SALES_ORDER
# # Column Name     Data Type       Size        Attributes
# # ------------------------------------------------------------------------------------------------------
# # ORDERNO         Varchar         6           Primary Key / First letter must start with ‘O’
# # CLIENTNO        Varchar         6           Foreign Key references ClientNo of Client_Master table
# # ORDERDATE       Date                        Not Null
# # DELYADDR        Varchar         25
# # SALESMANNO      Varchar         6           Foreign Key references SalesmanNo of Salesman_Master table
# # DELYTYPE        Char            1
# # BILLYN          Char            1
# # DELYDATE        Date
# # ORDERSTATUS     Varchar         10

# CREATE TABLE SALES_ORDER(
# 		ORDERNO VARCHAR(6),
#         CLIENTNO VARCHAR(6),
#         ORDERDATE DATE NOT NULL,
#         DELYADDR VARCHAR(25),
#         SALESMANNO VARCHAR(6),
#         DELYTYPE CHAR,
#         BILLYN CHAR,
#         DELYDATE DATE,
#         ORDERSTATUS VARCHAR(10),
#         PRIMARY KEY(ORDERNO),
#         CONSTRAINT fk_clientno FOREIGN KEY(CLIENTNO) REFERENCES CLIENT_MASTER(CLIENTNO),
#         CONSTRAINT fk_salesmanno FOREIGN KEY (SALESMANNO) REFERENCES SALESMAN_MASTER(SALESMANNO)
# );



# # Table Name: SALES_ORDER_DETAILS
# # Column Name     Data Type       Size        Attributes
# # ---------------------------------------------------------------------------------------------------
# # ORDERNO         Varchar         6           Foreign Key references OrderNo of Sales_Order table
# # PRODUCTNO       Varchar         6           Foreign Key references ProductNo of Product_Master table
# # QTYORDERED      Number          8
# # QTYDISP         Number          8
# # PRODUCTRATE     Number          10,2

# CREATE TABLE SALES_ORDER_DETAILS(
# 		ORDERNO VARCHAR(6),
#         PRODUCTNO VARCHAR(6),
#         QTYORDERED INT(8),
#         QTYDISP INT(8),
#         PRODUCTRATE DECIMAL(10,2),
#         CONSTRAINT fk_orederno FOREIGN KEY(ORDERNO) REFERENCES SALES_ORDER(ORDERNO),
#         CONSTRAINT fk_productno FOREIGN KEY(PRODUCTNO) REFERENCES PRODUCT_MASTER(PRODUCTNO)
# );



# # Insert data in respective tables
# INSERT INTO CLIENT_MASTER(CLIENTNO, NAME, CITY, PINCODE, STATE, BALDUE)
# VALUES
# 	('C00001', 'Ivan Bayross',  'Mumbai', 400054, 'Maharashtra', 15000),
#     ('C00003', 'Chhaya Bankar', 'Mumbai', 400057, 'Maharashtra', 5000),
#     ('C00004', 'Ashwini Joshi', 'Bangalore', 560001, 'Karnataka', 0),
#     ('C00005', 'Hansel Colaco', 'Mumbai', 400060, 'Maharashtra', 2000),
#     ('C00006', 'Deepak Sharma', 'Mangalore', 560050, 'Karnataka', 0);



# INSERT INTO PRODUCT_MASTER(PRODUCTNO, DESCRIPTION, PROFITPERCENT, UNITMEASURE, QTYONHAND, REORDERLVL, SELLPRICE, COSTPRICE)
# VALUES
# 	('P00001', 'T-Shirts', 5, 'Piece', 200, 50, 350, 250),
#     ('P03453', 'Shirts', 6, 'Piece', 150, 50, 500, 350),
#     ('P06734', 'Cotton Jeans', 5, 'Piece', 100, 20, 600, 450),
#     ('P07865', 'Jeans', 5, 'Piece', 100, 20, 750, 500),
#     ('P07868', 'Trousers', 2, 'Piece', 150, 50, 850, 550),
#     ('P07885', 'Pull Overs', 2.5, 'Piece', 80, 30, 700, 450),
#     ('P07965', 'Denim Shirts', 4, 'Piece', 100, 40, 350, 250),
#     ('P07975', 'Lycra Tops', 5, 'Piece', 70, 30, 300, 175),
#     ('P08865', 'Skirts', 5, 'Piece', 75, 30, 450, 300);



# INSERT INTO SALESMAN_MASTER(SALESMANNO, SALESMANNAME, ADDRESS1, ADDRESS2, CITY, PINCODE, STATE, SALAMT, TGTTOGET, YTDSALES, REMARKS)
# VALUES
# 	('S00001', 'Aman', 'A/14', 'Worli', 'Mumbai', 400002, 'Maharashtra', 3000, 100, 50, 'Good'),
#     ('S00002', 'Omkar', '65', 'Nariman', 'Mumbai', 400001, 'Maharashtra', 3000 , 200, 100, 'Good'),
#     ('S00003', 'Raj', 'P-7', 'Bandra', 'Mumbai', 400032, 'Maharashtra', 3000, 200, 100, 'Good'),
#     ('S00004', 'Ashish', 'A/5', 'Juhu', 'Bombay', 400044, 'Maharashtra', 3500, 200, 150, 'Good'); 



# INSERT INTO SALES_ORDER(ORDERNO, CLIENTNO, ORDERDATE, DELYADDR, SALESMANNO, DELYTYPE, BILLYN, DELYDATE, ORDERSTATUS)
# VALUES
# 	('O19003', 'C00001', STR_TO_DATE('03-APR-02', '%d-%b-%y'), 'Delhi', 'S00001', 'F', 'Y', STR_TO_DATE('07-APR-02', '%d-%b-%y'), 'Fulfilled'),
#     ('O46866', 'C00004', STR_TO_DATE('20-MAY-02', '%d-%b-%y'), 'Delhi', 'S00002', 'P', "N", STR_TO_DATE('22-MAY-02', '%d-%b-%y'), 'Cancelled'),
#     ('O19008', 'C00005', STR_TO_DATE('21-MAY-02', '%d-%b-%y'), 'Delhi', 'S00004', 'F', 'N', STR_TO_DATE('26-JUL-96', '%d-%b-%y'), 'In Process'),
#     ('O19001', 'C00001', STR_TO_DATE('12-Jun-02', '%d-%b-%y'), 'Delhi', 'S00001', 'F', 'N', STR_TO_DATE('20-JUL-02', '%d-%b-%y'), 'In Process');



# INSERT INTO SALES_ORDER_DETAILS(ORDERNO, PRODUCTNO, QTYORDERED, QTYDISP, PRODUCTRATE)
# VALUES
# 	('O19001', 'P00001', 4, 4, 525),
#     ('O19001', 'P07965', 2, 1, 8400),
#     ('O19001', 'P07885', 2, 1, 5250),
#     ('O19003', 'P03453', 2, 2, 1050),
#     ('O19003', 'P06734', 1, 1, 12000),
#     ('O46866', 'P07965', 1, 0, 8400),
#     ('O46866', 'P07965', 1, 0, 1050),
#     ('O19008', 'P00001', 10, 5, 525),
#     ('O19008', 'P07975', 5, 3, 1050);




# # Generate the SQL statements to perform the following computations on table data in Python IDLE:
# # a. List the names of all clients having ‘a’ as the second letter in their names.
# # b. List the clients who stay in a city whose first letter is ‘M’.
# # c. List all clients who stay in ‘Bangalore’ or ‘Mangalore’.
# # d. List all clients whose BalDue is greater than value 10000.
# # e. List all information from the Sales_order table for order placed in the month of June.
# # f. List the Order No & day on which clients placed their order.
# # g. List the names, city and state of clients who are not in the state of ‘Maharashtra’.


# import mysql
# import mysql.connector

# try:
#     conn = mysql.connector.connect(host='localhost', database='pgdai_database', user='root', password='cdac123')
#     if conn.is_connected():
#         # print(conn.get_server_info())
#         cursor = conn.cursor()


#         print("\nList the names of all clients having 'a' as the second letter in their names")
#         q1 = """SELECT name FROM client_master WHERE name LIKE '_a%'"""
#         cursor.execute(q1)
#         result = cursor.fetchall()
#         print(result)


#         print("\nList the clients who stay in a city whose first letter is 'M'.")
#         q2 = """SELECT name FROM client_master WHERE city LIKE 'M%';"""
#         cursor.execute(q2)
#         result = cursor.fetchall()
#         print(result)


#         print("\nList all clients who stay in 'Bangalore' or 'Mangalore'.")
#         q3 = """SELECT name FROM client_master WHERE city LIKE 'Bangalore' OR city LIKE 'Mangalore';"""
#         cursor.execute(q3)
#         result = cursor.fetchall()
#         print(result)


#         print("\nList all clients whose BalDue is greater than value 10000.")
#         q4 = """SELECT name FROM client_master WHERE baldue > 10000;"""
#         cursor.execute(q4)
#         result = cursor.fetchall()
#         print(result)


#         print("List all information from the Sales_order table for order placed in the month of June.")
#         q5 = """SELECT * FROM sales_order WHERE MONTH(orderdate) = 6;"""
#         cursor.execute(q5)
#         result = cursor.fetchall()
#         print(result)


#         print("\nList the Order No & day on which clients placed their order.")
#         q6 = """SELECT sod.orderno, DAY(so.orderdate) FROM sales_order_details sod, sales_order so;"""
#         cursor.execute(q6)
#         result = cursor.fetchall()
#         print(result)


#         print("List the names, city and state of clients who are not in the state of ‘Maharashtra’.")
#         q7 = """SELECT name, city, state FROM client_master WHERE state NOT LIKE 'Maharashtra';"""
#         cursor.execute(q7)
#         result = cursor.fetchall()
#         print(result)


#         cursor.close()
#         conn.close()


# except mysql.connector.Error as e:
#     print("Error: ", e)


# Exercises on Using Having, Group By and Joins in Python IDLE:
# a. Printing the description and total quantity sold for each product.
# b. Calculating the average quantity sold for each client that has a maximum order value of 15000.00.
import mysql
import mysql.connector

try:
    conn = mysql.connector.connect(host='localhost', database='pgdai_database', user='root', password='cdac123')
    if conn.is_connected():
        # print(conn.get_server_info())
        cursor = conn.cursor()


        cursor.close()
        conn.close()


except mysql.connector.Error as e:
    print("Error: ", e)

