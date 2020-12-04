### Part 4 - Questions (and your Answers)

Answer the following questions, baseline ~3-5 sentences each, as if they were
interview screening questions (a form you fill when applying for a job):

- In the Northwind database, what is the type of relationship between the
  `Employee` and `Territory` tables?
  
  - **ANSWER**: 
    - The relationship between the two is considered a `many-to-many` relationship.
    This relationship  occurs when multiple records in a table are associated with multiple records in another table.

- What is a situation where a document store (like MongoDB) is appropriate, and
  what is a situation where it is not appropriate?
  
  - **ANSWER**:
    - Document Stores are best used when the growth is unpredictable and the data will constantly be scaled, but if
    we want consistancy with the data transactions, then document stores would not be the best choice.

- What is "NewSQL", and what is it trying to achieve?

  - **ANSWER**:
    - NewSQL is like a class of RDMS's that seek to provide the scalability of NoSQL (Document Store) systems for online transaction processing workloads while maintaining the ACID guarantees of a traditional database system.
