import sqlite3


def reset_database(cursor):
    """Drop the students table if it exists."""
    cursor.execute('DROP TABLE IF EXISTS students')


def create_students_table(cursor):
    """Create the students table."""
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        grade INTEGER NOT NULL
    )
    ''')


def insert_initial_records(cursor):
    """Insert initial records into the students table."""
    cursor.executemany('''
    INSERT INTO students (name, grade)
    VALUES (?, ?)
    ''', [
        ('John Doe', 85),
        ('Jane Smith', 90),
        ('Alice Johnson', 75),
        ('Undertaker', 20),
        ('Majd Hassoun', 100)
    ])


def fetch_all_records(cursor):
    """Fetch and return all records from the students table."""
    cursor.execute('SELECT * FROM students')
    return cursor.fetchall()


def fetch_records_by_grade(cursor, grade):
    """Fetch and return records from the students table where grade is greater than the specified grade."""
    cursor.execute('SELECT * FROM students WHERE grade > ?', (grade,))
    return cursor.fetchall()


def update_student_grade(cursor, name, new_grade):
    """Update the grade of a student by name."""
    cursor.execute('UPDATE students SET grade = ? WHERE name = ?', (new_grade, name))


def delete_student_by_name(cursor, name):
    """Delete a student record by name."""
    cursor.execute('DELETE FROM students WHERE name = ?', (name,))


def main():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    # Reset the database
    reset_database(cursor)

    # Create the students table
    create_students_table(cursor)

    # Insert initial records
    insert_initial_records(cursor)

    # Commit the changes
    conn.commit()

    # Fetch and print all records initially
    all_students = fetch_all_records(cursor)
    print("All students first print:")
    for student in all_students:
        print(student)

    # Fetch and print records where grade is greater than 80
    results = fetch_records_by_grade(cursor, 80)
    print("\nAll students after >80 update:")
    for student in results:
        print(student)

    # Fetch and print records where grade is greater than 95
    results = fetch_records_by_grade(cursor, 95)
    print("\nAll students after >95 update:")
    for student in results:
        print(student)

    # Update the grade of one student
    update_student_grade(cursor, 'John Doe', 95)

    # Delete another student
    delete_student_by_name(cursor, 'Alice Johnson')

    # Commit the changes
    conn.commit()

    # Fetch and print all records to see the changes
    all_students = fetch_all_records(cursor)
    print("\nAll students after update and delete:")
    for student in all_students:
        print(student)

    # Drop the table to reset the database
    reset_database(cursor)

    # Close the connection
    conn.close()


if __name__ == "__main__":
    main()
