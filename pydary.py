# Import sqlite3 module
import sqlite3
import webbrowser
# Import datetime module
import datetime

# Define a class named Diary that represents a diary application
class Diary:
    # Define a constructor method that takes no arguments
    def __init__(self):
        # Connect to a database file named diary.db or create one if it does not exist
        self.conn = sqlite3.connect("diary.db")

        # Create a cursor object to execute SQL commands
        self.cur = self.conn.cursor()

        # Create a table named entries with four columns: id, title, text, and date
        self.cur.execute("CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY, title TEXT, text TEXT, date TEXT)")

    # Define a method that adds a new diary entry with a given title and text
    def add_entry(self, title, text):
        # Get the current date and time as a string
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Insert a new diary entry into the table with the given title, text, and date
        self.cur.execute("INSERT INTO entries (title, text, date) VALUES (?, ?, ?)", (title, text, date))

        # Commit the changes to the database
        self.conn.commit()

        # Print a confirmation message
        print(f"Added a new diary entry with title '{title}' and text '{text}' on {date}.")

    # Define a method that lists all the diary entries
    def list_entries(self):
        # Query all the diary entries from the table
        self.cur.execute("SELECT * FROM entries")

        # Fetch all the rows from the query result
        rows = self.cur.fetchall()

        # Print a header message
        print("Here are all your diary entries:")

        # Loop through each row and print its id, title, text, and date
        for row in rows:
            print(f"ID: {row[0]}")
            print(f"Title: {row[1]}")
            print(f"Text: {row[2]}")
            print(f"Date: {row[3]}")
            print("-" * 20)

    # Define a method that lists today's diary entries
    def list_today_entries(self):
        # Get today's date as a string
        today = datetime.date.today().strftime("%Y-%m-%d")

        # Query all the diary entries from the table that have today's date
        self.cur.execute("SELECT * FROM entries WHERE date LIKE ?", (today + "%",))

        # Fetch all the rows from the query result
        rows = self.cur.fetchall()

        # Print a header message
        print(f"Here are your diary entries for {today}:")

        # Loop through each row and print its id, title, text, and date
        for row in rows:
            print(f"ID: {row[0]}")
            print(f"Title: {row[1]}")
            print(f"Text: {row[2]}")
            print(f"Date: {row[3]}")
            print("-" * 20)
    def create_html(self):
    # Query all the diary entries from the table
        self.cur.execute("SELECT * FROM entries")

    # Fetch all the rows from the query result
        rows = self.cur.fetchall()

    # Create an html file named diary.html in write mode
        with open("diary.html", "w") as f:
            # Write some html tags and styles to the file
            f.write("<html><head><style>@import url('https://fonts.googleapis.com/css?family=Roboto+Slab');body{font-family: 'Roboto Slab', serif;}h1{color: blue;}p{color: green;}div{border: 1px solid black; padding: 10px; margin: 10px;}</style></head><body>")

        # Write a header to the file
            f.write("<h1>My Diary</h1>")

        # Loop through each row and write its title, text, and date in a div element
            for row in rows:
                f.write(f"<div><h2>{row[1]}</h2><p>{row[2]}</p><p>{row[3]}</p></div>")

        # Write some closing html tags to the file
            f.write("</body></html>")

    # Open the html file in a browser
            webbrowser.open("diary.html")

