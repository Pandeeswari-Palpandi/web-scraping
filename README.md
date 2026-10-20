# web-scraping

A small Python script that scrapes and prints the five latest headlines shown on
the BBC News India page.

## Requirements

- Python 3
- `requests`
- `beautifulsoup4`

Install the dependencies with:

```bash
python -m pip install requests beautifulsoup4
```

## Usage

Run the script from the project directory:

```bash
python headlines.py
```

The script fetches `https://www.bbc.com/news/world/asia/india` and prints up to
five headlines, numbered in order. An internet connection is required.
