import sqlite3

# Create or connect to the database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    date TEXT NOT NULL,
    note TEXT
)
""")
conn.commit()

# Function to add an expense
def add_expense(amount, category, date, note=""):
    cursor.execute("INSERT INTO expenses (amount, category, date, note) VALUES (?, ?, ?, ?)",
                   (amount, category, date, note))
    conn.commit()
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    for exp in expenses:
        print(exp)

# Function to filter expenses by category
def filter_expenses_by_category(category):
    cursor.execute("SELECT * FROM expenses WHERE category=?", (category,))
    expenses = cursor.fetchall()
    for exp in expenses:
        print(exp)

# Function to generate a monthly report
def generate_monthly_report(month):
    cursor.execute("SELECT * FROM expenses WHERE date LIKE ?", (f"{month}%",))
    expenses = cursor.fetchall()
    total_spent = sum(exp[1] for exp in expenses)
    print(f"Total expenses in {month}: {total_spent}")
    for exp in expenses:
        print(exp)

# Close the connection
conn.close()
