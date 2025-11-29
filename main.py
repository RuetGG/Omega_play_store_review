from src.scraper.reviews import *
from src.scraper.processor import *
import pandas as pd

BANKS = {
    "CBE": "com.combanketh.mobilebanking",
    "Dashen":"com.dashen.dashensuperapp",
    "Abyssinia":"com.boa.boaMobileBanking" 
    }


def run():
    app_banks_df = []
    
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/clean", exist_ok=True)
    for bank_name, app_id in BANKS.items():
        
        reviews = get_app_reviews(app_id, count=900)
        if not reviews:
            print(f"Warning: No reviews found for {bank_name}. Skipping...")
            continue
        print(f"{bank_name}: {len(reviews)} reviews scraped")

        df = preprocessed_reviews(reviews, bank_name)
        
        df.to_csv(f"data/clean/{bank_name}_reviews.csv", index=False)
        
        app_banks_df.append(df)
        print("Saved", len(df), "reviews for", bank_name)
        
        
    combine = pd.concat(app_banks_df, ignore_index=True)
    combine.to_csv("data/clean/all_bank_review.csv", index=False)
    print("Successfull")        
        

if __name__ == '__main__':
    run()