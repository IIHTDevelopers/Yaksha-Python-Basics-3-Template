# student_management.py

# Function 1: Student Names
def student_names():
    """
    Stores and displays a list of student names.

    Returns:
        list: List of student names.
    """
    # Sample Dataset
    students = ["John", "Emma", "Sophia", "Michael", "Daniel"]
    students.append("Olivia")  # Adding a new student

    # TODO: Implement logic to display and return student names
    pass  # Placeholder for the function body


# Function 2: Student Courses
def student_courses():
    """
    Stores student course enrollments using a dictionary.

    Returns:
        dict: Dictionary of student courses.
    """
    # Sample Dataset
    courses = {
        "John": ("Math", "Physics"),
        "Emma": ("Biology", "Chemistry"),
        "Sophia": ("History", "English"),
        "Michael": ("Math", "Computer Science"),
        "Daniel": ("Physics", "Chemistry")
    }
    courses["Olivia"] = ("Biology", "History")  # Adding a new student course

    # TODO: Implement logic to display and return student courses
    pass  # Placeholder for the function body


# Function 3: Unique Subjects
def unique_subjects():
    """
    Stores and displays unique subjects from all students using a set.

    Returns:
        set: Set of unique subjects.
    """
    # Sample Dataset
    all_subjects = {"Math", "Physics", "Biology", "Chemistry", "English", "History", "Computer Science", "Math"}
    all_subjects.add("Economics")  # Adding a new subject

    # TODO: Implement logic to display and return unique subjects
    pass  # Placeholder for the function body


# Execute the functions
if __name__ == "__main__":
    student_names()
    student_courses()
    unique_subjects()
