from google_play_scraper import reviews
import os
import re
import pandas as pd
from tqdm import tqdm


def clean_review(text:str)->str:
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.strip()

def preprocessed_reviews(review, bank_name: str, source:str="Google PlayStore")->pd.DataFrame:
    df = pd.DataFrame(review)
    
    df = df[['content', 'score', 'at']].copy()
    df = df.rename(columns={'content':'review', 'score':'rating', 'at':'date'}) 
    
    
    df['review'] = df['review'].apply(clean_review)
    
    df = df.drop_duplicates(subset='review')
    df = df.dropna(subset=['review', 'rating', 'date'])
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    df['bank'] = bank_name
    df['source'] = source
    
    return df

   