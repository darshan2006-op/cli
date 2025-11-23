# StudentHub - Learning Management CLI Tool

A simple command-line tool to help students manage their assignments, track deadlines, and organize study sessions.

## Features

- Add and track assignments
- Set deadlines and get reminders
- Calculate grade averages
- Organize study sessions with Pomodoro timer
- Export data to JSON

## Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd demo

# Install dependencies (if any)
pip install -r requirements.txt
```

## Usage

```bash
python main.py --help
python main.py add-assignment "Math Homework" --deadline "2024-12-01"
python main.py list-assignments
python main.py calculate-gpa
```

## Project Structure

```
demo/
├── main.py              # Entry point
├── utils.py             # Utility functions
├── student_manager.py   # Core functionality
├── tests/               # Test files
├── README.md            # This file
├── CONTRIBUTING.md      # Contribution guidelines
└── ISSUES.md           # List of open issues for contributors
```

## Contributing

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

Check out [ISSUES.md](ISSUES.md) for a list of beginner-friendly issues to get started!

## License

MIT License
