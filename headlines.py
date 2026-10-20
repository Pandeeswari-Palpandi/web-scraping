import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news/world/asia/india"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.select('[data-testid="card-headline"]')

for i, headline in enumerate(headlines[:5], start=1):
    print(f"{i}. {headline.get_text(strip=True)}")
