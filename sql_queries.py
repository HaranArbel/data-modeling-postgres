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
    songplay_id SERIAL PRIMARY KEY, 
    start_time TIMESTAMP,
    user_id INT,
    level VARCHAR(255),
    song_id VARCHAR(255),
    artist_id VARCHAR(255),
    session_id INT,
    location VARCHAR(255),
    user_agent VARCHAR(255)
    );
"""

user_table_create = """
    CREATE TABLE users 
    (
    user_id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    gender VARCHAR(50),
    level VARCHAR(255)
    );
"""

song_table_create = """
    CREATE TABLE songs 
    (
    song_id VARCHAR(255) PRIMARY KEY,
    title VARCHAR(255),
    artist_id VARCHAR(255),
    year INT,
    duration DECIMAL
    );
"""

artist_table_create = """
    CREATE TABLE artists 
    (
    artist_id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255) , 
    location VARCHAR(255), 
    latitude DECIMAL , 
    longitude DECIMAL 
    );
"""

time_table_create = """
    CREATE TABLE times 
    (
    start_time TIMESTAMP PRIMARY KEY, 
    hour INT, 
    day VARCHAR(50),
    week INT,
    month INT,
    year INT, 
    WEEKDAY INT
    );
"""

# INSERT RECORDS

songplay_table_insert = """
    INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (songplay_id) DO NOTHING
"""

user_table_insert = """
    INSERT INTO users (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level
"""

song_table_insert = """
    INSERT INTO songs (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING
"""

artist_table_insert = """
    INSERT INTO artists (artist_id, name, location, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING
"""

time_table_insert = """
    INSERT INTO times (start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING
"""

# FIND SONGS

song_select = """
    SELECT song_id, artists.artist_id 
    FROM songs 
    JOIN artists 
    ON songs.artist_id = artists.artist_id
    WHERE 
        songs.title = %s AND 
        artists.name = %s AND 
        songs.duration = %s
"""

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]