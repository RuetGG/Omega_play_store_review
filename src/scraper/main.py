# from src.scraper.reviews import *
# from src.scraper.processor import *
# import pandas as pd

# BANKS = {
#     "CBE": "com.combanketh.mobilebanking",
#     "Dashen":"com.dashen.dashensuperapp",
#     "Abyssinia":" com.boa.boaMobileBanking"
#     }


# def run():
#     app_banks_df = []
#     for bank_name, app_id in BANKS.items():
#         reviews = get_app_reviews(app_id, bank_name, count=500)
#         app_banks_df.append(reviews)
        
#     combine = pd.concat(app_banks_df, ignore_index=True)
#     combine.to_csv("data/clean/all_bank_review.csv", index=False)
#     print("Successfull")        
        

# if __name__ == '__main__':
#     run()