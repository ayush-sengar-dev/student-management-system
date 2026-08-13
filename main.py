import mysql.connector

from login import login
from student import student_details
from attendance import attendance
from results import results 
from fees import fees
from timetable import timetable
from notices import notices


def dashboard(student):

    while True:

        print("\n")
        print("=" * 60)
        print("              STUDENT MANAGEMENT SYSTEM")
        print("=" * 60)

        print(f"Welcome, {student['name']}")
        print(
            f"Course: {student['course']} | "
            f"Semester: {student['semester']}"
        )

        print("-" * 60)

        print("1. Student Details")
        print("2. Attendance")
        print("3. Results")
        print("4. Fees")
        print("5. Timetable")
        print("6. Notices")
        print("7. Logout")

        print("-" * 60)

        choice = input("Enter your choice: ")

        if choice == "1":
            student_details(student)

        elif choice == "2":
            attendance(student)

        elif choice == "3":
            results(student)

        elif choice == "4":
            fees(student)

        elif choice == "5":
            timetable(student)

        elif choice == "6":
            notices()

        elif choice == "7":
            print("\nLogged out successfully.")
            break

        else:
            print("\nInvalid choice.")

        input("\nPress Enter to continue...")


def main():

    print("=" * 60)
    print("             STUDENT MANAGEMENT SYSTEM")
    print("               Python + MySQL")
    print("=" * 60)
    print("              Created by Ayush Sengar")

    try:

        while True:

            student = login()

            if student:
                dashboard(student)

            again = input("\nLogin again? (y/n): ").lower()

            if again != "y":
                print("\nThank you for using Student Management System.")
                break

    except mysql.connector.Error as error:

        print("\nMySQL Error:", error)
        print("Check that MySQL is running and your credentials are correct.")

    except Exception as error:

        print("\nError:", error)


if __name__ == "__main__":
    main()