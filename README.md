# Library Management System

A Python-based desktop application for managing library operations using Tkinter GUI and MySQL database.

## Project Overview

The Library Management System is a comprehensive desktop application built with Python that provides a user-friendly interface for managing library books, issuing books to students, and handling book returns. It features a graphical user interface (GUI) built with Tkinter and stores all data in a MySQL database for persistent storage.

## Features

- **Add Books**: Add new books to the library with details like Book ID, Title, Author, and Status
- **Delete Books**: Remove books from the library database
- **View Books**: Display a complete list of all books in the library
- **Issue Books**: Issue books to students with proper tracking
- **Return Books**: Process book returns and update availability status
- **Database Integration**: Persistent data storage using MySQL
- **Error Handling**: Comprehensive error handling and user feedback
- **GUI Interface**: User-friendly Tkinter-based graphical interface

## Tech Stack

- **Language**: Python 3
- **GUI Framework**: Tkinter
- **Database**: MySQL
- **Database Driver**: PyMySQL
- **Image Processing**: Pillow (PIL)

## Installation Instructions

### Prerequisites
- Python 3.7 or higher
- MySQL Server installed and running
- pip (Python package manager)

### Steps

1. Clone the repository:
```bash
git clone https://github.com/NandiNandish/library_management_sys.git
cd library_management_sys
```

2. Install required dependencies:
```bash
pip install pymysql pillow
```

3. Configure MySQL credentials in `main.py`:
```python
mypass = "your_mysql_password"
mydatabase = "your_database_name"
```

## Database Setup

1. Open MySQL and create a new database:
```sql
CREATE DATABASE db;
```

2. Run the database setup script:
```bash
python setup_db.py
```

This script will create two tables:
- **books**: Stores book information (bid, title, author, status)
- **books_issued**: Tracks issued books (bid, issueto)

## Usage

1. Start the application:
```bash
python main.py
```

2. Use the graphical interface to:
   - Click **Add Book Details** to add new books
   - Click **Delete Book** to remove books
   - Click **View Book List** to see all books
   - Click **Issue Book to Student** to issue a book
   - Click **Return Book** to process returns

## Project Structure

```
library_management_sys/
├── main.py                 # Main application entry point with GUI
├── AddBook.py             # Module for adding books
├── DeleteBook.py          # Module for deleting books
├── ViewBooks.py           # Module for viewing all books
├── IssueBook.py           # Module for issuing books to students
├── ReturnBook.py          # Module for processing book returns
├── setup_db.py            # Database initialization script
├── readiness_check.py     # System readiness verification
├── test_connections.py    # Database connection testing
├── lib.jpg                # Background image for GUI
└── README.md              # Project documentation
```

## File Descriptions

- **main.py**: Contains the main GUI window with buttons and menu options
- **AddBook.py**: Handles adding new books with validation
- **DeleteBook.py**: Manages book deletion from database
- **ViewBooks.py**: Displays all books in a formatted table/list
- **IssueBook.py**: Issues books to students and tracks them
- **ReturnBook.py**: Processes book returns and updates status
- **setup_db.py**: Creates database tables if they don't exist

## Requirements

```
PyMySQL==1.0.2
Pillow==10.0.0
```

## Configuration

Update database credentials in `main.py` (lines 12-13):
```python
mypass = "root"           # Your MySQL password
mydatabase = "db"         # Your database name
```

## Common Issues

**Issue**: Connection refused error
**Solution**: Ensure MySQL server is running on localhost:3306

**Issue**: ModuleNotFoundError for pymysql or PIL
**Solution**: Run `pip install pymysql pillow`

**Issue**: Image not loading
**Solution**: Ensure `lib.jpg` is in the same directory as `main.py`

## Future Enhancements

- User authentication and role management
- Advanced search and filtering
- Overdue tracking and notifications
- Membership management
- Report generation
- Multi-language support

## Author
Nandi Nandish

## License
This project is open source and available under the MIT License.