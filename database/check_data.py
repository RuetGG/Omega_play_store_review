import psycopg2

conn = psycopg2.connect(
    dbname='bank_reviews',
    user='postgres',
    password='Ruth',
    host='localhost',
    port='5432'
)
cur = conn.cursor()

cur.execute("""
    SELECT b.bank_name, COUNT(r.review_id) AS total_reviews
    FROM banks b
    JOIN reviews r ON b.bank_id = r.bank_id
    GROUP BY b.bank_name
    ORDER BY total_reviews DESC;
""")
counts = cur.fetchall()
print("Total reviews per bank:")
for bank_name, total in counts:
    print(f"{bank_name}: {total}")

cur.execute("""
    SELECT b.bank_name, ROUND(AVG(r.rating), 2) AS avg_rating
    FROM banks b
    JOIN reviews r ON b.bank_id = r.bank_id
    GROUP BY b.bank_name
    ORDER BY avg_rating DESC;
""")
avg_ratings = cur.fetchall()
print("\nAverage rating per bank:")
for bank_name, avg in avg_ratings:
    print(f"{bank_name}: {avg}")

cur.execute("""
    SELECT sentiment_label, COUNT(*) AS count_reviews
    FROM reviews
    GROUP BY sentiment_label
    ORDER BY count_reviews DESC;
""")
sentiment_counts = cur.fetchall()
print("\nReview counts by sentiment:")
for sentiment, count in sentiment_counts:
    print(f"{sentiment}: {count}")


cur.close()
conn.close()
