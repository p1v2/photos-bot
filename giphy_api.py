import random

import requests
import settings


class GiphyApiClient:
    api_key = settings.GIPHY_KEY
    api_url = "https://api.giphy.com/v1/gifs/"

    @staticmethod
    def _get_gif_original_url(gif_dict):
        """
        Returns gif url from fetched gif dict
        """
        return gif_dict["images"]["original"]["url"]

    def get_random_gif_url(self, word):
        """
        Return random gif url that matches search word
        """
        # Getting search url
        search_url = f"{self.api_url}search?api_key={self.api_key}&q={word}&limit=50&offset=0&rating=G&lang=en"

        # Fetching gifs
        response = requests.get(search_url).json()

        # Checking if data in response
        if not response.get("data"):
            raise ValueError(f"Error fetching giphy: {response}")

        # Getting list of gifs
        gifs = response["data"]

        # Choice random gif
        gif = random.choice(gifs)

        # Getting URL
        url = self._get_gif_original_url(gif)

        return url


giphy_client = GiphyApiClient()
