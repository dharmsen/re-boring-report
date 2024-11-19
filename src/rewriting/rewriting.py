from transformers import AutoTokenizer, T5ForConditionalGeneration


class Rewriter:
    """
    Base class for rewriting articles.
    """

    def rewrite_article(self, article: str) -> str:
        """
        Rewrite a single article.
        """
        raise NotImplementedError

    def rewrite_articles(self, articles: list) -> list:
        """
        Rewrite a list of articles.
        """
        return [self.rewrite_article(article) for article in articles]


class T5Rewriter(Rewriter):
    """
    Rewrite articles using a T5 model.
    """

    def __init__(self):
        self.model_name = "google/flan-t5-small"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name,
                                                       padding="max_length",
                                                       truncation=True,
                                                       max_length=512)
        self.model = T5ForConditionalGeneration.from_pretrained(
            self.model_name)

    def rewrite_article(self, article: str) -> str:
        """
        Rewrite a single article.
        """
        input_text = (
            "Rewrite the article such that it is neutral and objective. "
            "Keep the same format and language:\n\n"
            f"{article}"
        )
        input_ids = self.tokenizer(
            input_text,
            return_tensors="pt"
        ).input_ids  # .to("cuda")
        outputs = self.model.generate(input_ids, max_length=512)

        return self.tokenizer.decode(outputs[0])
