"""
==============================
SMART STUDENT MANAGEMENT SYSTEM
==============================
Developed by:  Ali Raza
Enhanced Version with Input Re-prompting & Advanced Features
Feature: File Handling + Auto Grading + Data Analysis
File: students.txt
"""
# ==================== INPUT VALIDATION WITH RE-PROMPTING ====================

def get_valid_id(prompt="Enter ID: ", check_unique=True):
    """Get and validate student ID with re-prompting."""
    while True:
        id_input = input(prompt).strip()
        
        if not id_input:
            print("❌ ID cannot be empty!")
            continue
        
        if not id_input.isdigit():
            print("❌ ID must be a number!")
            continue
        
        if check_unique and is_duplicate_id(id_input):
            print("❌ ID already exists! Try another one.")
            continue
        
        return id_input


def get_valid_name(prompt="Enter Name: "):
    """Get and validate student name with re-prompting."""
    while True:
        name = input(prompt).strip()
        
        if not name:
            print("❌ Name cannot be empty!")
            continue
        
        if name.isdigit():
            print("❌ Name cannot be numeric only!")
            continue
        
        if not name.replace(" ", "").isalpha():
            print("❌ Invalid name! Only alphabets and spaces allowed.")
            continue
        
        return name


def get_valid_age(prompt="Enter Age: "):
    """Get and validate age with re-prompting."""
    while True:
        age = input(prompt).strip()
        
        if not age:
            print("❌ Age cannot be empty!")
            continue
        
        if not age.isdigit():
            print("❌ Age must be a number!")
            continue
        
        if int(age) <= 0:
            print("❌ Age must be greater than 0!")
            continue
        
        return age


def get_valid_marks(prompt="Enter Marks (0-100): "):
    """Get and validate marks with re-prompting."""
    while True:
        marks = input(prompt).strip()
        
        if not marks:
            print("❌ Marks cannot be empty!")
            continue
        
        if not marks.isdigit():
            print("❌ Marks must be a number!")
            continue
        
        marks_int = int(marks)
        if not (0 <= marks_int <= 100):
            print("❌ Marks must be between 0 and 100!")
            continue
        
        return marks


# ==================== AUTO GRADING SYSTEM ====================

def auto_grade(marks):
    """
    Automatically assign grade based on marks.
    
    Grading Scale:
    90-100: A+
    80-89:  A
    70-79:  B
    60-69:  C
    50-59:  D
    0-49:   F
    """
    marks = int(marks)
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


# ==================== FILE UTILITY FUNCTIONS ====================

def load_all_students():
    """Load all student records from file."""
    students = []
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                line = line.strip()
                if line:  # Skip empty lines
                    parts = line.split(",")
                    if len(parts) == 5:  # Valid record
                        students.append(parts)
    except FileNotFoundError:
        pass
    return students


def save_all_students(students):
    """Save all student records to file."""
    try:
        with open(FILENAME, "w") as f:
            for student in students:
                f.write(",".join(student) + "\n")
        return True
    except Exception as e:
        print(f"❌ Error saving data: {e}")
        return False


# ==================== CORE FUNCTIONS ====================

def add_student():
    """Add a new student with auto-calculated grade."""
    print("\n" + "="*50)
    print("📘 ADD NEW STUDENT RECORD")
    print("="*50)
    
    # Get validated inputs with automatic re-prompting
    student_id = get_valid_id()
    name = get_valid_name()
    age = get_valid_age()
    marks = get_valid_marks()
    
    # Auto-calculate grade
    grade = auto_grade(marks)
    
    # Save to file
    try:
        with open(FILENAME, "a") as f:
            f.write(f"{student_id},{name},{age},{grade},{marks}\n")
        print(f"\n✅ Student '{name}' added successfully!")
        print(f"   ID: {student_id} | Grade: {grade} | Marks: {marks}/100")
    except Exception as e:
        print(f"❌ Error: {e}")


def view_students():
    """View all student records in formatted table."""
    print("\n" + "="*50)
    print("📖 ALL STUDENT RECORDS")
    print("="*50)
    
    students = load_all_students()
    
    if not students:
        print("⚠️ No records found. Add some students first!")
        return
    
    print(f"\nTotal Students: {len(students)}")
    print(f"\n{'ID':<8} {'Name':<20} {'Age':<6} {'Grade':<8} {'Marks':<8}")
    print("-" * 60)
    
    for student in students:
        student_id, name, age, grade, marks = student
        print(f"{student_id:<8} {name:<20} {age:<6} {grade:<8} {marks:<8}")


def search_student():
    """Search for students by ID or name."""
    print("\n" + "="*50)
    print("🔍 SEARCH STUDENT")
    print("="*50)
    
    keyword = input("Enter ID or Name to search: ").strip().lower()
    
    if not keyword:
        print("❌ Search term cannot be empty!")
        return
    
    students = load_all_students()
    found = []
    
    for student in students:
        student_id, name, age, grade, marks = student
        if keyword in student_id.lower() or keyword in name.lower():
            found.append(student)
    
    if not found:
        print("❌ No matching records found.")
        return
    
    print(f"\n✅ Found {len(found)} record(s):\n")
    print(f"{'ID':<8} {'Name':<20} {'Age':<6} {'Grade':<8} {'Marks':<8}")
    print("-" * 60)
    
    for student in found:
        student_id, name, age, grade, marks = student
        print(f"{student_id:<8} {name:<20} {age:<6} {grade:<8} {marks:<8}")


def update_student():
    """Update student record with option to skip fields."""
    print("\n" + "="*50)
    print("✏️ UPDATE STUDENT RECORD")
    print("="*50)
    
    # Get student ID to update (don't check uniqueness)
    target_id = get_valid_id(check_unique=False)
    
    # Load all students
    students = load_all_students()
    student_index = None
    
    for i, student in enumerate(students):
        if student[0] == target_id:
            student_index = i
            break
    
    if student_index is None:
        print(f"❌ Student with ID {target_id} not found.")
        return
    
    # Show current record
    old_student = students[student_index]
    print(f"\n📋 Current Record:")
    print(f"   ID: {old_student[0]}")
    print(f"   Name: {old_student[1]}")
    print(f"   Age: {old_student[2]}")
    print(f"   Grade: {old_student[3]}")
    print(f"   Marks: {old_student[4]}")
    
    # Ask what to update
    print("\n📝 Update Options:")
    print("1. Update All Fields")
    print("2. Update Name Only")
    print("3. Update Age Only")
    print("4. Update Marks Only (Grade will recalculate)")
    
    while True:
        choice = input("\nChoose option (1-4): ").strip()
        if choice in ['1', '2', '3', '4']:
            break
        print("❌ Invalid choice! Enter 1, 2, 3, or 4.")
    
    # Get new values based on choice
    if choice == '1':
        name = get_valid_name("Enter New Name: ")
        age = get_valid_age("Enter New Age: ")
        marks = get_valid_marks("Enter New Marks: ")
        grade = auto_grade(marks)
    elif choice == '2':
        name = get_valid_name("Enter New Name: ")
        age = old_student[2]
        marks = old_student[4]
        grade = old_student[3]
    elif choice == '3':
        name = old_student[1]
        age = get_valid_age("Enter New Age: ")
        marks = old_student[4]
        grade = old_student[3]
    else:  # choice == '4'
        name = old_student[1]
        age = old_student[2]
        marks = get_valid_marks("Enter New Marks: ")
        grade = auto_grade(marks)
        print(f"📊 Recalculated Grade: {grade}")
    
    # Update record
    students[student_index] = [target_id, name, age, grade, marks]
    
    if save_all_students(students):
        print("✅ Record updated successfully!")
    else:
        print("❌ Failed to update record.")


def delete_student():
    """Delete a student record with confirmation."""
    print("\n" + "="*50)
    print("🗑️ DELETE STUDENT RECORD")
    print("="*50)
    
    # Get student ID to delete
    target_id = get_valid_id(check_unique=False)
    
    # Load all students
    students = load_all_students()
    student_to_delete = None
    
    for student in students:
        if student[0] == target_id:
            student_to_delete = student
            break
    
    if not student_to_delete:
        print(f"❌ No record found with ID {target_id}.")
        return
    
    # Show record and confirm
    print(f"\n⚠️ Student to Delete:")
    print(f"   ID: {student_to_delete[0]}")
    print(f"   Name: {student_to_delete[1]}")
    print(f"   Age: {student_to_delete[2]}")
    print(f"   Grade: {student_to_delete[3]}")
    print(f"   Marks: {student_to_delete[4]}")
    
    confirm = input("\n❓ Are you sure? Type 'yes' to confirm: ").strip().lower()
    
    if confirm == 'yes':
        students = [s for s in students if s[0] != target_id]
        if save_all_students(students):
            print("✅ Record deleted successfully!")
        else:
            print("❌ Failed to delete record.")
    else:
        print("❌ Deletion cancelled.")


def analyze_data():
    """Comprehensive data analysis with statistics."""
    print("\n" + "="*50)
    print("📊 STUDENT DATA ANALYSIS REPORT")
    print("="*50)
    
    students = load_all_students()
    
    if not students:
        print("⚠️ No records to analyze. Add some students first!")
        return
    
    # Extract data
    marks_list = [int(s[4]) for s in students]
    total_students = len(students)
    
    # Calculate statistics
    avg = sum(marks_list) / total_students
    highest = max(marks_list)
    lowest = min(marks_list)
    
    # Find top performer
    top_students = [s for s in students if int(s[4]) == highest]
    top_name = top_students[0][1]
    
    # Count below average
    below_avg = sum(1 for m in marks_list if m < avg)
    
    # Grade distribution
    grade_counts = {}
    for student in students:
        grade = student[3]
        grade_counts[grade] = grade_counts.get(grade, 0) + 1
    
    # Pass/Fail analysis (50 is passing)
    passed = sum(1 for m in marks_list if m >= 50)
    failed = total_students - passed
    pass_rate = (passed / total_students) * 100
    
    # Display results
    print(f"\n📈 OVERALL STATISTICS")
    print("-" * 50)
    print(f"Total Students: {total_students}")
    print(f"Average Marks: {avg:.2f}")
    print(f"Top Performer: {top_name} ({highest} marks)")
    print(f"Students Below Average: {below_avg}")
    print(f"Highest Marks: {highest} | Lowest: {lowest}")
    print(f"Pass Rate: {pass_rate:.1f}% ({passed}/{total_students})")
    
    print(f"\n📊 GRADE DISTRIBUTION")
    print("-" * 50)
    for grade in sorted(grade_counts.keys(), reverse=True):
        count = grade_counts[grade]
        percentage = (count / total_students) * 100
        bar = "█" * int(percentage / 5)
        print(f"{grade:>3}: {count:3d} students ({percentage:5.1f}%) {bar}")
    
    # Top 5 students
    print(f"\n🌟 TOP 5 STUDENTS")
    print("-" * 50)
    sorted_students = sorted(students, key=lambda s: int(s[4]), reverse=True)[:5]
    print(f"{'Rank':<6} {'Name':<20} {'ID':<8} {'Grade':<8} {'Marks':<8}")
    print("-" * 50)
    for i, student in enumerate(sorted_students, 1):
        print(f"{i:<6} {student[1]:<20} {student[0]:<8} {student[3]:<8} {student[4]:<8}")


def show_grading_scale():
    """Display the grading scale."""
    print("\n" + "="*50)
    print("📖 GRADING SCALE")
    print("="*50)
    print("\n Marks Range  |  Grade  |  Description")
    print("-" * 50)
    print("   90 - 100   |   A+    |  Outstanding")
    print("   80 - 89    |   A     |  Excellent")
    print("   70 - 79    |   B     |  Very Good")
    print("   60 - 69    |   C     |  Good")
    print("   50 - 59    |   D     |  Satisfactory")
    print("   0  - 49    |   F     |  Fail")
    print("-" * 50)
    print("\n💡 Grades are automatically calculated from marks!")


# ==================== MAIN MENU ====================

def display_menu():
    """Display main menu."""
    print("\n" + "="*50)
    print("🎓 SMART STUDENT MANAGEMENT SYSTEM")
    print("   Auto Grading • File Storage • Analytics")
    print("="*50)
    print("1. ➕ Add Student")
    print("2. 📖 View All Students")
    print("3. 🔍 Search Student")
    print("4. ✏️  Update Student")
    print("5. 🗑️  Delete Student")
    print("6. 📊 Analyze Data")
    print("7. 📖 GRADING SCALE ")
    print("8. 🚪 Exit")
    print("="*50)


def main():
    """Main program loop."""
    print("\n" + "="*60)
    print("        SMART STUDENT MANAGEMENT SYSTEM")
    print("        Developed by: Muhammad Zarq Ali")
    print("="*60)
    print("✨ Features: Auto Grading | Data Analysis | File Storage")
    print("="*60)
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            analyze_data()
        elif choice == '7':
            show_grading_scale()
        elif choice == '8':
            print("\n" + "="*50)
            print("🙏 Thank you for using the system!")
            print("   Goodbye! 👋")
            print("="*50 + "\n")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1-8.")
        
        input("\n⏎ Press Enter to continue...")


# ==================== RUN PROGRAM ====================

if __name__ == "__main__":
    main()