"""Module to connect and query chinook sqlite3"""
import sqlite3


def database_connector(database):
    connection = sqlite3.connect(database=database)
    cursor = connection.cursor()
    return connection, cursor


def query_sg_answers(context_arr, query_arr, cursor):
    for e, query in enumerate(query_arr):
        q = cursor.execute(query).fetchall()
        a = context_arr[e]
        print(f"{a} {q}\n")
        

def main():
    database = r'Chinook_Sqlite.sqlite'
    context_arr = (
        "Top 5 average invoice total per customer:",
        "First 5 customers from the US:",
        "Employees that don't report to anyone:",
        "Number of unique composers:",
        "Number of rows in track table:",
        "All black sabbath tracks:\n",
        "Most popular genre by num of tracks:\n",
        "All customers that spent more than $45:\n")
    
    query_array = (
        "SELECT customerid, total FROM invoice ORDER BY total LIMIT 5;",
        "SELECT * FROM customer WHERE country LIKE '%USA%' LIMIT 5;",
        "SELECT * FROM employee WHERE reportsto IS NULL;",
        "SELECT COUNT(DISTINCT composer) FROM track;",
        "SELECT COUNT(*) FROM track;",
        "SELECT \
            track.name, \
            album.title, \
            track.composer \
        FROM track \
        JOIN album \
        ON track.albumid = album.albumid \
        WHERE composer LIKE '%sabbath%';",
        "SELECT \
            genre.name, \
            COUNT(track.genreid) AS `genre_count` \
        FROM genre \
        JOIN track \
        ON genre.genreid = track.genreid \
        GROUP BY genre.name;",
        "SELECT \
            customer.lastname, \
            SUM(invoice.total) as sum_total \
        FROM invoice \
        JOIN customer \
        ON invoice.customerid = customer.customerid \
        GROUP BY invoice.customerid \
        HAVING sum_total > 45;")
    connection, cursor = database_connector(database=database)
    query_sg_answers(context_arr, query_array, cursor)
    connection.close()
    
    
if __name__ == "__main__":
    main()
    
# **Joins**
# 6. Get the name of all Black Sabbath tracks and the albums they came off of
# 7. What is the most popular genre by number of tracks?
# 8. Find all customers that have spent over $45
# 9. Find the first and last name, title, and the number of customers each employee has helped. If the customer count is 0 for an employee, it doesn't need to be displayed. Order the employees from most to least customers.
# 10. Return the first and last name of each employee and who they report to