import pandas as pd
from transformers import pipeline

def load_csv(file: str):
    df = pd.read_csv(file)
    return df

df = load_csv('../../data/clean/all_bank_review.csv')
df.head()


sentiment_analysis = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

def get_sentiment(text):
    try:
        result = sentiment_analysis(text[:512])[0]
        return result['label'], result['score']
    except:
        return None, None
df['sentiment'], df['confidence'] = zip(*df['review'].apply(get_sentiment))

df['sentiment_score'] = df['sentiment'].map({
    'POSITIVE': 1,
    'NEGATIVE': -1
})

mean_by_bank = df.groupby('bank')['sentiment_score'].mean()
print(mean_by_bank)

mean_by_rating = df.groupby('rating')['sentiment_score'].mean()
print(mean_by_rating)
