import psycopg2
import uuid


class Database:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def setup_database(self):
        conn = psycopg2.connect(
            f"user={self.user} port={self.port} host={self.host} password={self.password}")
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute("""SELECT 1 FROM pg_database WHERE datname = '%s'""", self.database)
        exists = cur.fetchone()

        if not exists:
            cur.execute('CREATE DATABASE "BlackMambaBot"')

        cur.close()
        conn.close()

    def setup_tables(self):
        conn = psycopg2.connect(
            f"dbname={self.database} user={self.user} port={self.port} host={self.host} password={self.password}")
        cur = conn.cursor()
        cur.execute("""
                CREATE TABLE IF NOT EXISTS Themes (
                    id UUID PRIMARY KEY,
                    month DATE,
                    theme TEXT
                )
            """)

        cur.execute("""
                CREATE TABLE IF NOT EXISTS TodayThemes (
                    id UUID PRIMARY KEY,
                    themeId UUID REFERENCES Themes(id),
                    date DATE,
                    themeDay TEXT
                )
            """)

        conn.commit()
        cur.close()
        conn.close()

    def setup(self):
        try:
            self.setup_database()
            self.setup_tables()
            print("Database initial configuration OK")
        except psycopg2.Error as error:
            print(f"Error: {error}")

    def insert_themes(self, month, year, theme):
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
                f"dbname={self.database} user={self.user} port={self.port} host={self.host} password={self.password}")
            cur = conn.cursor()
            cur.execute("""SELECT id FROM Themes WHERE month = %s AND theme = %s""", (f"01/{month}/{year}", theme))
            result = cur.fetchone()

            if result:
                return None
            else:
                cur.execute("""INSERT INTO Themes (id, month, theme) VALUES (%s, %s, %s)""",
                            (str(uuid.uuid4()), f"01/{month}/{year}", theme))
                conn.commit()
                cur.execute("""SELECT id FROM Themes WHERE month = %s AND theme = %s""", (f"01/{month}/{year}", theme))
                result = cur.fetchone()
                return result[0]
        except psycopg2.Error as error:
            print(f"Error: {error}")
            if conn:
                conn.rollback()
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def search_themes(self):
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
                f"dbname={self.database} user={self.user} port={self.port} host={self.host} password={self.password}")
            cur = conn.cursor()
            cur.execute("""SELECT * FROM Themes""")
            result = cur.fetchall()
            return result
        except psycopg2.Error as error:
            print(f"Error: {error}")
            if conn:
                conn.rollback()
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def insert_themes_day(self, id_theme, day, month, year, theme):
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
                f"dbname={self.database} user={self.user} port={self.port} host={self.host} password={self.password}")
            cur = conn.cursor()
            cur.execute("""INSERT INTO todaythemes (id, themeId, date, themeDay) VALUES (%s, %s, %s, %s)""",
                        (str(uuid.uuid4()), str(id_theme), f"{day}/{month}/{year}", str(theme)))
            conn.commit()
            cur.execute("""SELECT id FROM todaythemes WHERE themeId = %s""", (str(id_theme),))
            result = cur.fetchall()
            return result
        except psycopg2.Error as error:
            print(f"Error: {error}")
            if conn:
                conn.rollback()
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def search_themes_day(self):
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
                f"dbname={self.database} user={self.user} port={self.port} host={self.host} password={self.password}")
            cur = conn.cursor()
            cur.execute("""SELECT * FROM todaythemes""")
            result = cur.fetchall()
            return result
        except psycopg2.Error as error:
            print(f"Error: {error}")
            if conn:
                conn.rollback()
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def search_themes_day_per_month(self, month, year):
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
                f"dbname={self.database} user={self.user} port={self.port} host={self.host} password={self.password}")
            cur = conn.cursor()
            cur.execute("""SELECT * FROM todaythemes WHERE date >= %s AND date < %s ORDER BY date""",
                        (f"{year}/{month}/01", f"{year}/{int(month) + 1}/01"))
            result = cur.fetchall()
            return result
        except psycopg2.Error as error:
            print(f"Error: {error}")
            if conn:
                conn.rollback()
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def search_themes_day_per_day(self, day, month, year):
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
                f"dbname={self.database} user={self.user} port={self.port} host={self.host} password={self.password}")
            cur = conn.cursor()
            cur.execute("""SELECT * FROM todaythemes WHERE date = %s""",
                        f"{year}/{month}/{day}")
            result = cur.fetchall()
            return result
        except psycopg2.Error as error:
            print(f"Error: {error}")
            if conn:
                conn.rollback()
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()


db = Database(database="BlackMambaBot", user="postgres", password="1234", host="localhost", port="5432")

print(db.search_themes_day_per_month(month="01", year="2024"))
