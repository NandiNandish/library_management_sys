# Library Management System

## Project Overview
This is a library management system project aimed at providing a seamless experience for managing library operations
including the management of books, members, and transactions. It simplifies the process of issuing, returning, and maintaining records of library resources.

## Features
- User authentication (admin and member roles)
- Search functionality for books
- Issuing and returning books
- Overdue notifications
- Member management (add, remove, update)

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/NandiNandish/library_management_sys.git
   cd library_management_sys
   ```
2. Install the dependencies:
   ```bash
   npm install
   ```

## Usage
- Start the application:
  ```bash
  npm start
  ```
- Access the application at `http://localhost:3000`

## Database Setup
1. Ensure you have a running instance of the database (e.g., MySQL, PostgreSQL).
2. Create a new database for the library management system.
3. Run the following SQL script to set up the database schema:
   ```sql
   -- SQL script to create tables
   CREATE TABLE books (...);
   CREATE TABLE members (...);
   CREATE TABLE transactions (...);
   ```

## File Structure
```
├── src/
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── views/
│   └── app.js
├── tests/
├── package.json
└── README.md
```

## Requirements
- Node.js (v14 or later)
- npm (v6 or later)
- MySQL or PostgreSQL
- Git (for version control)
