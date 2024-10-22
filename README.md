# re-boring-report
Reverse engineering [Boring Report](https://www.boringreport.com) 

## Project Description
This project is an attempt at reverse engineering the inner workings of Boring Report from scratch.
I had the idea of a similar tool in my mind to build a neutral aggregated news source to limit endless doomscrolling and varied, possibly biased news intake by using generative AI.

One of the limitations I found with the original Boring Report is its generally US-focused news, which I want to make more customizable by being able to select your own (local) news sources.

## Getting Started
To get started, you have to install the requirements, preferrably in a virtual environment.
To create a virtual environment, use the following command:

```python3 -m venv venv```

This creates a virtual environment in the `venv` folder.
To activate this virtual environment, run the following command:

```source venv/bin/activate```

To install the dependencies for this project, run the following command whilst in the virtual environment:

```pip install -r requirements.txt```

Further details about the usage of the library are on the way, once the implementation is sufficiently complete.


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
Right now, this is done using BERT base multilingual and HDB scan for clustering.
This configuration requires tweaking to be usable.

TODO Finally, the clustered articles need to be aggregated and rewritten into one, neutral article.
Right now, this is done using the Google FLAN-T5 Sequence-to-Sequence model, with a simple rewriting instruction.

## Future Ideas
- Language-agnostic embeddings and rewrites into a language of choice
