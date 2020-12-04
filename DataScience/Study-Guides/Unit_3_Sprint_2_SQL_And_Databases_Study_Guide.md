# Unit 3 Sprint 2 SQL and Databases Study Guide
​
This study guide should reinforce and provide practice for all of the concepts you have seen in the past week. There are a mix of written questions and coding exercises, both are equally important to prepare you for the sprint challenge as well as to be able to speak on these topics comfortably in interviews and on the job.
​
If you get stuck or are unsure of something remember the 20 minute rule. If that doesn't help, then research a solution with [google](https://www.google.com) or [StackOverflow](https://www.stackoverflow.com). Only once you have exhausted these methods should you turn to your Team Lead - they won't be there on your SC or during an interview. That being said, don't hesitate to ask for help if you truly are stuck.
​
Have fun studying!
​
## SQL
​
**Concepts:**
​
1. What is SQL? **Structured Query Language**
2. What is a RDBMS? **Relational Database Management System**
3. What is an ETL pipeline? **Extract Transfom Load**
4. What is a schema? **Blueprint of a relational database**
5. What does each letter in ACID stand for? Give an explanation for each and why they matter?
	- **A**tomocity: Ensures completion or does not occur at all
	- **C**onsistency: Ensures that integrity constraints are maintained
	- **I**solation: Ensures that multiple transactions can occur simultaneously without causing any inconsistency.
	- **D**urability: Ensures that that changes exist permanently and are never lost.
6. Explain each of the table relationships and give an example for each
	- One-to-One **A `one-to-one` relationship is mostly used to split an entity in two to provide information concisely and make it more understandable.**
	- One-to-Many **A `one-to-many` relationship refers to the relationship between two entities X and Y in which an instance of X may be linked to many instances of Y, but not the other way around.**
	- Many-to-Many **A `many-to-many` relationship refers to the relationship between two entities X and Y in which X may be linked to many instances of Y and vise versa.** 
​
## Syntax
For the following section, give a brief explanation of each of the SQL commands.
​
1. **SELECT** - select columns from a table
2. **WHERE** - specify a condition for the query
3. **LIMIT** - set the amount of rows to return
4. **ORDER** - sort the data
5. **JOIN** - combine queries from seperate tables
6. **CREATE TABLE** - create a new table in a database
7. **INSERT** - put values into a table
8. **DISTINCT** - get unique rows with no duplicates
9. **GROUP BY** - groups rows that have the same values into summary roles
10. **ORDER BY** - sort the data by a specific column
11. **AVG** - get the average value in a column
12. **MAX** - get the max value in a column
13. **AS** - set an alias for a query item
​
## Starting From Scratch
Create a file named `study_part1.py` and complete the exercise below. The only library you should need to import is `sqlite3`. Don't forget to be PEP8 compliant!
1. Create a new database file call `study_part1.sqlite3`
2. Create a table with the following columns
    ```
    student - string
    studied - string
    grade - int
    age - int
    sex - string
    ```
​
3. Fill the table with the following data
​
    ```
    'Lion-O', 'True', 85, 24, 'Male'
    'Cheetara', 'True', 95, 22, 'Female'
    'Mumm-Ra', 'False', 65, 153, 'Male'
    'Snarf', 'False', 70, 15, 'Male'
    'Panthro', 'True', 80, 30, 'Male'
    ```
​
4. Save your data. You can check that everything is working so far if you can view the table and data in DBBrowser
​
5. Write the following queries to check your work. Querie outputs should be formatted for readability, don't simply print a number to the screen with no explanation, add context.
​
    ```
    What is the average age? Expected Result - 48.8
    What are the name of the female students? Expected Result - 'Cheetara'
    How many students studied? Expected Results - 3
    Return all students and all columns, sorted by student names in alphabetical order.
    ```
​
## Query All the Tables!
​
### Setup
Before we get started you'll need a few things.
1. Download the [Chinook Database here](https://github.com/bundickm/Study-Guides/blob/master/data/Chinook_Sqlite.sqlite)
2. The schema can be [found here](https://github.com/bundickm/Study-Guides/blob/master/data/Chinook%20Schema.png)
3. Create a file named `study_part2.py` and complete the exercise below. The only library you should need to import is `sqlite3`. Don't forget to be PEP8 compliant!
4. Add a connection to the chinook database so that you can answer the queries below. 
​
### Queries
**Single Table Queries**
1. Find the average invoice total for each customer, return the details for the first 5 ID's
2. Return all columns in Customer for the first 5 customers residing in the United States
3. Which employee does not report to anyone?
4. Find the number of unique composers
5. How many rows are in the Track table?
​
**Joins**
6. Get the name of all Black Sabbath tracks and the albums they came off of
7. What is the most popular genre by number of tracks?
8. Find all customers that have spent over $45
9. Find the first and last name, title, and the number of customers each employee has helped. If the customer count is 0 for an employee, it doesn't need to be displayed. Order the employees from most to least customers.
10. Return the first and last name of each employee and who they report to
​
## NoSQL
​
### Questions of Understanding
​
1. What is a document store? 
- **A document store is a document-oriented database.**
2. What is a `key:value` pair? What data type in Python uses `key:value` pairs?
​- **key value pairs are handy for retriveing a values by one name or key. Dictionaries**
3. Give an example of when it would be best to use a SQL Database and when it would be best to use a NoSQL Database
​- **Use NoSQL if you are constatly adding new features, functions, data types, and it's difficult to predict how the application will grow over time.**
- **Use SQL when dealing with complex queries and reports. If you will have high transaction application or you dont anticipate a lot of changes or growth**
4. What are some of the trade-offs between SQL and NoSQL?
​- ****
5. What does each letter in BASE stand for? Give an explanation for each and why they matter?
    - B.asic 
    - A.vailabillity
        - database works most of the time
    - S.oft-state
        - stores don't have to be write-consistent, nor do different replicas have to be mutually consistent all the time.
    - E.ventual consistency
        - stores exhibit consistency at some later point
