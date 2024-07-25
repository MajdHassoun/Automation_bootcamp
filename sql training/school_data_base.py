import sqlite3


class SchoolDatabase:
    def __init__(self, db_name='school.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def reset_database(self):
        """Drop the students table if it exists."""
        self.cursor.execute('DROP TABLE IF EXISTS students')
        self.conn.commit()

    def create_students_table(self):
        """Create the students table."""
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            grade INTEGER NOT NULL
        )
        ''')
        self.conn.commit()

    def insert_initial_records(self):
        """Insert initial records into the students table."""
        self.cursor.executemany('''
        INSERT INTO students (name, grade)
        VALUES (?, ?)
        ''', [
            ('John Doe', 85),
            ('Jane Smith', 90),
            ('Alice Johnson', 75),
            ('Undertaker', 20),
            ('Majd Hassoun', 100)
        ])
        self.conn.commit()

    def fetch_all_records(self):
        """Fetch and return all records from the students table."""
        self.cursor.execute('SELECT * FROM students')
        return self.cursor.fetchall()

    def fetch_records_by_grade(self, grade):
        """Fetch and return records from the students table where grade is greater than the specified grade."""
        self.cursor.execute('SELECT * FROM students WHERE grade > ?', (grade,))
        return self.cursor.fetchall()

    def update_student_grade(self, name, new_grade):
        """Update the grade of a student by name."""
        self.cursor.execute('UPDATE students SET grade = ? WHERE name = ?', (new_grade, name))
        self.conn.commit()

    def delete_student_by_name(self, name):
        """Delete a student record by name."""
        self.cursor.execute('DELETE FROM students WHERE name = ?', (name,))
        self.conn.commit()

    def close(self):
        """Close the database connection."""
        self.conn.close()


def main():
    db = SchoolDatabase()

    # Create the students table
    db.create_students_table()

    # Insert initial records
    db.insert_initial_records()

    # Fetch and print all records initially
    all_students = db.fetch_all_records()
    print("All students first print:")
    for student in all_students:
        print(student)

    # Fetch and print records where grade is greater than 80
    results = db.fetch_records_by_grade(80)
    print("\nAll students after >80 update:")
    for student in results:
        print(student)

    # Fetch and print records where grade is greater than 95
    results = db.fetch_records_by_grade(95)
    print("\nAll students after >95 update:")
    for student in results:
        print(student)

    # Update the grade of one student
    db.update_student_grade('John Doe', 95)

    # Delete another student
    db.delete_student_by_name('Alice Johnson')

    # Fetch and print all records to see the changes
    all_students = db.fetch_all_records()
    print("\nAll students after update and delete:")
    for student in all_students:
        print(student)

    db.reset_database()
    # Close the connection
    db.close()


if __name__ == "__main__":
    main()
