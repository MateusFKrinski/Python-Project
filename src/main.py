import calendar
import datetime

import gemini.generate_generic_theme as gemini_theme
from database import Database
from gemini import Gemini
from gemini.description_theme import description_theme
from gemini.description_theme import generate_text_by_theme
from twitter import post_tweet

date_today = datetime.date.today()
days_in_month = calendar.monthrange(date_today.year, date_today.month)

db = Database(database="BlackMambaBot", user="postgres",
              password="1234", host="localhost", port="5432")

db.setup()

actual_mouth_theme = db.search_themes_day_per_month(str(date_today.month), date_today.year)

validate_exist_publication_day = False

for i in range(len(actual_mouth_theme)):
    if actual_mouth_theme[i][2] == date_today:
        validate_exist_publication_day = True

if not validate_exist_publication_day:
    theme_base = gemini_theme.generic_theme
    theme = Gemini(theme_base)
    base_theme = theme.generate_theme_base()
    day_themes_publications = theme.generate_themes(base_theme)

    id_table = db.insert_themes(date_today.month, date_today.year, theme_base)

    try:
        publication = generate_text_by_theme(description_theme(day_themes_publications))

        db.insert_themes_day(id_table, date_today.day, date_today.month, date_today.year, publication)

    except Exception as e:
        print(f"Error encountered during day processing: {e}")

date_string = str(date_today).replace("-", "/")
publication_day = db.search_themes_day_per_day(date_string)
today_publication = publication_day[0][3]

payload = {"text": today_publication}

post_tweet(payload)
