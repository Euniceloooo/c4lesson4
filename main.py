import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('constituent_estates.db')

# Create a cursor object
cursor = conn.cursor()

# Create the table
create_table_query = '''
CREATE TABLE IF NOT EXISTS constituent_estates (
    c_estate TEXT,
    e_estate TEXT,
    pe_addr TEXT,
    scp_mktc TEXT,
    min_update INTEGER,
    max_update INTEGER,
    blgcount INTEGER,
    pc_dev TEXT,
    facilities_c TEXT,
    facilities_e TEXT,
    url TEXT
);
'''

# Execute the create table query
cursor.execute(create_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database initialized and table created successfully.")