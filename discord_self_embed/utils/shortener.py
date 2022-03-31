import requests
import bs4
import sys

# TODO: find a shortener that doesnt have cloudflare block and free api

class Shortener:
    def __init__(self, bitly_token):
        self.api_url = "https://api-ssl.bitly.com"
        self.bitly_token = bitly_token

    def shorten(self, url):
        data = {"long_url": url}
        headers = {
            "Authorization": f"Bearer {self.bitly_token}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        }

        response = requests.post(self.api_url + "/v4/shorten", json=data, headers=headers)
        response.raise_for_status()

        return response.json()["link"]