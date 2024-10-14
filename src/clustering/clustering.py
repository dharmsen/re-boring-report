import numpy as np
from sklearn.preprocessing import normalize
import torch
from transformers import AutoTokenizer, AutoModel
import hdbscan

from sources.sources import NOSNewsSource, ADNewsSource, TelegraafNewsSource, VolkskrantNewsSource, NRCNewsSource

class BertClustering():
    """
    Object handling clustering of articles.
    """
    def __init__(self, news_sources: list):
        self.news_sources = news_sources

        self.articles = []
        for news_source in self.news_sources:
            self.articles += news_source.get_articles()

        self.model_name = "bert-base-uncased"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModel.from_pretrained(self.model_name)
        self.clusterer = hdbscan.HDBSCAN(min_cluster_size=1, metric="euclidian")

    def preprocess_articles(self, articles: list):
        """
        Pre-process the articles to use as model input
        """
        processed_articles = []
        for article in articles:
            article_title = article["article_title"]
            article_text = article["article_text"]
            text_article = f"# Title:\n{article_title}\n\n#Text:\n{article_text}"
            processed_articles.append(text_article)
        return processed_articles

    def get_embeddings(self, articles: list):
        """
        Get BERT embeddings from articles.
        """
        inputs = self.tokenizer(articles, padding=True, truncation=True, return_tensors="pt", max_length=512)
        with torch.no_grad():
            outputs = self.model(**inputs)
            embeddings = outputs.last_hidden_state.mean(dim=1).cpu().numpy()
        return normalize(embeddings)
