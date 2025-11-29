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