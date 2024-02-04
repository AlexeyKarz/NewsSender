import requests
import logging

file = open("apigmailpass.txt", "r")
content = file.read().split(", ")


class NewsFeed:
    """Representing multiple news titles and links as a single string
    """
    base_url = "http://newsapi.org/v2/everything?"
    api_key = content[0]

    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()
        try:
            response = requests.get(url)
            response.raise_for_status()
            articles = self._get_articles(url)

            email_body = ''
            for article in articles:
                email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

            return email_body

        except requests.RequestException as e:
            print(f"Request failed: {e}")
            logging.error(f"News fetch failed for self.interest: {e}")
            return None

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
        return url


if __name__ == "__main__":
    news_feed = NewsFeed(interest='nasa', from_date='2024-02-03', to_date='2024-02-04', language='en')
    print(news_feed.get())
