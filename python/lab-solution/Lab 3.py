"""
## Lab Challange

**Challenge: Student Class with GPA Calculation, Inheritance, and Polymorphism**

**Task:**
1. Create a Student class that represents a student with attributes like name, student ID, and grades in different subjects. Implement methods to calculate the GPA (Grade Point Average) of the student based on their grades.
1. Extend the Student class to represent specific types of students (e.g., Undergraduate and Graduate students) to demonstrate inheritance.
1. Implement polymorphism to handle GPA calculations differently for each type of student (e.g., using different weightings for undergraduate and graduate students).

**Steps to Follow:**
1. Create a Student class with:
    - Attributes: name, student_id, and grades (a dictionary containing subject names and their corresponding grades).
    - A method calculate_gpa to calculate the GPA based on grades.
1. Extend the Student class to create subclasses Undergraduate and Graduate, where:
    - The Undergraduate class uses a different method for calculating the GPA (e.g., equal weights for all subjects).
    - The Graduate class gives more weight to certain subjects for GPA calculation.
1. Demonstrate polymorphism by overriding the calculate_gpa method in the Undergraduate and Graduate subclasses to calculate the GPA differently.
"""

# Base class: Student
class Student:
    def __init__(self, name, student_id, grades):
        """
        Initialize a student with a name, ID, and grades (dictionary of subject: grade).
        """
        self.name = name
        self.student_id = student_id
        self.grades = grades

    def calculate_gpa(self):
        """
        Calculate GPA for the student. GPA is an average of the grades.
        """
        total_points = sum(self.grades.values())  # Sum of all grades
        num_subjects = len(self.grades)  # Number of subjects
        return total_points / num_subjects if num_subjects > 0 else 0  # Avoid division by zero

    def __str__(self):
        return f"Student: {self.name}, ID: {self.student_id}"


# Inherited class: Undergraduate
class Undergraduate(Student):
    def __init__(self, name, student_id, grades):
        """
        Initialize an undergraduate student, inherits from the Student class.
        """
        super().__init__(name, student_id, grades)  # Call the parent constructor

    def calculate_gpa(self):
        """
        Calculate GPA for an undergraduate student. GPA is an average of the grades.
        """
        total_points = sum(self.grades.values())  # Sum of all grades
        num_subjects = len(self.grades)  # Number of subjects
        return total_points / num_subjects if num_subjects > 0 else 0  # Simple average


# Inherited class: Graduate
class Graduate(Student):
    def __init__(self, name, student_id, grades):
        """
        Initialize a graduate student, inherits from the Student class.
        """
        super().__init__(name, student_id, grades)  # Call the parent constructor

    def calculate_gpa(self):
        """
        Calculate GPA for a graduate student with weighted grades.
        For simplicity, assume that the first subject has more weight.
        """
        subjects = list(self.grades.values())
        # Assume the first subject has double the weight of others
        weighted_sum = (subjects[0] * 2) + sum(subjects[1:])  # Double the first subject's grade
        weighted_gpa = weighted_sum / (len(subjects) + 1)  # Normalizing by total number of subjects + 1 for the extra weight
        return weighted_gpa


# Example Usage:
# Create students with a dictionary of grades
undergrad_grades = {"Math": 3.5, "English": 4.0, "History": 3.0}
grad_grades = {"Math": 4.0, "Research": 3.8, "Computer Science": 4.2}

# Create objects for Undergraduate and Graduate
undergrad = Undergraduate("Alice", 12345, undergrad_grades)
grad = Graduate("Bob", 67890, grad_grades)

# Calculate and print their GPAs
print(undergrad)  # Printing student details
print(f"GPA of {undergrad.name}: {undergrad.calculate_gpa():.2f}")

print(grad)  # Printing student details
print(f"GPA of {grad.name}: {grad.calculate_gpa():.2f}")