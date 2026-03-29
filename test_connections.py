import pymysql
import sys

print("=" * 60)
print("LIBRARY MANAGEMENT SYSTEM - CONNECTION TEST")
print("=" * 60)

try:
    # Step 1: Test main database connection
    print("\n[1] Testing main database connection...")
    con = pymysql.connect(host='localhost', user='root', password='root', database='db')
    cur = con.cursor()
    print("    ✓ Connected to database 'db'")
    
    # Step 2: Verify tables exist
    print("\n[2] Verifying database tables...")
    cur.execute("SHOW TABLES")
    tables = [t[0] for t in cur.fetchall()]
    print(f"    ✓ Found tables: {tables}")
    
    if 'books' not in tables:
        print("    ✗ ERROR: 'books' table missing!")
        sys.exit(1)
    if 'books_issued' not in tables:
        print("    ✗ ERROR: 'books_issued' table missing!")
        sys.exit(1)
    
    # Step 3: Test importing AddBook module
    print("\n[3] Testing AddBook module import...")
    import AddBook
    print(f"    ✓ AddBook imported successfully")
    print(f"      - AddBook.con = {AddBook.con}")
    print(f"      - AddBook.cur = {AddBook.cur}")
    print(f"      - AddBook.bookTable = {AddBook.bookTable}")
    
    # Step 4: Inject connection into AddBook
    print("\n[4] Injecting connection into AddBook...")
    AddBook.con = con
    AddBook.cur = cur
    print(f"    ✓ AddBook.con injected: {AddBook.con is not None}")
    print(f"    ✓ AddBook.cur injected: {AddBook.cur is not None}")
    
    # Step 5: Test importing DeleteBook module
    print("\n[5] Testing DeleteBook module import...")
    import DeleteBook
    print(f"    ✓ DeleteBook imported successfully")
    DeleteBook.con = con
    DeleteBook.cur = cur
    print(f"    ✓ Connection injected into DeleteBook")
    
    # Step 6: Test importing ViewBooks module
    print("\n[6] Testing ViewBooks module import...")
    import ViewBooks
    print(f"    ✓ ViewBooks imported successfully")
    ViewBooks.con = con
    ViewBooks.cur = cur
    print(f"    ✓ Connection injected into ViewBooks")
    
    # Step 7: Test importing IssueBook module
    print("\n[7] Testing IssueBook module import...")
    import IssueBook
    print(f"    ✓ IssueBook imported successfully")
    IssueBook.con = con
    IssueBook.cur = cur
    print(f"    ✓ Connection injected into IssueBook")
    
    # Step 8: Test importing ReturnBook module
    print("\n[8] Testing ReturnBook module import...")
    import ReturnBook
    print(f"    ✓ ReturnBook imported successfully")
    ReturnBook.con = con
    ReturnBook.cur = cur
    print(f"    ✓ Connection injected into ReturnBook")
    
    # Step 9: Verify all modules have connection
    print("\n[9] Verifying all modules have database access...")
    modules_ok = True
    
    if AddBook.con is None or AddBook.cur is None:
        print("    ✗ AddBook connection missing!")
        modules_ok = False
    else:
        print("    ✓ AddBook has connection")
    
    if DeleteBook.con is None or DeleteBook.cur is None:
        print("    ✗ DeleteBook connection missing!")
        modules_ok = False
    else:
        print("    ✓ DeleteBook has connection")
    
    if ViewBooks.con is None or ViewBooks.cur is None:
        print("    ✗ ViewBooks connection missing!")
        modules_ok = False
    else:
        print("    ✓ ViewBooks has connection")
    
    if IssueBook.con is None or IssueBook.cur is None:
        print("    ✗ IssueBook connection missing!")
        modules_ok = False
    else:
        print("    ✓ IssueBook has connection")
    
    if ReturnBook.con is None or ReturnBook.cur is None:
        print("    ✗ ReturnBook connection missing!")
        modules_ok = False
    else:
        print("    ✓ ReturnBook has connection")
    
    # Step 10: Test a simple query from each module
    print("\n[10] Testing database queries from each module...")
    
    try:
        AddBook.cur.execute("SELECT COUNT(*) FROM books")
        count = AddBook.cur.fetchone()[0]
        print(f"    ✓ AddBook can query books table (count: {count})")
    except Exception as e:
        print(f"    ✗ AddBook query failed: {str(e)}")
        modules_ok = False
    
    try:
        DeleteBook.cur.execute("SELECT COUNT(*) FROM books")
        count = DeleteBook.cur.fetchone()[0]
        print(f"    ✓ DeleteBook can query books table (count: {count})")
    except Exception as e:
        print(f"    ✗ DeleteBook query failed: {str(e)}")
        modules_ok = False
    
    try:
        ViewBooks.cur.execute("SELECT COUNT(*) FROM books")
        count = ViewBooks.cur.fetchone()[0]
        print(f"    ✓ ViewBooks can query books table (count: {count})")
    except Exception as e:
        print(f"    ✗ ViewBooks query failed: {str(e)}")
        modules_ok = False
    
    try:
        IssueBook.cur.execute("SELECT COUNT(*) FROM books_issued")
        count = IssueBook.cur.fetchone()[0]
        print(f"    ✓ IssueBook can query books_issued table (count: {count})")
    except Exception as e:
        print(f"    ✗ IssueBook query failed: {str(e)}")
        modules_ok = False
    
    try:
        ReturnBook.cur.execute("SELECT COUNT(*) FROM books_issued")
        count = ReturnBook.cur.fetchone()[0]
        print(f"    ✓ ReturnBook can query books_issued table (count: {count})")
    except Exception as e:
        print(f"    ✗ ReturnBook query failed: {str(e)}")
        modules_ok = False
    
    # Final status
    print("\n" + "=" * 60)
    if modules_ok:
        print("✓ ALL TESTS PASSED - SYSTEM READY!")
    else:
        print("✗ SOME TESTS FAILED - CHECK ERRORS ABOVE")
    print("=" * 60)
    
    con.close()
    
except Exception as e:
    print(f"\n✗ CRITICAL ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
