"""Module to create a sqlite3 database call school"""
import sqlite3


def main():
    conn = sqlite3.connect(r'study_part1.sqlite3')
    cur = conn.cursor()
    
    cur.execute("DROP TABLE school;")
    
    cur.execute(
        """
        CREATE TABLE school(
            student string,
            studied string,
            grade int,
            age int,
            sex string );
        """)
    
    cur.execute(
        """
        INSERT INTO school(
            student, studied, grade, age, sex)
        VALUES
            ('Lion-O', 'True', 85, 24, 'Male'),
            ('Cheetara', 'True', 95, 22, 'Female'),
            ('Mumm-Ra', 'False', 65, 153, 'Male'),
            ('Snarf', 'False', 70, 15, 'Male'),
            ('Panthro', 'True', 80, 30, 'Male');
        """)
    
    conn.commit()
            
    ans1 = cur.execute("SELECT * FROM school;").fetchall()
    print(f"All data from table: \n{ans1[0]}\n{ans1[1]}\n{ans1[2]}\n{ans1[3]}\n")
    
    ans2 = cur.execute("SELECT AVG(age) FROM school;").fetchall()
    print(f"The average age of students is: {ans2[0][0]}\n")
    
    ans3 = cur.execute("SELECT COUNT(studied) FROM school WHERE studied = 'True';").fetchall()
    print(f"Total amount of students that studied: {ans3[0][0]}\n")
    
    ans4 = cur.execute("SELECT student, * FROM school ORDER BY student;").fetchall()
    print(f"Student list in alphabetical order: \n{ans4[0]}\n{ans4[1]}\n{ans4[2]}\n{ans4[3]}\n")
    
    conn.close()
    
    
if __name__ == "__main__":
    main()
    
    

