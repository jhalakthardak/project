# -------------------------------------------------------------
# Name: Jhalak Choudhary
# Date: 08-Nov-2025
# Roll no.: KRMU2532485
# Assignment Title: Attendance Tracker - Assignment 01
# Course: Programming for Problem Solving Using Python (ETCCPP171)
# -------------------------------------------------------------


from datetime import datetime

print("\nWelcome to the Attendance Tracker!")
print("This tool helps record student attendance efficiently.\n")


attendance = {}  

num_entries_input = input("Enter number of students to record: ")

if num_entries_input.isdigit():
    num_entries = int(num_entries_input)

    if num_entries > 0:
        count = 1
        while count <= num_entries:
            print(f"\n--- Entry {count} ---")

            name = input("Enter student name: ").strip()
            if name == "":
                print("Name cannot be empty. Skipping this entry.")
            elif name in attendance:
                print("Duplicate entry! This student is already recorded.")
            else:
                time = input("Enter check-in time: ").strip()
                if time == "":
                    print("Timestamp missing. Entry not recorded.")
                else:
                    attendance[name] = time
                    print("Entry recorded successfully.")
                    count += 1
    else:
        print("Number of entries must be greater than zero.")
else:
    print("Invalid input! Please enter a valid number for entries.")

print("\nAttendance Summary".center(45, "-"))
print(f"{'Student Name':20s}\t{'Check-in Time'}")
print("-" * 45)

if len(attendance) > 0:
    for name, time in attendance.items():
        print(f"{name:20s}\t{time}")
else:
    print("No attendance records found.")

print("-" * 45)
print(f"Total Students Present: {len(attendance)}")

choice = input("\nDo you want to calculate absentees? (yes/no): ").lower()
if choice == "yes":
    total_students_input = input("Enter total number of students in class: ")
    if total_students_input.isdigit():
        total_students = int(total_students_input)
        absentees = total_students - len(attendance)
        if absentees < 0:
            absentees = 0
        print(f"Total Present: {len(attendance)}")
        print(f"Total Absent: {absentees}")
    else:
        print("Invalid input! Please enter a valid number.")
else:
    print("Absentee calculation skipped.")

save_choice = input("\nDo you want to save this attendance record? (yes/no): ").lower()

if save_choice == "yes":
    if len(attendance) > 0:
        with open("attendance_log.txt", "w") as file:
            file.write("Attendance Report\n")
            file.write(f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n")
            file.write(f"{'Student Name':20s}\t{'Check-in Time'}\n")
            file.write("-" * 45 + "\n")
            for name, time in attendance.items():
                file.write(f"{name:20s}\t{time}\n")
            file.write("-" * 45 + "\n")
            file.write(f"Total Present: {len(attendance)}\n")
            if 'total_students' in locals():
                file.write(f"Total Absent: {absentees}\n")
        print("Attendance successfully saved to 'attendance_log.txt'!")
    else:
        print("No data to save.")
else:
    print("Data not saved.")

print("\nThank you for using the Attendance Tracker!\n")