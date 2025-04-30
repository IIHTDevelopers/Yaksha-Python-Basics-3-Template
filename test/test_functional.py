# test/test_car_inventory.py

import unittest
import os
import sys
import json

# Adjusting the path to import TestUtils and the car inventory module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test.TestUtils import TestUtils
from carinventory import  search_by_budget, save_inventory, car_inventory

class TestCarInventory(unittest.TestCase):
    def setUp(self):
        # Initialize TestUtils object for yaksha assertions
        self.test_obj = TestUtils()

        # Sample Data
        self.max_budget = 25000
        self.expected_filtered_cars = [
            {"id": 1, "make": "Toyota", "model": "Camry", "year": 2021, "price": 25000},
            {"id": 2, "make": "Honda", "model": "Civic", "year": 2020, "price": 22000},
            {"id": 4, "make": "Chevrolet", "model": "Malibu", "year": 2019, "price": 20000}
        ]
        self.filename = "test_car_inventory.json"


    def test_search_by_budget(self):
        try:
            result = search_by_budget(car_inventory, self.max_budget)
            if result == self.expected_filtered_cars:
                self.test_obj.yakshaAssert("TestSearchByBudget", True, "functional")
                print("TestSearchByBudget = Passed")
            else:
                self.test_obj.yakshaAssert("TestSearchByBudget", False, "functional")
                print("TestSearchByBudget = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestSearchByBudget", False, "functional")
            print(f"TestSearchByBudget = Failed ")

    def test_save_inventory(self):
        try:
            filename = save_inventory(car_inventory, self.filename)
            if os.path.exists(filename):
                with open(filename, "r") as file:
                    data = json.load(file)
                result = data == car_inventory
                if result:
                    self.test_obj.yakshaAssert("TestSaveInventory", True, "functional")
                    print("TestSaveInventory = Passed")
                else:
                    self.test_obj.yakshaAssert("TestSaveInventory", False, "functional")
                    print("TestSaveInventory = Failed")
            else:
                self.test_obj.yakshaAssert("TestSaveInventory", False, "functional")
                print("TestSaveInventory = Failed | File not found")
            os.remove(filename)
        except Exception as e:
            self.test_obj.yakshaAssert("TestSaveInventory", False, "functional")
            print(f"TestSaveInventory = Failed ")

if __name__ == '__main__':
    unittest.main()


# test/test_student_management.py

import unittest
import sys
import os

# Adjusting the path to import TestUtils and the student management module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test.TestUtils import TestUtils
from StudentCourseManagement import student_names, student_courses, unique_subjects


class TestStudentManagement(unittest.TestCase):
    def setUp(self):
        # Initialize TestUtils object for yaksha assertions
        self.test_obj = TestUtils()

    def test_student_names(self):
        try:
            result = student_names()
            expected_result = ["John", "Emma", "Sophia", "Michael", "Daniel", "Olivia"]

            if result == expected_result:
                self.test_obj.yakshaAssert("TestStudentNames", True, "functional")
                print("TestStudentNames = Passed")
            else:
                self.test_obj.yakshaAssert("TestStudentNames", False, "functional")
                print("TestStudentNames = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestStudentNames", False, "functional")
            print(f"TestStudentNames = Failed ")

    def test_student_courses(self):
        try:
            result = student_courses()
            expected_result = {
                "John": ("Math", "Physics"),
                "Emma": ("Biology", "Chemistry"),
                "Sophia": ("History", "English"),
                "Michael": ("Math", "Computer Science"),
                "Daniel": ("Physics", "Chemistry"),
                "Olivia": ("Biology", "History")
            }

            if result == expected_result:
                self.test_obj.yakshaAssert("TestStudentCourses", True, "functional")
                print("TestStudentCourses = Passed")
            else:
                self.test_obj.yakshaAssert("TestStudentCourses", False, "functional")
                print("TestStudentCourses = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestStudentCourses", False, "functional")
            print(f"TestStudentCourses = Failed ")

    def test_unique_subjects(self):
        try:
            result = unique_subjects()
            expected_result = {"Math", "Physics", "Biology", "Chemistry", "English", "History", "Computer Science", "Economics"}

            if result == expected_result:
                self.test_obj.yakshaAssert("TestUniqueSubjects", True, "functional")
                print("TestUniqueSubjects = Passed")
            else:
                self.test_obj.yakshaAssert("TestUniqueSubjects", False, "functional")
                print("TestUniqueSubjects = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestUniqueSubjects", False, "functional")
            print(f"TestUniqueSubjects = Failed ")


# test/test_student_marks_analysis.py

import unittest
import numpy as np
import sys
import os

# Adjusting the path to import TestUtils and the student marks module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test.TestUtils import TestUtils
from StudentMarksAnalysis import (
    analyze_marks,
    classify_grades
)


class TestStudentMarksAnalysis(unittest.TestCase):
    def setUp(self):
        # Initialize TestUtils object for yaksha assertions
        self.test_obj = TestUtils()

        # Sample data for student marks
        self.student_marks = np.array([78, 85, 92, 88, 76])
        self.expected_avg_marks = 83.80
        self.expected_max_marks = 92
        self.expected_min_marks = 76
        self.expected_grades = ['C', 'B', 'A', 'B', 'C']

    def test_analyze_marks(self):
        try:
            # Analyze student marks
            avg_marks, max_marks, min_marks = analyze_marks(self.student_marks)

            # Verify the calculated statistics
            result = (
                    round(avg_marks, 2) == self.expected_avg_marks and
                    max_marks == self.expected_max_marks and
                    min_marks == self.expected_min_marks
            )

            if result:
                self.test_obj.yakshaAssert("TestAnalyzeMarks", True, "functional")
                print("TestAnalyzeMarks = Passed")
            else:
                self.test_obj.yakshaAssert("TestAnalyzeMarks", False, "functional")
                print("TestAnalyzeMarks = Failed")
                print("Expected Average Marks:", self.expected_avg_marks)
                print("Actual Average Marks:", avg_marks)
                print("Expected Highest Marks:", self.expected_max_marks)
                print("Actual Highest Marks:", max_marks)
                print("Expected Lowest Marks:", self.expected_min_marks)
                print("Actual Lowest Marks:", min_marks)
        except Exception as e:
            self.test_obj.yakshaAssert("TestAnalyzeMarks", False, "functional")
            print(f"TestAnalyzeMarks = Failed ")

    def test_classify_grades(self):
        try:
            # Classify student grades
            result = classify_grades(self.student_marks)

            # Verify the classified grades
            if result == self.expected_grades:
                self.test_obj.yakshaAssert("TestClassifyGrades", True, "functional")
                print("TestClassifyGrades = Passed")
            else:
                self.test_obj.yakshaAssert("TestClassifyGrades", False, "functional")
                print("TestClassifyGrades = Failed")
                
        except Exception as e:
            self.test_obj.yakshaAssert("TestClassifyGrades", False, "functional")
            print(f"TestClassifyGrades = Failed ")


if __name__ == '__main__':
    unittest.main()
