## Data Modeling with Postgres

This project is used to create a Postgres database optimized for analysing data on songs and user activity. 
this was done by first creating a star schema of the data, and then creating an ETL pipeline to that transfers files in two local directories into the database tables. 

## Project Files
 
1. sql_queries.py - contains all the SQL queries used to define teh database schema, create the tables and insert records into the tables.
2. create_tables.py - creates and connects to the database, creates the fact and dimension tables.
3. etl.py - an implementation of the ETL pipeline that transfers the data from the files into the database.

## Data Files

There are two datasets for this projects:

1. song_data - each file in this dataset is in JSON format and contains metadata about a song and the artist of the song.
2. log_data - each file this dataset is in JSON format and simulates activity logs from a music streaming app.

## Database Tables

there are five database tables:

1. A songplay table
2. A user
3. A song table
4. An artist table
5. A time table

![star schema](/star_schema.jpg)


## Usage

1. Run `create_tables.py` to reset your database tables before each time you run the ETL script. 
2. Run `etl.py` to read and process files from `song_data` and `log_data` and load them into the tables. 
