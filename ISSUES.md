# Open Issues - StudentHub

Welcome contributors! Below are issues organized by difficulty level. Pick one that matches your skill level and get started!

---

## 🟢 Good First Issues (Beginner-Friendly)

### Issue #1: Add Error Handling for Invalid Date Formats
**Label:** `good-first-issue`, `bug`
**Difficulty:** Easy
**File:** `utils.py:9`

**Description:**
The `format_date()` function in utils.py doesn't handle invalid date formats. If a user enters a date like "2024-13-45", the program crashes.

**Task:**
- Add try-except block to handle `ValueError`
- Return a helpful error message to the user
- Test with various invalid date formats

**Expected Outcome:**
```python
# Should handle invalid dates gracefully
format_date("invalid-date")  # Should return error, not crash
```

**Skills You'll Learn:** Error handling, defensive programming

---

### Issue #2: Fix Typo in README
**Label:** `good-first-issue`, `documentation`
**Difficulty:** Very Easy
**File:** `README.md`

**Description:**
There's a placeholder `<your-repo-url>` in the README that should be replaced with actual repository instructions.

**Task:**
- Update the clone command in README.md
- Make it more generic or add proper instructions
- Check for any other placeholders

**Skills You'll Learn:** Documentation, attention to detail

---

### Issue #3: Add Input Validation for Grade Range
**Label:** `good-first-issue`, `enhancement`
**Difficulty:** Easy
**File:** `student_manager.py:38`

**Description:**
The `add_grade()` method calls `validate_grade()` but we should also add validation for negative numbers and non-numeric inputs.

**Task:**
- Enhance the validation in `add_grade()` method
- Add type checking for the grade parameter
- Raise appropriate exceptions with clear messages

**Expected Behavior:**
```python
manager.add_grade("Math", -5)    # Should raise ValueError
manager.add_grade("Math", "A+")  # Should raise TypeError
```

**Skills You'll Learn:** Input validation, type checking

---

### Issue #4: Add Docstring to get_priority_level Function
**Label:** `good-first-issue`, `documentation`
**Difficulty:** Very Easy
**File:** `utils.py:44`

**Description:**
The `get_priority_level()` function is missing a docstring. Good documentation is important!

**Task:**
- Add a proper docstring following Python conventions
- Describe parameters and return value
- Include an example if possible

**Skills You'll Learn:** Code documentation, Python docstrings

---

## 🟡 Intermediate Issues

### Issue #5: Implement Delete Assignment Feature
**Label:** `enhancement`, `help-wanted`
**Difficulty:** Medium
**Files:** `student_manager.py`, `main.py`

**Description:**
Users can add and complete assignments, but there's no way to delete them.

**Task:**
- Add `delete_assignment()` method in StudentManager class
- Add CLI command in main.py to call this method
- Handle case when assignment doesn't exist
- Update README with new command usage

**Expected Usage:**
```bash
python main.py delete "Math Homework"
```

**Skills You'll Learn:** Feature implementation, CLI development

---

### Issue #6: Add Unit Tests for StudentManager Class
**Label:** `testing`, `good-second-issue`
**Difficulty:** Medium
**File:** Create `tests/test_student_manager.py`

**Description:**
The project has no tests! We need unit tests for the StudentManager class.

**Task:**
- Create a test file in the tests directory
- Write tests for at least 5 methods in StudentManager
- Use Python's unittest or pytest framework
- Ensure all tests pass

**Test Examples:**
- Test adding an assignment
- Test marking assignment as completed
- Test GPA calculation
- Test invalid grade handling

**Skills You'll Learn:** Unit testing, test-driven development

---

### Issue #7: Add Color-Coded Priority Display
**Label:** `enhancement`
**Difficulty:** Medium
**File:** `main.py`

**Description:**
When listing assignments, show priorities in different colors (red for HIGH, yellow for MEDIUM, green for LOW).

**Task:**
- Install and use the `colorama` library
- Color-code the output based on priority level
- Update requirements.txt with new dependency
- Ensure it works cross-platform (Windows/Linux/Mac)

**Skills You'll Learn:** External libraries, terminal formatting

---

## 🔴 Advanced Issues

### Issue #8: Implement Data Persistence
**Label:** `enhancement`, `advanced`
**Difficulty:** Hard
**Files:** `student_manager.py`, `main.py`

**Description:**
Currently, all data is lost when the program exits. Implement data persistence using JSON files.

**Task:**
- Save assignments and grades to `data.json` when program exits
- Load data when program starts
- Handle file corruption gracefully
- Add backup mechanism
- Update the StudentManager class to handle serialization

**Skills You'll Learn:** File I/O, data persistence, JSON handling

---

### Issue #9: Add Pomodoro Timer Feature
**Label:** `enhancement`, `feature`
**Difficulty:** Hard
**File:** Create new `pomodoro.py`

**Description:**
Add a Pomodoro timer to help students focus on studying.

**Task:**
- Create a new PomodoroTimer class
- Implement 25-minute work sessions and 5-minute breaks
- Add CLI command to start timer
- Show countdown in terminal
- Play sound or notification when session ends (optional)

**Expected Usage:**
```bash
python main.py pomodoro --sessions 4
```

**Skills You'll Learn:** Time management, threading, CLI tools

---

### Issue #10: Create Export to CSV Feature
**Label:** `enhancement`, `feature`
**Difficulty:** Medium-Hard
**Files:** `student_manager.py`, `main.py`, create new `export.py`

**Description:**
Allow users to export their assignments and grades to CSV format for use in spreadsheets.

**Task:**
- Add export functionality using Python's csv module
- Create separate exports for assignments and grades
- Add CLI command for export
- Allow user to specify output filename

**Expected Usage:**
```bash
python main.py export assignments --output my_assignments.csv
python main.py export grades --output my_grades.csv
```

**Skills You'll Learn:** CSV handling, data formatting

---

## 📋 How to Claim an Issue

1. Choose an issue that matches your skill level
2. Comment on this file or create a GitHub issue: "I would like to work on Issue #X"
3. Wait for assignment confirmation
4. Fork the repo and start working
5. Follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md)
6. Submit your Pull Request

## 🏆 Bonus Challenges

After completing 2-3 issues, try creating your own feature! Some ideas:
- Weekly study schedule planner
- Integration with Google Calendar
- Reminder notifications
- Study group management
- Grade prediction based on current performance

---

**Questions?** Check CONTRIBUTING.md or ask in the comments!

Good luck and happy coding! 🚀
