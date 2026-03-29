import os
import sys

print("=" * 70)
print("LIBRARY MANAGEMENT SYSTEM - READINESS CHECK")
print("=" * 70)

all_checks_passed = True

# ============================================================================
# 1. CHECK REQUIRED FILES
# ============================================================================
print("\n[1] CHECKING REQUIRED FILES...")
required_files = [
    'main.py',
    'AddBook.py',
    'DeleteBook.py',
    'IssueBook.py',
    'ReturnBook.py',
    'ViewBooks.py',
    'lib.jpg'
]

for file in required_files:
    if os.path.exists(file):
        print(f"    ✓ {file}")
    else:
        print(f"    ✗ {file} - MISSING!")
        all_checks_passed = False

# ============================================================================
# 2. CHECK PYTHON DEPENDENCIES
# ============================================================================
print("\n[2] CHECKING PYTHON DEPENDENCIES...")
required_modules = {
    'tkinter': 'Tkinter (GUI)',
    'PIL': 'Pillow (Image)',
    'pymysql': 'PyMySQL (Database)'
}

for module, name in required_modules.items():
    try:
        __import__(module)
        print(f"    ✓ {name}")
    except ImportError:
        print(f"    ✗ {name} - NOT INSTALLED!")
        all_checks_passed = False

# ============================================================================
# 3. CHECK DATABASE CONNECTION
# ============================================================================
print("\n[3] CHECKING DATABASE CONNECTION...")
try:
    import pymysql
    con = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='db'
    )
    cur = con.cursor()
    print(f"    ✓ Connected to database 'db'")
    
    # Check tables
    cur.execute("SHOW TABLES")
    tables = [t[0] for t in cur.fetchall()]
    
    if 'books' in tables and 'books_issued' in tables:
        print(f"    ✓ Required tables exist: {tables}")
    else:
        print(f"    ✗ Missing tables! Found: {tables}")
        all_checks_passed = False
    
    # Check table structures
    cur.execute("DESCRIBE books")
    books_cols = [col[0] for col in cur.fetchall()]
    if books_cols == ['bid', 'title', 'author', 'status']:
        print(f"    ✓ 'books' table structure correct")
    else:
        print(f"    ✗ 'books' table structure incorrect: {books_cols}")
        all_checks_passed = False
    
    cur.execute("DESCRIBE books_issued")
    issued_cols = [col[0] for col in cur.fetchall()]
    if issued_cols == ['bid', 'issueto']:
        print(f"    ✓ 'books_issued' table structure correct")
    else:
        print(f"    ✗ 'books_issued' table structure incorrect: {issued_cols}")
        all_checks_passed = False
    
    con.close()
    
except Exception as e:
    print(f"    ✗ Database error: {str(e)}")
    all_checks_passed = False

# ============================================================================
# 4. CHECK MODULE IMPORTS
# ============================================================================
print("\n[4] CHECKING MODULE IMPORTS...")
try:
    import AddBook
    print(f"    ✓ AddBook imported")
except Exception as e:
    print(f"    ✗ AddBook import failed: {str(e)}")
    all_checks_passed = False

try:
    import DeleteBook
    print(f"    ✓ DeleteBook imported")
except Exception as e:
    print(f"    ✗ DeleteBook import failed: {str(e)}")
    all_checks_passed = False

try:
    import ViewBooks
    print(f"    ✓ ViewBooks imported")
except Exception as e:
    print(f"    ✗ ViewBooks import failed: {str(e)}")
    all_checks_passed = False

try:
    import IssueBook
    print(f"    ✓ IssueBook imported")
except Exception as e:
    print(f"    ✗ IssueBook import failed: {str(e)}")
    all_checks_passed = False

try:
    import ReturnBook
    print(f"    ✓ ReturnBook imported")
except Exception as e:
    print(f"    ✗ ReturnBook import failed: {str(e)}")
    all_checks_passed = False

# ============================================================================
# 5. CHECK GLOBAL VARIABLES IN MODULES
# ============================================================================
print("\n[5] CHECKING MODULE GLOBALS...")
try:
    import AddBook, DeleteBook, ViewBooks, IssueBook, ReturnBook
    
    modules_to_check = {
        'AddBook': AddBook,
        'DeleteBook': DeleteBook,
        'ViewBooks': ViewBooks,
        'IssueBook': IssueBook,
        'ReturnBook': ReturnBook
    }
    
    for module_name, module in modules_to_check.items():
        if hasattr(module, 'bookTable'):
            print(f"    ✓ {module_name} has 'bookTable' variable")
        else:
            print(f"    ✗ {module_name} missing 'bookTable' variable!")
            all_checks_passed = False
except Exception as e:
    print(f"    ✗ Module check failed: {str(e)}")
    all_checks_passed = False

# ============================================================================
# 6. CHECK DATABASE QUERY FUNCTIONALITY
# ============================================================================
print("\n[6] CHECKING DATABASE QUERY CAPABILITY...")
try:
    import pymysql
    con = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='db'
    )
    cur = con.cursor()
    
    # Test INSERT (without committing)
    try:
        test_query = "INSERT INTO books VALUES (%s, %s, %s, %s)"
        cur.execute(test_query, ('TEST001', 'Test Book', 'Test Author', 'available'))
        con.rollback()  # Don't commit test data
        print(f"    ✓ INSERT query works (test rolled back)")
    except Exception as e:
        print(f"    ✗ INSERT query failed: {str(e)}")
        all_checks_passed = False
    
    # Test SELECT
    try:
        cur.execute("SELECT COUNT(*) FROM books")
        count = cur.fetchone()[0]
        print(f"    ✓ SELECT query works (currently {count} books)")
    except Exception as e:
        print(f"    ✗ SELECT query failed: {str(e)}")
        all_checks_passed = False
    
    # Test UPDATE (without committing)
    try:
        test_query = "UPDATE books SET status = %s WHERE bid = %s"
        cur.execute(test_query, ('issued', 'NONEXISTENT'))
        con.rollback()  # Don't commit
        print(f"    ✓ UPDATE query works")
    except Exception as e:
        print(f"    ✗ UPDATE query failed: {str(e)}")
        all_checks_passed = False
    
    # Test DELETE (without committing)
    try:
        test_query = "DELETE FROM books WHERE bid = %s"
        cur.execute(test_query, ('NONEXISTENT',))
        con.rollback()  # Don't commit
        print(f"    ✓ DELETE query works")
    except Exception as e:
        print(f"    ✗ DELETE query failed: {str(e)}")
        all_checks_passed = False
    
    con.close()
    
except Exception as e:
    print(f"    ✗ Query test failed: {str(e)}")
    all_checks_passed = False

# ============================================================================
# 7. CHECK CODE QUALITY
# ============================================================================
print("\n[7] CHECKING CODE QUALITY...")
try:
    import py_compile
    
    files_to_check = [
        'main.py',
        'AddBook.py',
        'DeleteBook.py',
        'IssueBook.py',
        'ReturnBook.py',
        'ViewBooks.py'
    ]
    
    for file in files_to_check:
        try:
            py_compile.compile(file, doraise=True)
            print(f"    ✓ {file} - No syntax errors")
        except py_compile.PyCompileError as e:
            print(f"    ✗ {file} - Syntax error: {str(e)}")
            all_checks_passed = False
            
except Exception as e:
    print(f"    ✗ Code quality check failed: {str(e)}")
    all_checks_passed = False

# ============================================================================
# 8. CHECK CONFIGURATION
# ============================================================================
print("\n[8] CHECKING CONFIGURATION...")
try:
    # Check database credentials
    with open('main.py', 'r') as f:
        content = f.read()
        if 'mypass = "root"' in content and 'mydatabase="db"' in content:
            print(f"    ✓ Database credentials configured")
        else:
            print(f"    ✗ Database credentials not found in main.py")
            all_checks_passed = False
    
    # Check table names
    with open('AddBook.py', 'r') as f:
        content = f.read()
        if 'bookTable = "books"' in content:
            print(f"    ✓ AddBook table name configured")
        else:
            print(f"    ✗ AddBook table name not configured")
            all_checks_passed = False
    
except Exception as e:
    print(f"    ✗ Configuration check failed: {str(e)}")
    all_checks_passed = False

# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("\n" + "=" * 70)
if all_checks_passed:
    print("✓✓✓ PROJECT IS READY TO RUN ✓✓✓")
    print("\nYou can now start the application by running:")
    print("  python main.py")
    print("\nOR via the command line:")
    print("  cd \"e:\\language\\PY\\library management system\"")
    print("  python main.py")
else:
    print("✗✗✗ PROJECT HAS ISSUES - FIX ERRORS ABOVE ✗✗✗")
    sys.exit(1)
print("=" * 70)
