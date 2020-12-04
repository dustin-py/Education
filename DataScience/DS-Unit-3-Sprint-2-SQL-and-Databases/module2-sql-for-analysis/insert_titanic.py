import psycopg2
import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
print(DB_NAME,DB_USER,DB_PASSWORD,DB_HOST)
conn = psycopg2.connect(
	"""
	dbname={}
	user={}
	password={}
	host={}
	""".format(DB_NAME,DB_USER,DB_PASSWORD,DB_HOST))
cur = conn.cursor()
cur.execute(
	"""
	CREATE TABLE IF NOT EXISTS titanic(
	survived integer,
	p_class integer,
	name text,
	sex text,
	age decimal,
	sib_spouse_aboard integer,
	parent_child_aboard integer,
	fare decimal);
	""")

with open('titanic.csv', 'r') as f:
	next(f) # skip header row because we already made the columns
	cur.copy_from(f, 'titanic', sep=',')

conn.commit()
cur.execute('SELECT * from titanic;')
cur.fetchall()
