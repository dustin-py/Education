"""Module for querying northwind_small.sqlite3"""
import sqlite3

query_1 = """
    SELECT productname FROM product
    ORDER BY unitprice DESC
    LIMIT 10;
    """
    
query_2 = """
    SELECT 
        AVG( hiredate - birthdate ) AS average_age
    FROM employee;
    """

query_3 = """
    SELECT 
	    city,        
	    AVG( hiredate - birthdate ) AS average_age
    FROM employee
    GROUP BY city;
    """
    
query_4 = """
    SELECT 
        product.productname as top_10,
        supplier.companyname as supplier
    FROM product
    JOIN supplier
    ON product.id = supplier.id
    ORDER BY unitprice DESC
    LIMIT 10;
    """

query_5 = """
    SELECT
        category.categoryname, 
        COUNT( DISTINCT productname ) as product_count
    FROM product
    JOIN category
    ON product.categoryid = category.id
    GROUP BY product.categoryid
    ORDER BY product_count DESC
    LIMIT 1;
    """


def database_connector(database):
    """[connect to sqlite3 database]
    
    Args:
        database ([string]): [database to connect to.]

    Returns:
        [connection]: [the data base connection]
        [cursor]: [allows communication with the connected database]
    """
    connection = sqlite3.connect(database=database)
    cursor = connection.cursor()
    return connection, cursor


def query_output(context_arr, query_arr, cursor):
    """[Outputs queried data]

    Args:
        context_arr ([list]): [list of strings to describe the query ouputs]
        query_arr ([list]): [list of queries to execute]
        cursor ([connection cursor]): [used to query the data]
    """
    for e, query in enumerate(query_arr):
        q = cursor.execute(query).fetchall()
        a = context_arr[e]
        print(f"{a} {q}\n")


def main():
    database = r'northwind_small.sqlite3'
    context_arr = [
        "Ten most expensive items:\n",
        "Average age of employee at time of hiring:\n",
        "Average hire age by city:\n",
        "Most expensive item per unit price and thier supplier:\n",
        "Largest category by number of unique products:\n",
    ]
    query_arr = [
        query_1, query_2, query_3,
        query_4, query_5,
    ]
    connection, cursor = database_connector(database)
    query_output(context_arr, query_arr, cursor)
    
    connection.close()
    
    
if __name__ == "__main__":
    main()
