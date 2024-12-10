"""
***
## Lab Challenge: Student Grade Calculator

Create a Python program to calculate the grade of students based on their marks in multiple subjects. The program will:

1. Read student data (name and marks for 3 subjects) from a CSV file.
1. Calculate the average marks.
1. Assign a grade based on the average:
    - A: 90-100
    - B: 80-89
    - C: 70-79
    - D: 60-69
    - F: Below 60
1. Write the results, including the student's name, marks, average, and grade, to another CSV file.

**Sample Data**:
<pre>
Name,Subject1,Subject2,Subject3
Alice,85,90,88
Bob,72,65,78
Charlie,95,92,91
David,80,75,82
Eva,88,92,90
</pre>

**Expected Output**:
<pre>
Name,Subject1,Subject2,Subject3,Average,Grade
Alice,85,90,88,87.67,B
Bob,72,65,78,71.67,C
Charlie,95,92,91,92.67,A
David,80,75,82,79.0,C
Eva,88,92,90,90.0,A
</pre>

**Steps:**
1. Setup Input File: Create a CSV file (students.csv) with student names and marks in 3 subjects.
1. Read Data: Use Python's csv module to read the input file.
1. Calculate Results:
    - Compute the average of the 3 subject marks.
    - Assign grades based on the average.
1. Write Results: Write the results to a new CSV file (grades.csv), including the calculated average and grade.
1. Test and Validate: Run the program with multiple input scenarios to ensure accuracy.
"""

import csv

class StudentGradesProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    # Function to calculate grade based on average score
    def calculate_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    # Function to process the student grades
    def process_grades(self):
        # Open the input file and output file
        with open(self.input_file, 'r') as infile, open(self.output_file, 'w', newline='') as outfile:
            reader = csv.DictReader(infile)  # Read the CSV file as a dictionary
            fieldnames = reader.fieldnames + ['Average', 'Grade']  # Add Average and Grade columns
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()  # Write the header row to the output file

            # Process each student row
            for row in reader:
                # Extract the grades (assuming the grades are in columns 'Grade1', 'Grade2', 'Grade3', etc.)
                grades = [int(row[field]) for field in row if field.startswith('Grade')]
                
                if grades:  # If there are grades in the row
                    average = sum(grades) / len(grades)  # Calculate average
                    grade = self.calculate_grade(average)  # Calculate letter grade
                    row['Average'] = round(average, 2)  # Round to 2 decimal places
                    row['Grade'] = grade  # Add the grade to the row

                    # Write the row to the output file with average and grade
                    writer.writerow(row)

        print(f"Results written to {self.output_file}")

# Example usage
input_file = 'student_grades.csv'  # Replace with your input file path
output_file = 'student_results.csv'  # Replace with your output file path

# Create an instance of StudentGradesProcessor
processor = StudentGradesProcessor(input_file, output_file)

# Process the student grades and write the results
processor.process_grades()


"""
**Further challange**

*Challenge Tasks:*
- Task 1: Extend the grading criteria to include plus/minus grades (e.g., A+, B-).
- Task 2: Add error handling to ensure all marks are valid integers between 0 and 100.
- Task 3: Allow the user to enter the name of the input and output files at runtime.
- Task 4: Sort the output file by grades (descending order) or names (alphabetical order).
"""

"""

import csv

def calculate_grade(average):
    '''Determine the grade based on average marks with plus/minus grades.'''
    if 97 <= average <= 100:
        return 'A+'
    elif 90 <= average < 97:
        return 'A'
    elif 87 <= average < 90:
        return 'B+'
    elif 80 <= average < 87:
        return 'B'
    elif 77 <= average < 80:
        return 'C+'
    elif 70 <= average < 77:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'

def validate_marks(marks):
    '''Validate that all marks are integers between 0 and 100.'''
    try:
        marks = [int(mark) for mark in marks]
        if all(0 <= mark <= 100 for mark in marks):
            return marks
        else:
            raise ValueError("Marks must be between 0 and 100.")
    except ValueError as e:
        print(f"Error: {e}")
        return None

def main():
    # Get input and output file names from the user
    input_file = input("Enter the name of the input CSV file (e.g., students.csv): ").strip()
    output_file = input("Enter the name of the output CSV file (e.g., grades.csv): ").strip()

    try:
        # Read input file
        with open(input_file, 'r') as infile:
            reader = csv.DictReader(infile)
            results = []

            for row in reader:
                # Validate and parse marks
                marks = validate_marks([row['Subject1'], row['Subject2'], row['Subject3']])
                if marks is None:
                    continue  # Skip invalid rows

                # Calculate average and grade
                average = sum(marks) / len(marks)
                grade = calculate_grade(average)

                # Append results with calculated data
                row['Average'] = round(average, 2)
                row['Grade'] = grade
                results.append(row)

        # Sort results (by grade descending, then name alphabetically)
        results.sort(key=lambda x: (-calculate_grade_rank(x['Grade']), x['Name']))

        # Write to output file
        with open(output_file, 'w', newline='') as outfile:
            fieldnames = ['Name', 'Subject1', 'Subject2', 'Subject3', 'Average', 'Grade']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)

        print(f"Grades have been successfully written to {output_file}.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except KeyError as e:
        print(f"Error: Missing column in input file - {e}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def calculate_grade_rank(grade):
    '''Map grades to numerical ranks for sorting.'''
    grade_rank = {
        'A+': 1, 'A': 2,
        'B+': 3, 'B': 4,
        'C+': 5, 'C': 6,
        'D': 7, 'F': 8
    }
    return grade_rank.get(grade, 9)

if __name__ == "__main__":
    main()

"""