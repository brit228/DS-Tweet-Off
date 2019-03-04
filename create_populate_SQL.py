import psycopg2


user = "qnhiusek"
password = "F1e0AqF_XxEMiMsfzI4-c2BaLYg3woiV"
db = "qnhiusek"
server = "stampy.db.elephantsql.com"
conn = psycopg2.connect(dbname=db, user=user, password=password, host=server)
curs = conn.cursor()
curs.execute("""
    SELECT COUNT(*)
    FROM information_schema.schemata
    WHERE schema_name='twitoff';
""")
if curs.fetchone()[0] == 0:
    curs.execute("""
        CREATE SCHEMA twitoff
        AUTHORIZATION {};
    """.format(user))

curs.execute("""
    SELECT COUNT(*)
    FROM pg_catalog.pg_tables
    WHERE
        schemaname='twitoff'
        AND tablename='tweet';
""")
if curs.fetchone()[0] == 0:
    curs.execute("""
        CREATE TABLE twitoff.tweet
        (
            id integer UNIQUE NOT NULL,
            created_at timestamp,
            text varchar (256),
            user_id integer NOT NULL
        );
    """)
curs.execute("""
    SELECT COUNT(*)
    FROM pg_catalog.pg_tables
    WHERE
        schemaname='twitoff'
        AND tablename='user';
""")
if curs.fetchone()[0] == 0:
    curs.execute("""
        CREATE TABLE twitoff.user
        (
            id integer UNIQUE NOT NULL
        );
    """)

curs.execute("""
    SELECT *
    FROM pg_catalog.pg_tables
    WHERE schemaname='twitoff';
""")
print(curs.fetchall())

curs.commit()
curs.close()
conn.close()
