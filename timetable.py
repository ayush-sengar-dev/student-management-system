from database import connect_database


def timetable(student):

    print("\n" + "=" * 80)
    print("                              TIMETABLE")
    print("=" * 80)

    connection = connect_database()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            t.day_of_week,
            t.start_time,
            t.end_time,
            s.subject_name
        FROM timetable t
        JOIN subjects s
            ON t.subject_id = s.subject_id
        WHERE t.course = %s
          AND t.semester = %s
        ORDER BY
            FIELD(
                t.day_of_week,
                'Monday',
                'Tuesday',
                'Wednesday',
                'Thursday',
                'Friday'
            ),
            t.start_time
    """, (student["course"], student["semester"]))

    schedule = cursor.fetchall()

    cursor.close()
    connection.close()

    if not schedule:
        print("No timetable found.")
        return

    current_day = None

    for row in schedule:

        day = row["day_of_week"]

        if day != current_day:
            print(f"\n{day}")
            print("-" * 80)
            print(f"{'Time':<25}{'Subject'}")
            print("-" * 80)
            current_day = day

        start = str(row["start_time"])[:5]
        end = str(row["end_time"])[:5]

        time_slot = f"{start} - {end}"

        print(f"{time_slot:<25}{row['subject_name']}")