import numpy as np
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
import torch
from transformers import AutoTokenizer, AutoModel
import hdbscan
from sources.sources import Language
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class BertClustering():
    """
    Object handling clustering of articles.
    """

    def __init__(self, news_sources: list):
        self.news_sources = news_sources

        self.articles = []
        for news_source in self.news_sources:
            self.articles += news_source.get_articles()

        self.model_name = "bert-base-multilingual-uncased"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModel.from_pretrained(self.model_name)
        self.clusterer = hdbscan.HDBSCAN(min_cluster_size=10,
                                         metric="euclidean")
        nltk.download("stopwords")
        nltk.download("punkt")

    def remove_stop_words(self, article: str, language: Language):
        """
        Remove (language-specific) stop words from the article text.
        """
        stopwords_set = set(stopwords.words(language))
        article_wordslist = word_tokenize(article)
        filtered_words = filter(lambda word:
                                word.lower() not in stop_words,
                                article_wordslist)
        article_nostop = ' '.join(filtered_words)
        return article_nostop

    def preprocess_articles(self, sources_articles: list):
        """
        Pre-process the articles to use as model input for embedding
        clustering.
        """
        processed_articles = []
        for source, article in sources_articles:
            article_title = article["article_title"]
            article_text = article["article_text"]
            article_title_nostop = self.remove_stop_words(
                article, source.language)
            article_text_nostop = self.remove_stop_words(
                article, source.language)
            text_article = f"# Title:\n{article_title_nostop}\n\n# Text:\n{article_text}"
            processed_articles.append(text_article)
        return processed_articles

    def format_articles(self, articles: list):
        """
        Format the articles to use as model input for rewriting.
        """
        formatted_articles = []
        for article in articles:
            article_title = article["article_title"]
            article_text = article["article_text"]
            text_article = f"# Title:\n{article_title}\n\n# Text:\n{article_text}"
            formatted_articles.append(text_article)
        return formatted_articles

    def get_embeddings(self, articles: list):
        """
        Get BERT embeddings from articles.
        """
        inputs = self.tokenizer(
            articles,
            padding=True,
            truncation=True,
            return_tensors="pt",
            max_length=512
        )
        with torch.no_grad():
            outputs = self.model(**inputs)
            embeddings = outputs.last_hidden_state.mean(dim=1).cpu().numpy()
            normalized_embeddings = normalize(embeddings)
            pca = PCA(n_components=10)
            reduced_embeddings = pca.fit_transform(normalized_embeddings)
        return reduced_embeddings

    def get_cluster_labels(self, embeddings: np.ndarray):
        """
        Get cluster labels from embeddings using HDBSCAN.
        """
        labels = self.clusterer.fit_predict(embeddings)
        return labels
