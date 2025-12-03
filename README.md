# Omega Bank Reviews Scraper
## Overview

### This project scrapes and preprocesses Google Play Store reviews for Ethiopian banks. The goal is to collect user feedback, ratings, and review dates for analysis.

## Currently supported banks:

Commercial Bank of Ethiopia (CBE)

Dashen Bank

Bank of Abyssinia

### The scraper collects at least 600 reviews per bank, cleans the text, normalizes dates, removes duplicates, and saves the data as CSV files.

## Features

Scrapes reviews, ratings, and dates from Google Play Store.

Preprocesses review text (removes duplicates, handles missing data, normalizes dates).

Adds metadata columns: bank and source.

Saves per-bank CSV and a combined CSV dataset.

Handles apps with 0 reviews gracefully.

# PostgreSQL Database Schema

## The cleaned review data is stored in a PostgreSQL database (bank_reviews) with two tables:

## banks Table
### Column	Type	Description
bank_id	SERIAL PRIMARY KEY	Unique identifier for each bank
bank_name	VARCHAR(255)	Short name of the bank
app_name	VARCHAR(255)	Full name of the bank/app

## reviews Table
### Column	Type	Description
review_id	SERIAL PRIMARY KEY	Unique identifier for each review
bank_id	INT REFERENCES banks(bank_id) ON DELETE CASCADE	Links to the bank
review_text	TEXT	Cleaned review text
rating	NUMERIC(2,1)	User rating
review_date	DATE	Date of the review
sentiment_label	VARCHAR(20)	Predicted sentiment (POSITIVE/NEGATIVE)
sentiment_score	NUMERIC(3,2)	Confidence score of the sentiment
source	VARCHAR(50)	Source of the review (e.g., Google Play)

### Data integrity checks include counting reviews per bank, average ratings, and sentiment distribution to ensure proper insertion.

## Installation

Clone the repository:
```bash
git clone https://github.com/RuetGG/Omega_play_store_review.git
cd Omega_play_store_review
```

##Create a virtual environment and activate it:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

Install required packages:
```bash
pip install -r requirements.txt
```

Run the Scraper
```bash
python main.py
```
