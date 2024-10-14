# re-boring-report
Reverse engineering [Boring Report](https://www.boringreport.com) 

## Project Description
This project is an attempt at reverse engineering the inner workings of Boring Report from scratch. I had the idea of a similar tool in my mind to build a neutral aggregated news source to limit endless doomscrolling and varied, possibly biased news intake by using generative AI.

One of the limitations I found with the original Boring Report is its generally US-focused news, which I want to make more customizable by being able to select your own (local) news sources.

## High-level System Description
The system is practically a three-step process.

First the news articles need to be obtained from the news sources and stored in a `.json` file.
```
{
    "source_url": ...,
    "source_text": ...,
    "published_datetime": ...,
    "article_title": ...,
    "article_text": ...
}
```

TODO Next, articles reporting the same news need to be clustered.

TODO Finally, the clustered articles need to be aggregated and rewritten into one, neutral article.
