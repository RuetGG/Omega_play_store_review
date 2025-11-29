from google_play_scraper import app, reviews

def get_app_info(app_id):
    return app(app_id, lang='en',country='us')

def get_app_reviews(app_id, count=500):
    result, _ = reviews(
        app_id=app_id,
        lang='en',
        country='us',
        count=count,
    )
    return result

