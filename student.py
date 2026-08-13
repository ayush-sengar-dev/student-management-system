def student_details(student):
    """Display complete student information."""

    print("\n" + "=" * 50)
    print("              STUDENT DETAILS")
    print("=" * 50)

    print("Student ID      :", student["student_id"])
    print("Enrollment No.  :", student["enrollment_no"])
    print("Name            :", student["name"])
    print("Email           :", student["email"])
    print("Phone           :", student["phone"])
    print("Department      :", student["department"])
    print("Course          :", student["course"])
    print("Semester        :", student["semester"])
    print("Admission Year  :", student["admission_year"])
    print("Date of Birth   :", student["date_of_birth"])
    print("Address         :", student["address"])