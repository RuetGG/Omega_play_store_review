from google_play_scraper import app, reviews

def get_app_info(app_id):
    return app(app_id, lang='en',country='us')

# app_id = "com.combanketh.mobilebanking"
def get_app_reviews(app_id, count=100):
    result, _ = reviews(
        app_id,
        lang='en',
        country='us',
        count=count
        
    )
    return result

