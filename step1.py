import requests

from pathlib import Path
from pprint import pprint


def download_picture(url, path, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(path + filename, 'wb') as file:
        file.write(response.content)


def get_link(url):
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()["links"]["flickr"]["original"]
    return links


# Подумай над названием функции(fetch_spacex_last_launch).
def fetch_spacex_last_launch(links, path):
    for link_number, link in enumerate(links):
        link_number += 1
        download_picture(link, path, filename="spacex{}.jpeg".format(link_number))


Path(r"e:\Python\DVMN2\photo_inst\venv\Include\inst_photo\\Test").mkdir(parents=True, exist_ok=True)

url_spacex = "https://api.spacexdata.com/v4/launches/latest"
path = r"e:\Python\DVMN2\photo_inst\venv\Include\inst_photo\Test\\"

fetch_spacex_last_launch(get_link(url_spacex), path)
