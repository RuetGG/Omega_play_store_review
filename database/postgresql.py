import pandas as pd
import psycopg2

df = pd.read_csv('../data/processed/all_bank_reviews_with_themes.csv')


bank_mapping = {
    "CBE": "Commercial Bank of Ethiopia",
    "Dashen": "Dashen Bank",
    "Abyssinia": "Bank of Abyssinia"
}
df['app_name'] = df['bank'].map(bank_mapping)

conn = psycopg2.connect(
    dbname='bank_reviews',
    user='postgres',
    password='Ruth',
    host='localhost',
    port='5432'
)

cur = conn.cursor()
banks = df[['bank', 'app_name']].drop_duplicates()
for _, row in banks.iterrows():
    cur.execute("""
                INSERT INTO banks (bank_name, app_name)
                VALUES (%s, %s)
                ON CONFLICT (bank_name) DO NOTHING;
                """, (row['bank'], row['app_name']))
    
conn.commit()

cur.execute("SELECT bank_id, bank_name FROM banks;")
bank_id_map = {name: id_ for id_, name in cur.fetchall()}

review_tuples = [
    (
        bank_id_map[row['bank']],
        row['clean_review'],
        row['rating'],
        row['date'],
        row['sentiment'],
        row['sentiment_score'],
        row['source']
    )
    for _, row in df.iterrows()
]

cur.executemany("""
    INSERT INTO reviews (bank_id, review_text, rating, review_date, sentiment_label, sentiment_score, source)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""", review_tuples)

conn.commit()
cur.close()
conn.close()

