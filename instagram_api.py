import json

import requests

API_HOST = "www.instagram.com"
PROTOCOL = "https"


def _api_path(hash_tag):
    """
    Instagram secret API path
    """
    return f"{PROTOCOL}://{API_HOST}/explore/tags/{hash_tag}/"


def get_image_urls_by_hash_tag(hash_tag):
    """
    Returns list of top instagram images by a hashtag
    :param hash_tag: Hashtag to fetch images
    """

    # Get response from instagram
    response_bytes = requests.get(_api_path(hash_tag), params={"__a": 1}).content

    # Load response into dictionary
    response_dict = json.loads(response_bytes)

    # Fetch all response images
    response_images = response_dict['graphql']['hashtag']['edge_hashtag_to_top_posts']['edges']

    # Extract image urls from images
    urls = list(map(lambda image: image['node']['display_url'], response_images))

    return urls
