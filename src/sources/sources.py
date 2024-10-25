### Sources for obtaining news articles
import requests
import json
from enum import Enum

class Language(Enum):
    EN = "EN"
    NL = "NL"

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
        raise NotImplementedError

    def get_write_articles(self, filepath: str, processed=True):
        """
        Get articles and optionally format into proper JSON formatting to write to a JSON file.
        """
        raise NotImplementedError

    def preprocess_articles(self, articles: dict) -> dict:
        """
        Preprocess the articles from their RSS feed format to the proper JSON formatting.
        """
        raise NotImplementedError


class NOSNewsSource(NewsSource):
    """
    NewsSource object wrapping NOS.nl
    """
    def __init__(self, api_url: str):
        self.api_url = api_url
        self.language = Language.NL

    def get_articles(self, processed=True) -> dict:
        """
        Get articles from NOS.nl and optionally format into the proper JSON formatting.
        """
        articles = requests.get(self.api_url + "/api/nos").json()
        if processed:
            articles = self.preprocess_articles(articles)

        return articles

    def get_write_articles(self, filepath: str, processed=True):
        """
        Get from NOS.nl articles and optionally format into proper JSON formatting to write to a JSON file.
        """
        articles = requests.get(self.api_url + "/api/nos").json()
        
        if processed:
            articles = self.preprocess_articles(articles)
        
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
    def __init__(self, api_url: str):
        self.api_url = api_url
        self.language = Language.NL

    def get_articles(self, processed=True) -> dict:
        """
        Get articles from AD.nl and optionally format into the proper JSON formatting.
        """
        articles = requests.get(self.api_url + "/api/ad").json()
        if processed:
            articles = self.preprocess_articles(articles)

        return articles

    def get_write_articles(self, filepath: str, processed=True):
        """
        Get from AD.nl articles and optionally format into proper JSON formatting to write to a JSON file.
        """
        articles = requests.get(self.api_url + "/api/ad").json()
        
        if processed:
            articles = self.preprocess_articles(articles)
        
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
    def __init__(self, api_url: str):
        self.api_url = api_url
        self.language = Language.NL

    def get_articles(self, processed=True) -> dict:
        """
        Get articles from Telegraaf.nl and optionally format into the proper JSON formatting.
        """
        articles = requests.get(self.api_url + "/api/telegraaf").json()
        if processed:
            articles = self.preprocess_articles(articles)

        return articles

    def get_write_articles(self, filepath: str, processed=True):
        """
        Get articles from Telegraaf.nl and optionally format into proper JSON formatting to write to a JSON file.
        """
        articles = requests.get(self.api_url + "/api/telegraaf").json()
        
        if processed:
            articles = self.preprocess_articles(articles)
        
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
    def __init__(self, api_url: str):
        self.api_url = api_url
        self.language = Language.NL

    # TODO RSS feed only contains title and link, no description
    def get_articles(self, processed=True) -> dict:
        """
        Get articles from Volkskrant.nl and optionally format into the proper JSON formatting.
        """
        articles = requests.get(self.api_url + "/api/volkskrant").json()
        if processed:
            articles = self.preprocess_articles(articles)

        return articles

    def get_write_articles(self, filepath: str, processed=True):
        """
        Get articles from Volkskrant.nl and optionally format into proper JSON formatting to write to a JSON file.
        """
        articles = requests.get(self.api_url + "/api/volkskrant").json()
        
        if processed:
            articles = self.preprocess_articles(articles)
        
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
    def __init__(self, api_url: str):
        self.api_url = api_url
        self.language = Language.NL

    def get_articles(self, processed=True) -> dict:
        """
        Get articles from NRC.nl and optionally format into the proper JSON formatting.
        """
        articles = requests.get(self.api_url + "/api/nrc").json()
        if processed:
            articles = self.preprocess_articles(articles)

        return articles

    def get_write_articles(self, filepath: str, processed=True):
        """
        Get from NRC.nl articles and optionally format into proper JSON formatting to write to a JSON file.
        """
        articles = requests.get(self.api_url + "/api/nrc").json()
        
        if processed:
            articles = self.preprocess_articles(articles)
        
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
