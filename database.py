import sqlite3

def get_connection():
    return sqlite3.connect("resumes.db")

def insert_candidate(parsed_data):
    conn = get_connection()
    cur = conn.cursor()

    # Create the table if it doesn't exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            education TEXT,
            organizations TEXT
        )
    """)

    cur.execute("""
        INSERT INTO candidates (name, education, organizations)
        VALUES (?, ?, ?)
    """, (
        parsed_data["name"],
        ", ".join(parsed_data["education"]),
        ", ".join(parsed_data["organizations"])
    ))

    conn.commit()
    conn.close()
