from database import connect_database


def login():
    print("\n" + "=" * 50)
    print("              STUDENT LOGIN")
    print("=" * 50)

    enrollment_no = input("Enrollment Number: ")
    password = input("Password: ")

    connection = connect_database()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM students
        WHERE enrollment_no = %s
        AND password = %s
    """, (enrollment_no, password))

    student = cursor.fetchone()

    cursor.close()
    connection.close()

    if student:
        print("\nLogin successful.")
        return student

    print("\nInvalid enrollment number or password.")
    return None