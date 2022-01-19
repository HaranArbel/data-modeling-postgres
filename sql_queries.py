# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS times;"

# CREATE TABLES

songplay_table_create = """
    CREATE TABLE songplays
    (
    songplay_id INT, 
    start_time TIMESTAMP,
    user_id INT,
    level INT,
    song_id INT,
    artist_id INT,
    session_id INT,
    location VARCHAR(255),
    user_agent INT
    );
"""

user_table_create = """
    CREATE TABLE users 
    (
    user_id INT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    gender VARCHAR(50),
    level INT
    );
"""

song_table_create = """
    CREATE TABLE songs 
    (
    song_id INT,
    title VARCHAR(255),
    artist_id INT,
    year INT,
    duration INT
    );
"""

artist_table_create = """
    CREATE TABLE artists 
    (
    artist_id INT,
    name VARCHAR(255), 
    location VARCHAR(255), 
    latitude INT, 
    longtitude INT
    );
"""

time_table_create = """
    CREATE TABLE times 
    (
    start_time TIMESTAMP, 
    hour INT, 
    day VARCHAR(50),
    week INT,
    month INT,
    year INT, 
    WEEKDAY BOOLEAN
    );
"""

# INSERT RECORDS

songplay_table_insert = """
    INSERT INTO sonplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

user_table_insert = """
    INSERT INTO users (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
"""

song_table_insert = """
    INSERT INTO songs (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
"""

artist_table_insert = """
    INSERT INTO artists (artist_id, name, location, latitude, longtiutde)
    VALUES (%s, %s, %s, %s, %s)
"""

time_table_insert = """
    INSERT INTO times (start_time, hour, day, week, months, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]