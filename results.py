from database import connect_database


def results(student):

    print("\n" + "=" * 80)
    print("                              RESULTS")
    print("=" * 80)

    connection = connect_database()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            sub.subject_name,
            r.internal_marks,
            r.external_marks,
            r.total_marks,
            r.grade,
            r.grade_point,
            r.result_status
        FROM results r
        JOIN subjects sub
            ON r.subject_id = sub.subject_id
        WHERE r.student_id = %s
        ORDER BY r.subject_id
    """, (student["student_id"],))

    results_data = cursor.fetchall()

    if not results_data:
        print("No result records found.")
        cursor.close()
        connection.close()
        return

    print(
        f"{'Subject':<30}"
        f"{'Internal':<10}"
        f"{'External':<10}"
        f"{'Total':<8}"
        f"{'Grade':<8}"
        f"{'GP':<8}"
        f"{'Status':<8}"
    )

    print("-" * 80)

    for record in results_data:
        print(
            f"{record['subject_name']:<30}"
            f"{record['internal_marks']:<10}"
            f"{record['external_marks']:<10}"
            f"{record['total_marks']:<8}"
            f"{record['grade']:<8}"
            f"{record['grade_point']:<8}"
            f"{record['result_status']:<8}"
        )

    cursor.close()
    connection.close()