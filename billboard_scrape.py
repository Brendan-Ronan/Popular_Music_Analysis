import billboard
import sqlite3
from billboard import ChartData

# Create SQLite database and table
conn = sqlite3.connect('top_songs_database.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS top_songs (
        Year INTEGER,
        Rank INTEGER,
        Song TEXT,
        Artist TEXT)   
''')


# Retrieve Data
for year in range(2006, 2024):
    chart = billboard.ChartData('hot-100-songs', year=year)
    print(f"Data for {year} fetched.")

    # Insert data into the database
    for rank, song in enumerate(chart, start=1):
        cursor.execute('''
            INSERT INTO top_songs (Year, Rank, Song, Artist)
            VALUES (?, ?, ?, ?)
        ''', (year, rank, song.title, song.artist))

conn.commit()
conn.close()

print("Data collection complete.")
