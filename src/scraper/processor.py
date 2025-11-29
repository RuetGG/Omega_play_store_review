import re
import pandas as pd

def clean_review(text:str)->str:
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.strip()

def preprocessed_reviews(df: pd.DataFrame):
    df['clean_text'] = df['content'].apply(clean_review)
    return df