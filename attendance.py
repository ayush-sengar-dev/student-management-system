from database import connect_database


def attendance(student):

    print("\n" + "=" * 70)
    print("                         ATTENDANCE")
    print("=" * 70)

    connection = connect_database()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            sub.subject_name,
            COUNT(*) AS total_classes,
            SUM(a.status = 'Present') AS present_classes,
            ROUND(
                SUM(a.status = 'Present') / COUNT(*) * 100,
                2
            ) AS attendance_percentage
        FROM attendance a
        JOIN subjects sub
            ON a.subject_id = sub.subject_id
        WHERE a.student_id = %s
        GROUP BY sub.subject_id, sub.subject_name
        ORDER BY sub.subject_id
    """, (student["student_id"],))

    attendance_data = cursor.fetchall()

    print(
        f"{'Subject':<30}"
        f"{'Present':<10}"
        f"{'Total':<10}"
        f"{'Attendance':<12}"
    )

    print("-" * 70)

    for record in attendance_data:
        print(
            f"{record['subject_name']:<30}"
            f"{record['present_classes']:<10}"
            f"{record['total_classes']:<10}"
            f"{record['attendance_percentage']:.2f}%"
        )

    cursor.execute("""
        SELECT
            COUNT(*) AS total_classes,
            SUM(status = 'Present') AS present_classes,
            ROUND(
                SUM(status = 'Present') / COUNT(*) * 100,
                2
            ) AS overall_attendance
        FROM attendance
        WHERE student_id = %s
    """, (student["student_id"],))

    overall = cursor.fetchone()

    print("-" * 70)
    print(f"Overall Attendance: {overall['overall_attendance']:.2f}%")

    cursor.close()
    connection.close()