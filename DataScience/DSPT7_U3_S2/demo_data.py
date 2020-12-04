"""Module for SQL Sprint"""
import sqlite3


create_demo_data_table = """
    CREATE TABLE demo(
        s, x, y);
    """

insert_demo_data = """
    INSERT INTO demo (
        s, x, y)
    VALUES
        ('g', 3, 9),
        ('v', 5, 7),
        ('f', 8, 7);
    """
    
query_1 = """
    SELECT COUNT(*) FROM demo;
    """
    
query_2 = """
    SELECT * FROM demo
    WHERE x >= 5 
    AND y >= 5;
    """

query_3 = """
    SELECT COUNT( DISTINCT y ) FROM demo;
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
    new_database = r'demo_data.sqlite3'
    
    context_arr = [
        "Row Count:\n",
        "All data >= 5 in x, y column:\n",
        "Count of unique y values:\n"]
    
    query_arr = [
        query_1,
        query_2,
        query_3]
    
    connection, cursor = database_connector(new_database)
    
    cursor.execute(create_demo_data_table)
    cursor.execute(insert_demo_data)
    query_output(context_arr, query_arr, cursor)
    
    connection.commit()
    connection.close()
    

if __name__ == "__main__":
    main()
