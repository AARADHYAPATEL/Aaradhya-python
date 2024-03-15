import requests
from bs4 import BeautifulSoup


def scrape_security_news():
    url = "https://www.cyberscoop.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h2', class_='security_headline')
    return [headline.text for headline in headlines]


# Example
security_headlines = scrape_security_news()
print("Security Headlines:", security_headlines)
