import pytest
from student_manager import StudentManager
from datetime import datetime, timedelta

def test_add_assignment():
    sm = StudentManager()
    deadline = datetime.now() + timedelta(days=5)
    
    assignment = sm.add_assignment("Math HW", deadline, "Math")

    assert assignment in sm.assignments
    assert assignment['title'] == "Math HW"
    assert assignment['completed'] is False

def test_mark_completed():
    sm = StudentManager()
    deadline = datetime.now() + timedelta(days=5)
    
    sm.add_assignment("Physics HW", deadline)
    result = sm.mark_completed("Physics HW")

    assert result is True
    assert sm.assignments[0]['completed'] is True


def test_calculate_gpa():
    sm = StudentManager()

    sm.add_grade("Math", 90)
    sm.add_grade("English", 80)

    assert sm.calculate_gpa() == 85  # average

def test_invalid_grade():
    sm = StudentManager()
    
    with pytest.raises(ValueError):
        sm.add_grade("Math", 120)  # invalid


def test_statistics():
    sm = StudentManager()
    deadline = datetime.now() + timedelta(days=5)

    sm.add_assignment("Chem", deadline)
    sm.add_assignment("Bio", deadline)
    sm.mark_completed("Chem")
    sm.add_grade("Chem", 90)

    stats = sm.get_statistics()

    assert stats['total_assignments'] == 2
    assert stats['completed'] == 1
    assert stats['pending'] == 1
    assert stats['gpa'] == 90


def test_upcoming_deadlines():
    sm = StudentManager()
    deadline = datetime.now() + timedelta(days=3)

    sm.add_assignment("Task1", deadline)

    upcoming = sm.get_upcoming_deadlines(days=7)

    assert len(upcoming) == 1
    assert upcoming[0]['title'] == "Task1"
