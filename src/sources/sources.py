### Sources for obtaining news articles
import requests
import json

class NewsSource():
    """
    NewsSource object wrapping an API for obtaining articles from a specific news source API and formatting as needed.
    """
    def __init__(self, api_url: str):
        self.api_url = api_url

    def get_articles(self, processed=True) -> dict:
        """
        Get articles and optionally format into the proper JSON formatting.
        """
        ...

    def get_write_articles(self, filepath: str, processed=True):
        """
        Get articles and optionally format into proper JSON formatting to write to a JSON file.
        """
        ...

    def preprocess_articles(self, articles: dict) -> dict:
        """
        Preprocess the articles from their RSS feed format to the proper JSON formatting.
        """
        ...


class NOSNewsSource(NewsSource):
    """
    NewsSource object wrapping NOS.nl
    """
    def get_articles(self) -> dict:
        """
        Get articles from NOS.nl and optionally format into the proper JSON formatting.
        """
        articles = requests.get(self.api_url + "/api/nos").json()
        if processed:
            processed_articles = preprocess_articles(articles)

        return articles

    def get_write_articles(self, filepath: str, processed=True):
        """
        Get from NOS.nl articles and optionally format into proper JSON formatting to write to a JSON file.
        """
        articles = requests.get(self.api_url + "/api/nos").json()
        
        if processed:
            processed_articles = preprocess_articles(articles)
        
        with open(filepath, "w") as file:
            json.dump(articles, file, indent=4)

    def preprocess_articles(self, articles: dict) -> dict:
        """
        Preprocess the NOS.nl articles from their RSS feed format to the proper JSON formatting.
        """
        preprocessed_articles = []
        for article in articles["rss"]["channel"]["item"]:
            preprocessed_article = {
                "source_url": article["link"],
                "source_text": "NOS.nl",
                "published_datetime": article["pubDate"],
                "article_title": article["title"],
                "article_text": article["description"]
            }
            preprocessed_articles.append(preprocessed_article)

        return preprocessed_articles


class ADNewsSource(NewsSource):
    """
    NewsSource object wrapping AD.nl
    """
    def get_articles(self) -> dict:
        """
        Get articles from AD.nl and optionally format into the proper JSON formatting.
        """
        articles = requests.get(self.api_url + "/api/ad").json()
        if processed:
            processed_articles = preprocess_articles(articles)

        return articles

    def get_write_articles(self, filepath: str, processed=True):
        """
        Get from AD.nl articles and optionally format into proper JSON formatting to write to a JSON file.
        """
        articles = requests.get(self.api_url + "/api/ad").json()
        
        if processed:
            processed_articles = preprocess_articles(articles)
        
        with open(filepath, "w") as file:
            json.dump(articles, file, indent=4)

    def preprocess_articles(self, articles: dict) -> dict:
        """
        Preprocess the AD.nl articles from their RSS feed format to the proper JSON formatting.
        """
        preprocessed_articles = []
        for article in articles["rss"]["channel"]["item"]:
            preprocessed_article = {
                "source_url": article["link"],
                "source_text": "AD.nl",
                "published_datetime": article["pubDate"],
                "article_title": article["title"],
                "article_text": article["description"]
            }
            preprocessed_articles.append(preprocessed_article)

        return preprocessed_articles



class TelegraafNewsSource(NewsSource):
    """
    NewsSource object wrapping Telegraaf.nl
    """
    def get_articles(self) -> dict:
        """
        Get articles from Telegraaf.nl and optionally format into the proper JSON formatting.
        """
        articles = requests.get(self.api_url + "/api/telegraaf").json()
        if processed:
            processed_articles = preprocess_articles(articles)

        return articles

    def get_write_articles(self, filepath: str, processed=True):
        """
        Get articles from Telegraaf.nl and optionally format into proper JSON formatting to write to a JSON file.
        """
        articles = requests.get(self.api_url + "/api/telegraaf").json()
        
        if processed:
            processed_articles = preprocess_articles(articles)
        
        with open(filepath, "w") as file:
            json.dump(articles, file, indent=4)

    def preprocess_articles(self, articles: dict) -> dict:
        """
        Preprocess the Telegraaf.nl articles from their RSS feed format to the proper JSON formatting.
        """
        preprocessed_articles = []
        for article in articles["rss"]["channel"]["item"]:
            preprocessed_article = {
                "source_url": article["link"],
                "source_text": "Telegraaf.nl",
                "published_datetime": article["pubDate"],
                "article_title": article["title"],
                "article_text": article["description"]["p"]["#text"]
            }
            preprocessed_articles.append(preprocessed_article)

        return preprocessed_articles



class VolkskrantNewsSource(NewsSource):
    """
    NewsSource object wrapping Volkskrant.nl
    """
    # TODO RSS feed only contains title and link, no description
    def get_articles(self) -> dict:
        """
        Get articles from Volkskrant.nl and optionally format into the proper JSON formatting.
        """
        articles = requests.get(self.api_url + "/api/volkskrant").json()
        if processed:
            processed_articles = preprocess_articles(articles)

        return articles

    def get_write_articles(self, filepath: str, processed=True):
        """
        Get articles from Volkskrant.nl and optionally format into proper JSON formatting to write to a JSON file.
        """
        articles = requests.get(self.api_url + "/api/volkskrant").json()
        
        if processed:
            processed_articles = preprocess_articles(articles)
        
        with open(filepath, "w") as file:
            json.dump(articles, file, indent=4)

    def preprocess_articles(self, articles: dict) -> dict:
        """
        Preprocess the Volkskrant.nl articles from their RSS feed format to the proper JSON formatting.
        """
        preprocessed_articles = []
        for article in articles["rss"]["channel"]["item"]:
            preprocessed_article = {
                "source_url": article["link"],
                "source_text": "AD.nl",
                "published_datetime": article["pubDate"],
                "article_title": article["title"],
                "article_text": article["description"]
            }
            preprocessed_articles.append(preprocessed_article)

        return preprocessed_articles



class NRCNewsSource(NewsSource):
    """
    NewsSource object wrapping NRC.nl
    """
    def get_articles(self) -> dict:
        """
        Get articles from NRC.nl and optionally format into the proper JSON formatting.
        """
        articles = requests.get(self.api_url + "/api/nrc").json()
        if processed:
            processed_articles = preprocess_articles(articles)

        return articles

    def get_write_articles(self, filepath: str, processed=True):
        """
        Get from NRC.nl articles and optionally format into proper JSON formatting to write to a JSON file.
        """
        articles = requests.get(self.api_url + "/api/nrc").json()
        
        if processed:
            processed_articles = preprocess_articles(articles)
        
        with open(filepath, "w") as file:
            json.dump(articles, file, indent=4)

    def preprocess_articles(self, articles: dict) -> dict:
        """
        Preprocess the NRC.nl articles from their RSS feed format to the proper JSON formatting.
        """
        preprocessed_articles = []
        for article in articles["rss"]["channel"]["item"]:
            preprocessed_article = {
                "source_url": article["link"],
                "source_text": "NRC.nl",
                "published_datetime": article["pubDate"],
                "article_title": article["title"],
                "article_text": article["description"]
            }
            preprocessed_articles.append(preprocessed_article)

        return preprocessed_articles

