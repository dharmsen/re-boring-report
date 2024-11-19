# APIs for obtaining news articles from news sources

from flask import Flask, jsonify
import requests
import xmltodict

app = Flask(__name__)


def rss_to_json(rss_feed_url: str) -> dict:
    """
    Standard function for converting RSS feed (in XML) to JSON.
    """
    try:
        response = requests.get(rss_feed_url)
        response.raise_for_status()

        rss_data = xmltodict.parse(response.content)

        return jsonify(rss_data)
    except requests.exceptions.RequestException as e:
        return jsonify(
            {"error": "Failed to fetch RSS feed",
             "message": str(e)}), 500


@app.route("/api/nos", methods=["GET"])
def nos_rss_to_json():
    RSS_FEED_URL = "https://feeds.nos.nl/nosnieuwsalgemeen"
    return rss_to_json(RSS_FEED_URL)


@app.route("/api/ad", methods=["GET"])
def ad_rss_to_json():
    RSS_FEED_URL = "https://www.ad.nl/nieuws/rss.xml"
    return rss_to_json(RSS_FEED_URL)


@app.route("/api/telegraaf", methods=["GET"])
def telegraaf_rss_to_json():
    RSS_FEED_URL = "https://www.telegraaf.nl/rss"
    return rss_to_json(RSS_FEED_URL)


@app.route("/api/volkskrant", methods=["GET"])
def volkskrant_rss_to_json():
    # TODO functional but only contains link, no description
    RSS_FEED_URL = "https://www.volkskrant.nl/voorpagina/rss.xml"
    return rss_to_json(RSS_FEED_URL)


@app.route("/api/nrc", methods=["GET"])
def nrc_rss_to_json():
    RSS_FEED_URL = "https://feeds.feedburner.com/nrc/FmXV"
    return rss_to_json(RSS_FEED_URL)


# TODO NOT FUNCTIONAL YET
# @app.route("/api/nieuwsnl", methods=["GET"])
# def nieuwsnl_rss_to_json():
#     RSS_FEED_URL = "https://nieuws.nl/feed"
#     return rss_to_json(RSS_FEED_URL)


# TODO NOT FUNCTIONAL YET
# @app.route("/api/nu", methods=["GET"])
# def nu_rss_to_json():
#     RSS_FEED_URL = "https://www.nu.nl/nu-rss.html"
#     return rss_to_json(RSS_FEED_URL)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
