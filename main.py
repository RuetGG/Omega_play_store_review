from src.scraper.reviews import *
from src.scraper.processor import *
import pandas as pd

APP_ID = "com.combanketh.mobilebanking"

def run():
    reviews = get_app_reviews(APP_ID, count=500)
    df = pd.DataFrame(reviews)
    
    df = preprocessed_reviews(df)
    df.to_csv('data/clean/reviews_clean.csv', index=False)
    

if __name__ == '__main__':
    run()