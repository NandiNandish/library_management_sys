import pymysql

try:
    con = pymysql.connect(host='localhost', user='root', password='root', database='db')
    cur = con.cursor()
    
    # Create books table
    create_books = """
    CREATE TABLE IF NOT EXISTS books (
        bid VARCHAR(50) PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        author VARCHAR(100) NOT NULL,
        status VARCHAR(20) NOT NULL
    )
    """
    
    # Create books_issued table
    create_issued = """
    CREATE TABLE IF NOT EXISTS books_issued (
        bid VARCHAR(50) PRIMARY KEY,
        issueto VARCHAR(100) NOT NULL,
        FOREIGN KEY (bid) REFERENCES books(bid)
    )
    """
    
    cur.execute(create_books)
    con.commit()
    print("✓ Created 'books' table")
    
    cur.execute(create_issued)
    con.commit()
    print("✓ Created 'books_issued' table")
    
    # Verify tables
    cur.execute("SHOW TABLES")
    tables = [t[0] for t in cur.fetchall()]
    print(f"\n✓ Database tables created: {tables}")
    
    # Show table structures
    print("\n--- Books Table Structure ---")
    cur.execute("DESCRIBE books")
    for col in cur.fetchall():
        print(f"  {col[0]}: {col[1]}")
    
    print("\n--- Books_Issued Table Structure ---")
    cur.execute("DESCRIBE books_issued")
    for col in cur.fetchall():
        print(f"  {col[0]}: {col[1]}")
    
    con.close()
    print("\n✓ Database setup complete! Ready to use.")
    
except Exception as e:
    print(f"✗ Error: {str(e)}")
